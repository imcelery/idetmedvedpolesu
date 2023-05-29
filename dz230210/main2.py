
if __name__ == "__main__":
    room_temp = 22.0

    dt = 0.1

    r = 0.004185

    t = 0
    temp = 85.0
    while temp > 75.0:
        change = -r * (temp - room_temp)
        temp += change
        t += dt
    print(f"Если льем молоко сначало то ждем {t} минут")

    t = 0
    temp = 90.0
    while temp > 80.0:
        change = -r * (temp - room_temp)
        temp += change
        t += dt
    print(f"Если льем молоко потом то ждем {t} минут")


    relax = 0.37
    t = 0
    temp = 90.0
    differ = temp - room_temp
    while (temp - room_temp) > differ * relax:
        change = -r * (temp - room_temp)
        temp += change
        t += dt
    print(f"Время релаксации = {t} минут")
    print()
    rs = [i / 1000 for i in range(1, 1000)]
    ts = []
    m = []
    for i in range(len(rs)):
        t = 0
        temp = 90.0
        differ = temp - room_temp
        while (temp - room_temp) > differ * relax:
            change = -rs[i] * (temp - room_temp)
            temp += change
            t += dt
        ts.append(t)
        m.append(t * rs[i])
    print(f"коэфиценты :  {rs}")
    print(f"дают такое время релаксации : {ts}")

    print(f" а это массив перемноженных значений r b t : {m}")
    print("они все примерно равны 0.1, f это значит что формулой описывающей зависимость t от r будет t = 0.1/r")