import math

from ventils import Xor, And, WireOut, Or, WireIn, MultiplyWire, OrNot, Not, Or8, And4

import numpy as np


class HalfAdder:
    """
    Полусумматор
    """
    def __init__(self):
        self._in_a = None
        self._in_b = None
        self._out_s = None  # разряд суммы
        self._out_co = None  # разряд переноса

        self._xor = Xor()
        self._and = And()
        self._wire1 = WireOut()
        self._wire2 = WireOut()

        self._xor.set_out(self._wire1.in1)
        self._and.set_out(self._wire2.in1)

    def _set_none(self):
        self._out_s = None
        self._out_co = None

    def _result(self):
        self._xor.in1(self._in_a)
        self._and.in1(self._in_a)
        self._xor.in2(self._in_b)
        self._and.in2(self._in_b)
        return self._wire1.get_signal(), self._wire2.get_signal()

    def in_a(self, value):
        """
        Установка входа _in_a
        :param value:
        :return:
        """
        self._in_a = value
        if self._in_b is not None:
            out1, out2 = self._result()
            self._out_s(out1)
            self._out_co(out2)
            self._set_none()

    def in_b(self, value):
        """
        Установка входа _in_b
        :param value:
        :return:
        """
        self._in_b = value
        if self._in_a is not None:
            out1, out2 = self._result()
            self._out_s(out1)
            self._out_co(out2)
            self._set_none()

    def set_out(self, out1, out2):
        self._out_s = out1
        self._out_co = out2

class BinaryAdder:
    """
    Сумматор
    """
    def __init__(self):
        self._in_ci = None
        self._in_a = None
        self._in_b = None
        self._out_s = None
        self._out_co = None

        self._ha1 = HalfAdder()
        self._ha2 = HalfAdder()
        self._or = Or()
        self._wire1 = WireOut()
        self._wire2 = WireOut()

        self._ha1.set_out(self._wire1.in1, self._or.in1)
        self._ha2.set_out(self._ha1.in_b, self._or.in2)
        self._or.set_out(self._wire2.in1)

    def _result(self):
        self._ha1.in_a(self._in_ci)
        self._ha2.in_a(self._in_a)
        self._ha2.in_b(self._in_b)
        return self._wire1.get_signal(), self._wire2.get_signal()

    def in_ci(self, value):
        self._in_ci = value
        if self._in_a is not None and self._in_b is not None:
            out1, out2 = self._result()
            self._out_s(out1)
            self._out_co(out2)
            self._set_none()

    def in_a(self, value):
        self._in_a= value
        if self._in_ci is not None and self._in_b is not None:
            out1, out2 = self._result()
            self._out_s(out1)
            self._out_co(out2)
            self._set_none()

    def in_b(self, value):
        self._in_b = value
        if self._in_ci is not None and self._in_a is not None:
            out1, out2 = self._result()
            self._out_s(out1)
            self._out_co(out2)
            self._set_none()

    def set_out(self, out1, out2):
        self._out_s = out1
        self._out_co = out2

    def _set_none(self):
        self._in_ci = None
        self._in_a = None
        self._in_b = None


class BinaryAdder8:
    def __init__(self):
        self._n = 8
        # входы A и B
        self._in_a = []
        self._in_b = []
        self._in_ci = None
        # сумматоры
        self._ba = []
        #  провода которые свяжут выход от сумматоров с выходами 8битного сумматора
        self._wire_out = []
        # провод от выхода для переноса
        self._wire_co = WireOut()

        self._out_s = []
        self._out_co = None

        for i in range(self._n):
            self._out_s.append(None)
            self._in_a.append(None)
            self._in_b.append(None)
            self._ba.append(BinaryAdder())
            self._wire_out.append(WireOut())

        for i in range(self._n-1):
            self._ba[i].set_out(self._wire_out[i].in1, self._ba[i+1].in_ci)

        self._ba[self._n - 1].set_out(self._wire_out[self._n - 1].in1, self._wire_co.in1)

    def _set_none(self):
        # входы A и B
        self._in_a = [None] * self._n
        self._in_b = [None] * self._n
        self._in_ci = None

    def set_out(self, out1, *out2):
        self._out_co = out1
        self._out_s = out2

    def _result(self):

        for i in range(self._n):
            self._ba[i].in_a(self._in_a[i])
            self._ba[i].in_b(self._in_b[i])

        self._ba[0].in_ci(self._in_ci)

        res = [self._wire_co.get_signal()]
        for i in range(self._n):
            res.append(self._wire_out[i].get_signal())

        return res

    def __getattr__(self, attr):
        # attr = "in_a0" or "in_b0" or "in_ci"
        # i = 0, s = a
        # print("__getattr__ run", attr, len(attr), attr[:3])
        if len(attr) > 4 and (attr[:4] == "in_a" \
                              or attr[:4] == "in_b" \
                              or attr == "in_ci"):

            if attr != "in_ci":
                i = int(attr[4:])
                s = attr[3]
            else:
                i = 0
                s = "c"
            def wrap(value):
                return self._in_summary(i, s, value)
            return wrap

    def _in_summary(self, i, s, value):
        if s == "c":

            self._in_ci = value
        elif s == "a":
            self._in_a[i] = value
        else:
            self._in_b[i] = value

        a = True
        for i in self._in_a:
            if i is None:
                a = False
                break
        b = True
        for i in self._in_b:
            if i is None:
                b = False
                break

        if a and b and self._in_ci is not None:
            out_co, *out_s = self._result()

            for i, el in enumerate(out_s):
                self._out_s[i](el)
            self._out_co(out_co)
            self._set_none()

    def in_a(self, a:list) -> None:
        for i in range(self._n):
            getattr(self, "in_a" + str(i))(a[self._n - i - 1])

    def in_b(self, b:list) -> None:
        for i in range(self._n):
            getattr(self, "in_b" + str(i))(b[self._n - i - 1])

