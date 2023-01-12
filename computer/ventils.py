import numpy as np


class WireIn:
    def __init__(self):
        self._out = None

    def set_out(self, out):
        self._out = out

    def set_signal(self, value):
        self._out(value)


class WireOut:
    def __init__(self):
        self._in1 = None

    def in1(self, value):
        self._in1 = value

    def get_signal(self):
        return self._in1


class MultiplyWire:
    def __init__(self):
        self._outs = None

    def set_out(self, outs:list):
        self._outs = outs


    def in1(self, value):
        for i in self._outs:
            i(value)

class Lamp:
    def __init__(self, label):
        self._label = label

    def in1(self, value):
        print(self._label, value)


class And:
    """
      | 0 1
    --------
    0 | 0 0
    1 | 0 1
    """

    def __init__(self):
        self._out = None
        self._in1 = None
        self._in2 = None

    def _result(self):

        return int(self._in1 and self._in2)

    def _set_none(self):
        self._in1 = None
        self._in2 = None


    def in1(self, value):
        self._in1 = value
        if self._in2 is not None:
            self._out(self._result())
            self._set_none()

    def in2(self, value):
        self._in2 = value
        if self._in1 is not None:
            self._out(self._result())

            self._set_none()

    def set_out(self, out):

        self._out = out


class Or(And):
    """
      | 0 1
    --------
    0 | 0 1
    1 | 1 1
    """

    def _result(self):
        return int(self._in1 or self._in2)


class Not:
    """
      | 0 1
    --------
      | 1 0
    """

    def __init__(self):
        self._out = None
        self._in1 = None

    def _result(self):
        return int(not (self._in1))

    def _set_none(self):
        self._in1 = None

    def in1(self, value):
        self._in1 = value
        self._out(self._result())
        self._set_none()

    def set_out(self, out):
        self._out = out


class AndNot(And):
    """
      | 0 1
    --------
    0 | 1 1
    1 | 1 0
    """

    def _result(self):
        return int(not (self._in1 and self._in2))


class OrNot(And):
    """
      | 0 1
    --------
    0 | 1 0
    1 | 0 0
    """

    def _result(self):
        return int(not (self._in1 or self._in2))


class Xor(And):
    """
      | 0 1
    --------
    0 | 0 1
    1 | 1 0
    """

    def __init__(self):
        super().__init__()  # in1, in2, out

        self._or = Or()
        self._and_not = AndNot()
        self._and = And()
        self._wire = WireOut()

        self._or.set_out(self._and.in1)
        self._and_not.set_out(self._and.in2)
        self._and.set_out(self._wire.in1)

    def _result(self):
        self._or.in1(self._in1)
        self._and_not.in1(self._in1)
        self._or.in2(self._in2)
        self._and_not.in2(self._in2)
        return self._wire.get_signal()


class Or8:
    def __init__(self):
        self._n = 8
        self._in = []
        self._wire_out = WireOut()
        self._out = None
        for i in range(self._n):
            self._in.append(None)

    def _set_none(self):
        self._in = [None] * self._n


    def set_out(self, out):
        self._out = out

    def _result(self):

        b = int(np.any(self._in) == 1)
        self._set_none()
        return b

    def __getattr__(self, attr):
        if "in" in attr:
            i = int(attr[2:])

            def wrap(value):
                return self._in_summary(i,  value)
            return wrap

    def _in_summary(self, i, value):
        self._in[i] = value
        b = True
        for i in self._in:
            if i is None:
                b = False
                break
        if b:

            self._out(self._result())
            self._set_none()

    def in_a(self, a:list) -> None:

        for i in range(self._n):
            getattr(self, "in" + str(i))(a[self._n - i - 1])

class And4:
    def __init__(self):
        self._out = None
        self._in = []

    def _result(self):
        return int(self._in[0] and self._in[1] and self._in[2] and self._in[3])

    def _set_none(self):
        self._in = []


    def ina(self, value):
        if value is not None:
            self._in.append(value)

            if len(self._in) == 4:
                self._out(self._result())
                self._set_none()

    def set_out(self, out):
        self._out = out




