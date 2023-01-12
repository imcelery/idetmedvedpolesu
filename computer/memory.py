import math

import numpy as np

from ventils import And, WireOut,  MultiplyWire, OrNot, Not, Or8, And4


class Trigger:
    def __init__(self):
        self._in1 = None
        self._in2 = None

        self._ornot1 = OrNot()
        self._ornot1.in1(0)

        self._ornot2 = OrNot()
        self._ornot2.in1(0)

        self._out1 = None
        self._out2 = None

        self._whire_ornot_out1 = MultiplyWire()
        self._whire_ornot_out2 = MultiplyWire()

        self._whire_final = WireOut()

        self._whire_promesh_ornot1 = WireOut()
        self._whire_promesh_ornot2 = WireOut()

        self._ornot1.set_out(self._whire_promesh_ornot1.in1)
        self._ornot2.set_out(self._whire_promesh_ornot2.in1)

        self._whire_ornot_out1.set_out([self._whire_final.in1, self._ornot2.in1])

        self._whire_ornot_out2.set_out([self._ornot1.in1])


    def set_out(self, out1):
        self._out1 = out1


    def _set_none(self):
        self._in1 = None
        self._in2 = None


    def _result(self):
        self._ornot1.in2(self._in1)
        self._ornot2.in2(self._in2)

        out1 = self._whire_promesh_ornot1.get_signal()
        out2 = self._whire_promesh_ornot2.get_signal()

        self._ornot1.in1(out2)
        self._ornot2.in1(out1)

        self._ornot1.in2(self._in1)
        self._ornot2.in2(self._in2)

        out1 = self._whire_promesh_ornot1.get_signal()
        out2 = self._whire_promesh_ornot2.get_signal()

        self._whire_ornot_out1.in1(out1)
        self._whire_ornot_out2.in1(out2)
        return self._whire_final.get_signal()


    def in1(self, value):
        self._in1 = value
        if self._in2 is not None:
            self._out1(self._result())
            self._set_none()


    def in2(self, value):
        self._in2 = value
        if self._in1 is not None:
            self._out1(self._result())
            self._set_none()


class MemoryBit:
    def __init__(self):
        # данные
        self._in1 = None
        #запомнить
        self._in2 = None

        self._and1 = And()
        self._and2 = And()

        self._no = Not()

        self._no.set_out(self._and1.in1)

        self._out1 = None


        self._whire_multiply1 = MultiplyWire()
        self._whire_multiply1.set_out([self._no.in1, self._and2.in1])

        self._whire_multiply2 = MultiplyWire()
        self._whire_multiply2.set_out([self._and1.in2, self._and2.in2])


        self._whire_out1 = WireOut()


        self._trigger = Trigger()
        self._trigger.set_out(self._whire_out1.in1)

        self._and1.set_out(self._trigger.in1)
        self._and2.set_out(self._trigger.in2)


    def set_out(self, out1):
        self._out1 = out1


    def _set_none(self):
        self._in1 = None
        self._in2 = None


    def _result(self):
        self._whire_multiply1.in1(self._in1)
        self._whire_multiply2.in1(self._in2)
        return self._whire_out1.get_signal()


    def in1(self, value):
        self._in1 = value
        if self._in2 is not None :
            self._out1(self._result())

            self._set_none()


    def in2(self, value):
        self._in2 = value
        if self._in1 is not None:
            self._out1(self._result())

            self._set_none()


class BinaryMemory8:
    def __init__(self):
        self._n = 8
        # входы A и B
        self._in_a = []
        self._in_b = None
        # бинпамять
        self._bm = []

        self._wire_out = []

        self._out = None

        for i in range(self._n):
            self._in_a.append(None)
            self._bm.append(MemoryBit())
            self._wire_out.append(WireOut())
            self._bm[i].set_out(self._wire_out[i].in1)


    def _set_none(self):
        # входы A и B
        self._in_a = [None] * self._n
        self._in_b = None

    def set_out(self, out):
        self._out = out


    def _result(self):

        for i in range(self._n):
            self._bm[i].in1(self._in_a[i])
            self._bm[i].in2(self._in_b)
        res = []
        for i in range(self._n):
            res.append(self._wire_out[i].get_signal())

        return reversed(res)

    def __getattr__(self, attr):
        if len(attr) >= 4 and (attr[:4] == "in_a" or attr == "in_b"):

            if attr != "in_b":
                i = int(attr[4:])
                s = attr[3]
            else:
                i = 0
                s = "b"
            def wrap(value):
                return self._in_summary(i, s, value)
            return wrap

    def _in_summary(self, i, s, value):
        if s == "b":
            self._in_b = value
        elif s == "a":
            self._in_a[i] = value

        a = True
        for i in self._in_a:
            if i is None:
                a = False
                break

        if a and self._in_b is not None:

            self._out(self._result())
            self._set_none()

    def in_a(self, a:list) -> None:
        for i in range(self._n):
            getattr(self, "in_a" + str(i))(a[self._n - i - 1])

