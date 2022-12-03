from ventils import WireIn, Lamp
from adders import BinaryAdder, NAdder

if __name__ == '__main__':

    adder = NAdder(2)


    l = []
    for i in range(2 + 1):
        l.append(Lamp(i))

    o = []
    for i in l:
        o.append(i.in1)

    adder.set_out(o)

    adder.in_a([1, 1])
    adder.in_b([0, 0])


