import math

if __name__ == "__main__":
    begin_temp = 83.0
    room_temp = 22.0

    dt = 0.1

    max_time = 15

    ro = [83.0, 77.7, 75.1, 73.0, 71.1, 69.4, 67.8, 66.4, 64.7, 63.4, 62.1, 61.1, 59.9, 58.7, 57.8, 56.6]
    predo = []
    minerror = 1000000000

    tr = 0

    for i in range(0, 10000):
        t = 0
        temp = begin_temp
        r = i / 1000000
        o = [temp]

        for j in range(int(max_time / dt)):
            change = -r*(temp - room_temp)

            temp += change
            t += dt
            if (j + 1 )% (1 / dt) == 0:
                o.append(temp)
        error = 0
        for j in range(len(o)):
            error += pow(ro[j] - o[j], 2)

        if error < minerror:
            tr = r
            minerror = error
            predo = o

    print(f"Лучший r равен {tr}")
    print(f"Вот с такими результатами {predo}")
    print(f"И такой ошибкой {minerror}")