class Selector8:
    def __init__(self):
        self._n = 8
        # входы A и B
        self._in_a = []
        self._in_b = []
        # ииии
        self._ands = []
        # или
        self._or = Or8()

        self._myltiWires = []
        self._myltiWiresOuts = [[], [], []]
        self._myltiNegativWires = []
        self._myltiNegativWiresOuts = [[], [], []]

        self._wire_out = WireOut()
        self._or.set_out(self._wire_out.in1)
        self._out = None

        self._nos = []

        for i in range(self._n):
            self._in_a.append(None)
            self._ands.append(And4())
            self._ands[i].set_out(eval("self._or.in" + str(i)))

        for i in range(math.ceil(self._n / 8) * 3):
            self._nos.append(Not())
            self._in_b.append(None)
            self._myltiWires.append((MultiplyWire()))
            self._myltiNegativWires.append((MultiplyWire()))
            self._nos[i].set_out(self._myltiNegativWires[i].in1)


        #ДЕЛАЦ С ЭТИ ЧТОТО ЕСЛИ ХОЧЕШ РАСШИРЯТСЯ цыдвлыдзлвыздлвыздлвдылвдлы

        for i in range(2):
            for j in range(2):
                for k in range(2):

                    if i:
                        self._myltiWiresOuts[0].append(self._ands[i * 4 + j * 2 + k * 1].ina)

                    else:

                        self._myltiNegativWiresOuts[0].append(self._ands[i * 4 + j * 2 + k * 1].ina)

                    if j:

                        self._myltiWiresOuts[1].append(self._ands[i * 4 + j * 2 + k * 1].ina)
                    else:

                        self._myltiNegativWiresOuts[1].append(self._ands[i * 4 + j * 2 + k * 1].ina)

                    if k:

                        self._myltiWiresOuts[2].append(self._ands[i * 4 + j * 2 + k * 1].ina)
                    else:

                        self._myltiNegativWiresOuts[2].append(self._ands[i * 4 + j * 2 + k * 1].ina)


        for i in range(math.ceil(self._n / 8) * 3):

            self._myltiWiresOuts[i].append(self._nos[i].in1)
            self._myltiWires[i].set_out(self._myltiWiresOuts[i])
            self._myltiNegativWires[i].set_out(self._myltiNegativWiresOuts[i])


    def _set_none(self):
        # входы A и B
        self._in_a = [None] * self._n
        self._in_b = [None] * math.ceil(self._n / 8) * 3


    def set_out(self, out):
        self._out = out


    def _result(self):

        for i in range(self._n):
            self._ands[i].ina(self._in_a[i])
        self._in_b = list(reversed(self._in_b))
        for i in range(math.ceil(self._n / 8) * 3):
            self._myltiWires[i].in1(self._in_b[i])

        res = self._wire_out.get_signal()
        return res

    def __getattr__(self, attr):
        if len(attr) > 4 and (attr[:4] == "in_a" or attr[:4] == "in_b"):

            i = int(attr[4:])
            s = attr[3]
            def wrap(value):
                return self._in_summary(i, s, value)
            return wrap

    def _in_summary(self, i, s, value):
        if s == "a":
            self._in_a[i] = value
        else:
            self._in_b[i] = value

        b = True
        for i in self._in_b:
            if i is None:
                b = False
                break

        if np.any(self._in_a) is not None and b:

            self._out(self._result())
            self._set_none()

    def in_a(self, a:list) -> None:
        for i in range(self._n):
            getattr(self, "in_a" + str(i))(a[self._n - i - 1])

    def in_b(self, b:list) -> None:
        for i in range(math.ceil(self._n / 8) * 3):
            getattr(self, "in_b" + str(i))(b[math.ceil(self._n / 8) * 3 - i - 1])


