class Provod:
    def __init__(self):
        self.out = None

    def set_out(self, in1):
        self.out = in1

    def set_signal(self, value):
        self.out(value)


class Lamp:
    def in1(self, value):
        print(value)


class And:
    '''
      / 0 1
    -------
    0 / 0 0
    1 / 0 1
    '''
    def __init__(self):
        self._out = None
        self._in1 = None
        self._in2 = None

    def set_out(self, in1):
        self._out = in1


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



class Or(And):

    '''
      / 0 1
    -------
    0 / 0 1
    1 / 1 1
    '''

    def _result(self):
        return int(self._in1 or self._in2)


class Not:
    '''
          / 0 1
        -------
        0 / 1 1
        1 / 0 0
        '''
    pass

