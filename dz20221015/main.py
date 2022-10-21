class Digital:
    def __init__(self):
        pass
    # из десятичной в двоичную
    def dec_to_bin(self, number):
        deep = 10000
        # длина приближения если дробь бесконечная
        if number == 0:
            # проверка на ноль
            return 0
        bin = ""
        minus = ""
        if number < 0:
            # проверка на отрицательность
            minus = "-"

        # делим целую часть на 2 и смотрим на остаток
        div, mod = divmod(number//1, 2)
        while div > 0:
            if mod == 1:
                bin += "1"
            elif mod == 0:
                bin += "0"
            else:
                return None
            div, mod = divmod(div, 2)
        if mod == 1:
            bin += "1"

        # переворачиваем чило и добавляем знак минуса если он есть
        bin = minus + bin[::-1]

        #умножаем дробную часть на 2 и смотрим целое
        if type(number) == float:
            drob = number % 1
            bin += "."
            for i in range(deep):
                drob *= 2
                bin += str(int(drob // 1))
                drob = drob % 1
                if drob == 0:
                    break

        return bin



    def bin_to_dec(self, number):

        cel = ""
        drob = ""
        minus = 1
        dec = 0
        # отделяем дробную часть от целой
        a = True
        for i in str(number):
            if i == "-":
                # проверка на отрицательность
                minus = -1
            elif i == ".":
                a = False
            elif a:
                cel += i
            else:
                drob += i

        # переводим целую часть
        razrid = 0
        for i in cel[::-1]:
            if i == "1":
                dec += 2**razrid
            razrid += 1

        # переводим дробную часть
        razrid = 1
        for i in drob:
            if i == "1":
                dec += 1 / (2 ** razrid)
            razrid += 1
        return dec * minus
a = Digital()
print(a.bin_to_dec(.111111))