class DeSelector8:
    def __init__(self):
        self._n = 8
        # входы A и B
        self._in_a = None
        self._in_b = []
        # ииии
        self._ands = []
        # или
        self._or = Or8()

        self._myltiWires = []
        self._myltiWiresOuts = [[],[],[]]
        self._myltiNegativWires = []
        self._myltiNegativWiresOuts = [[],[],[]]

        self._wires_out = []

        self._out = None

        self._nos = []

        for i in range(self._n):
            self._wires_out.append(WireOut())
            self._ands.append(And4())
            self._ands[i].set_out(self._wires_out[i].in1)

        for i in range(math.ceil(self._n / 8) * 3):
            self._nos.append(Not())
            self._in_b.append(None)
            self._myltiWires.append((MultiplyWire()))
            self._myltiNegativWires.append((MultiplyWire()))
            self._nos[i].set_out(self._myltiNegativWires[i].in1)


        #ДЕЛАЦ С ЭТИ ЧТОТО ЕСЛИ ХОЧЕШ РАСШИРЯТСЯ цыдвлыдзлвыздлвыздлвдылвдлы

        for i in range(2):
            for j in range(2):
                for k in range(2):

                    if i:
                        self._myltiWiresOuts[0].append(self._ands[i * 4 + j * 2 + k * 1].ina)

                    else:

                        self._myltiNegativWiresOuts[0].append(self._ands[i * 4 + j * 2 + k * 1].ina)

                    if j:

                        self._myltiWiresOuts[1].append(self._ands[i * 4 + j * 2 + k * 1].ina)
                    else:

                        self._myltiNegativWiresOuts[1].append(self._ands[i * 4 + j * 2 + k * 1].ina)

                    if k:

                        self._myltiWiresOuts[2].append(self._ands[i * 4 + j * 2 + k * 1].ina)
                    else:

                        self._myltiNegativWiresOuts[2].append(self._ands[i * 4 + j * 2 + k * 1].ina)


        for i in range(math.ceil(self._n / 8) * 3):

            self._myltiWiresOuts[i].append(self._nos[i].in1)
            self._myltiWires[i].set_out(self._myltiWiresOuts[i])
            self._myltiNegativWires[i].set_out(self._myltiNegativWiresOuts[i])


    def _set_none(self):
        # входы A и B
        self._in_a = None
        self._in_b = [None] * math.ceil(self._n / 8) * 3


    def set_out(self, out):
        self._out = out


    def _result(self):

        for i in range(self._n):
            self._ands[i].ina(self._in_a)

        self._in_b = list(reversed(self._in_b))
        for i in range(math.ceil(self._n / 8) * 3):
            self._myltiWires[i].in1(self._in_b[i])

        res = []
        for i in self._wires_out:
            res.append(i.get_signal())
        return list(reversed(res))

    def __getattr__(self, attr):

        if len(attr) > 4 and attr[:4] == "in_b":


            i = int(attr[4:])
            s = attr[3]
            def wrap(value):
                return self._in_summary(i, s, value)
            return wrap

    def _in_summary(self, i, s, value):
        if s == "a":
            self._in_a = value
        else:
            self._in_b[i] = value

        b = True
        for i in self._in_b:
            if i is None:
                b = False
                break

        if self._in_a is not None and b:

            out = self._result()
            for i, el in enumerate(out):
                self._out[i](el)
            self._set_none()

    def in_a(self, value) -> None:
        self._in_summary(0, "a", value)

    def in_b(self, b:list) -> None:
        for i in range(math.ceil(self._n / 8) * 3):
            getattr(self, "in_b" + str(i))(b[math.ceil(self._n / 8) * 3 - i - 1])


class Ram8:
    def __init__(self):
        self._n = 8

        #адрес
        self._in_a = [None] * math.ceil(self._n / 8) * 3
        # запись
        self._in_b = None
        # ввод данных
        self._in_c = None

        self._desel = DeSelector8()
        self._sel = Selector8()

        self._wire_out = WireOut()


        self._out = None

        self._bm = []

        self._wire_out_mem = []


        for i in range(self._n):
            self._bm.append(MemoryBit())
            self._wire_out_mem.append(WireOut())
            self._bm[i].set_out(self._wire_out_mem[i].in1)


        self._desel.set_out([el.in2 for el in self._bm])


        self._sel.set_out(self._wire_out.in1)


    def _set_none(self):
        # входы A и B
        self._in_a = [None] * math.ceil(self._n / 8) * 3
        self._in_b = None
        self._in_c = None


    def set_out(self, out):
        self._out = out

    def _result(self):

        self._desel.in_a(self._in_b)

        self._in_a = list(reversed(self._in_a))

        self._desel.in_b(self._in_a)

        for i in range(self._n):
            self._bm[i].in1(self._in_c)

        self._sel.in_a([el.get_signal() for el in self._wire_out_mem])

        self._sel.in_b(self._in_a)

        res = self._wire_out.get_signal()
        return res

    def __getattr__(self, attr):

        if len(attr) > 4 and attr[:4] == "in_a":
            i = int(attr[4:])
            s = attr[3]
            def wrap(value):
                return self._in_summary(i, s, value)
            return wrap

    def _in_summary(self, i, s, value):
        if s == "b":
            self._in_b = value
        elif s == "c":
            self._in_c = value
        else:
            self._in_a[i] = value

        a = True
        for i in self._in_a:
            if i is None:
                a = False
                break

        if self._in_b is not None and self._in_c is not None and a:

            self._out(self._result())
            self._set_none()

    def in_b(self, value) -> None:
        self._in_summary(0, "b", value)

    def in_c(self, value) -> None:
        self._in_summary(0, "c", value)

    def in_a(self, b:list) -> None:
        for i in range(math.ceil(self._n / 8) * 3):
            getattr(self, "in_a" + str(i))(b[math.ceil(self._n / 8) * 3 - i - 1])




# class Clock:
#     def __init__(self):
#         self._no = Not()
#         self._out = None
#
#         self._and = And()
#
#         self._wireout = MultiplyWire()
#         self._wireoutfinal = WireOut()
#
#         self._wireout.set_out([ self._wireoutfinal.in1, self._and.in2])
#         self._no.set_out(self._wireout.in1)
#         self._and.set_out(self._no.in1)
#         self._and.in2(0)
#
#     def set_out(self, out):
#         self._out = out
#
#     def _result(self):
#         self._and.in1(1)
#         return self._wireoutfinal.get_signal()
#
#     def get_signal(self):
#         self._out(self._result())





