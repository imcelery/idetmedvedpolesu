class Digital:
    def __init__(self):
        pass
    # из десятичной в двоичную
    def dec_to_bin(self, number):
        #проверка на ноль
        if number == 0:
            return "0"
        # делим целую часть на 2 и смотрим на остаток
        bin = ""
        div, mod = divmod(number // 1, 2)
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

        # переворачиваем чило
        return str(bin[::-1])


    def dec_to_bin_float(self, number):
        # длина приближения если дробь бесконечная
        deep = 10000

        bin = ""

        #умножаем дробную часть на 2 и смотрим целое
        drob = number % 1
        bin += "."
        for i in range(deep):
            drob *= 2
            bin += str(int(drob // 1))
            drob = drob % 1
            if drob == 0:
                break

        return self.dec_to_bin(number//1) + bin



    def bin_to_dec(self, number):
        dec = 0
        # переводим целую часть
        razrid = 0
        for i in number[::-1]:
            if i == "1":
                dec += 2**razrid
            razrid += 1
        return dec


    def bin_to_dec_float(self, number):

        cel = ""
        drob = ""
        dec = 0

        # отделяем дробную часть от целой
        a = True
        for i in str(number):
            if i == ".":
                a = False
            elif a:
                cel += i
            else:
                drob += i

        # переводим дробную часть
        razrid = 1
        for i in drob:
            if i == "1":
                dec += 1 / (2 ** razrid)
            razrid += 1
        return dec + self.bin_to_dec(cel)