class Invertor8:
    def __init__(self):
        self._n = 8
        self._in = []
        self._xor = []
        self._be_or_not_be = None
        self._wire_out = []
        self._out = None
        for i in range(self._n):
            self._wire_out.append(WireOut())
            self._xor.append(Xor())
            self._in.append(None)
            self._xor[i].set_out(self._wire_out[i].in1)



    def _set_none(self):
        self._in = [None] * self._n
        self._be_or_not_be = None


    def set_out(self, out):
        self._out = out

    def _result(self):
        for i in range(self._n):
            self._xor[i].in1(self._be_or_not_be)
            self._xor[i].in2(self._in[i])
        res = []
        for i in range(self._n):
            res.append(self._wire_out[i].get_signal())
        return res

    def __getattr__(self, attr):
        if "in" in attr:
            i = int(attr[2:])

            def wrap(value):
                return self._in_summary(i,  value)
            return wrap

    def _in_summary(self, i, value):
        self._in[i] = value
        a = True
        for i in self._in:
            if i is None:
                a = False
                break

        if a and self._be_or_not_be is not None:

            out = self._result()
            for i, el in enumerate(out):
                self._out[i](el)
            self._set_none()

    def in_a(self, a:list) -> None:
        for i in range(self._n):
            getattr(self, "in" + str(i))(a[self._n - i - 1])

    def in_b(self, value):
        self._be_or_not_be = value
        a = True
        for i in self._in:
            if i is None:
                a = False
                break

        if a:

            out = self._result()

            for i, el in enumerate(out):
                self._out[i](el)
            self._set_none()


class BinMinuserPluser8:
    def __init__(self):
        self._n = 8
        # входы A и B
        self._in_a = []
        self._in_b = []
        self._in_ci = None
        # сумматоры
        self._ba8 = BinaryAdder8()
        self._invertor = Invertor8()
        self._invertor.set_out(self._ba8.in_b)
        #  провода которые свяжут выход от инвертора с0 входами 8битного сумматора
        self._wire_invertor_out = []
        #  провода которые свяжут выход от сумматоров с выходами 8битного сумматора
        self._wire_out = []
        # провод от выхода для переноса
        self._wire_co = WireOut()

        self._fxor = Xor()

        self._fxor.set_out(self._wire_co.in1)
        self._out_s = []
        self._out_co = None


        wire_outsin = []

        wire_outcos = []

        for i in range(self._n):
            self._out_s.append(None)
            self._in_a.append(None)
            self._in_b.append(None)
            self._wire_out.append(WireOut())
            wire_outsin.append(self._wire_out[i].in1)

            self._wire_invertor_out.append(WireOut())

            wire_outcos.append(self._wire_invertor_out[i].in1)
        self._ba8.set_out(self._fxor.in1, *wire_outsin)

        self._invertor.set_out(list(reversed(wire_outcos)))


    def _set_none(self):
        # входы A и B
        self._in_a = [None] * self._n
        self._in_b = [None] * self._n
        self._in_ci = None

    def set_out(self, out1, *out2):
        self._out_co = out1
        self._out_s = out2

    def _result(self):

        self._invertor.in_a(self._in_b)
        self._invertor.in_b(self._in_ci)
        res = []
        for i in range(self._n):
            res.append(self._wire_invertor_out[i].get_signal())
        res = list(reversed(res))

        self._ba8.in_a(list(reversed(self._in_a)))
        self._ba8.in_b(res)
        self._ba8.in_ci(self._in_ci)
        self._fxor.in2(self._in_ci)
        res = [self._wire_co.get_signal()]

        for i in range(self._n):
            res.append(self._wire_out[i].get_signal())

        return res


    def __getattr__(self, attr):
        # attr = "in_a0" or "in_b0" or "in_ci"
        # i = 0, s = a
        # print("__getattr__ run", attr, len(attr), attr[:3])
        if len(attr) > 4 and (attr[:4] == "in_a" \
                              or attr[:4] == "in_b" \
                              or attr == "in_ci"):

            if attr != "in_ci":
                i = int(attr[4:])
                s = attr[3]
            else:
                i = 0
                s = "c"

            def wrap(value):
                return self._in_summary(i, s, value)

            return wrap

    def _in_summary(self, i, s, value):
        if s == "c":
            self._in_ci = value
        elif s == "a":
            self._in_a[i] = value
        else:
            self._in_b[i] = value

        a = True
        for i in self._in_a:
            if i is None:
                a = False
                break

        b = True
        for i in self._in_b:
            if i is None:
                b = False
                break

        if a and b and self._in_ci is not None:
            out_co, *out_s = self._result()

            for i, el in enumerate(out_s):
                self._out_s[i](el)
            self._out_co(out_co)
            self._set_none()

    def in_a(self, a: list) -> None:
        for i in range(self._n):
            getattr(self, "in_a" + str(i))(a[self._n - i - 1])

    def in_b(self, b: list) -> None:
        for i in range(self._n):
            getattr(self, "in_b" + str(i))(b[self._n - i - 1])




