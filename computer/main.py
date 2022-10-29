from ventils import And, Or, Not, Provod, Lamp


if __name__ == '__main__':
    and1 = And()
    or1 = Or()
    lamp1 = Lamp()


    provod1 = Provod()
    provod2 = Provod()

    provod1.set_out(or1.in1)
    provod2.set_out(or1.in2)

    or1.set_out(lamp1.in1)

    provod1.set_signal(0)
    provod2.set_signal(0)


