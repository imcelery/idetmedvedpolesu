from ventils import Xor, And, WireOut, Or


class HalfAdder(And):
    def __init__(self):

        self._in1 = None
        self._in2 = None
        self._out1 = None
        self._out2 = None

        self._xor = Xor()
        self._and = And()
        self._wire1 = WireOut()
        self._wire2 = WireOut()

        self._xor.set_out(self._wire1.in1)
        self._and.set_out(self._wire2.in1)

    def _result(self):
        self._xor.in1(self._in1)
        self._and.in1(self._in1)
        self._xor.in2(self._in2)
        self._and.in2(self._in2)
        return self._wire1.get_signal(), self._wire2.get_signal()

    def in1(self, value):
        self._in1 = value
        if self._in2 is not None:
            out1, out2 = self._result()
            self._out1(out1)
            self._out2(out2)
            self._set_none()

    def in2(self, value):
        self._in2 = value
        if self._in1 is not None:
            out1, out2 = self._result()

            self._out1(out1)
            self._out2(out2)
            self._set_none()

    def set_out(self, out1, out2):
        self._out1 = out1
        self._out2 = out2



class BinaryAdder:
    def __init__(self):
        self._in1 = None
        self._in2 = None
        self._in3 = None
        self._out1 = None
        self._out2 = None

        self._ha1 = HalfAdder()
        self._ha2 = HalfAdder()
        self._or = Or()
        self._wire1 = WireOut()
        self._wire2 = WireOut()


        self._ha1.set_out(self._wire1.in1, self._or.in1)

        self._ha2.set_out(self._ha1.in2, self._or.in2)
        self._or.set_out(self._wire2.in1)


    def _result(self):
        self._ha1.in1(self._in1)
        self._ha2.in1(self._in2)
        self._ha2.in2(self._in3)
        return self._wire1.get_signal(), self._wire2.get_signal()

    def in1(self, value):
        self._in1 = value
        if self._in2 is not None and self._in3 is not None:
            out1, out2 = self._result()
            self._out1(out1)
            self._out2(out2)
            self._set_none()

    def in2(self, value):
        self._in2 = value
        if self._in1 is not None and self._in3 is not None:
            out1, out2 = self._result()
            self._out1(out1)
            self._out2(out2)
            self._set_none()

    def in3(self, value):
        self._in3 = value
        if self._in2 is not None and self._in1 is not None:
            out1, out2 = self._result()
            self._out1(out1)
            self._out2(out2)
            self._set_none()

    def set_out(self, out1, out2):
        self._out1 = out1
        self._out2 = out2

    def _set_none(self):
        self._in1 = None
        self._in2 = None
        self._in3 = None


class NAdder:
    def __init__(self, n):
        self._n = n
        self._ina = []
        self._inb = []

        for i in range(n):
            self._ina.append(None)

        for i in range(n):
            self._inb.append(None)

        self._wires = []
        for i in range(n + 1):
            self._wires.append(WireOut)

        self._outs = []
        for i in range(n + 1):
            self._outs.append(None)

        self._bas = []
        for i in range(n):
            self._bas.append(BinaryAdder())

        self._bas[0].in1(0)

        for i in range(n - 1):
            self._bas[i].set_out(self._wires[i].in1, self._bas[i + 1].in1)

        self._bas[n - 1].set_out(self._wires[n - 1].in1, self._wires[n].in1)


    def _result(self):
        for i in range(len(self._ina)):
            self._bas[i].in2(self._ina[i])
            self._bas[i].in3(self._inb[i])

        o = []
        for i in self._wires:
            o.append(i.get_signal())
        return o

    def in_a(self, a):

        self._ina = a
        bo = True
        for i in self._inb:

            if i is None:
                bo = False
        if bo:
            all_out = self._result()

            for i in range(len(all_out)):
                self._outs[i](all_out[i])

            self._set_none()

    def in_b(self, b):

        self._inb = b
        bo = True
        for i in self._ina:

            if i is None:
                bo = False
        if bo:
            all_out = self._result()

            for i in range(len(all_out)):
                self._outs[i](all_out[i])

            self._set_none()

    def set_out(self, l):
        self._outs = l

    def _set_none(self):
        for i in self._ina:
            i = None

        for i in self._inb:
            i = None

