from ventils import And, Or, Not, WireIn, Lamp, Xor
from adders import HalfAdder, BinaryAdder8
from memory import Trigger, MemoryBit, Ram8
if __name__ == '__main__':

    lamp1 = Lamp("lamp1")


    wire1 = WireIn()
    wire2 = WireIn()

    t = Ram8()

    wire1.set_out(t.in_b)
    wire2.set_out(t.in_c)


    t.set_out(lamp1.in1)


    wire1.set_signal(1)
    wire2.set_signal(1)
    t.in_a([0,0,0])


    wire1.set_signal(0)
    wire2.set_signal(1)
    t.in_a([0, 0, 0])


    wire1.set_signal(1)
    wire2.set_signal(1)
    t.in_a([0, 1, 1])


    wire1.set_signal(0)
    wire2.set_signal(0)
    t.in_a([0, 1, 1])

    wire1.set_signal(0)
    wire2.set_signal(1)
    t.in_a([0, 0, 0])








