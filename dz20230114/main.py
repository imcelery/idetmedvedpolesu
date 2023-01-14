import numpy as np


class ArrayList:
    """
    """

    def __init__(self):
        self.max_len = 8  # сколько мы выделли в памяти
        self.memory_addr = np.zeros((self.max_len,), dtype=np.uint16)  # [0] * self.max_len
        self.memory_obj = []  # не чистите никогда за время работы
        self.len = 0  # какой объем массива заполнен (по сути длина массива)

    def len(self):
        """
        """
        return self.len

    def seti(self, i, value):
        # проверка на вместимость
        if i >= self.len:
            raise IndexError()
        # устанавливаем i элемент
        self.memory_obj.append(value)
        self.memory_addr[i] = len(self.memory_obj) - 1

    def geti(self, i):
        # проверка на вместимость
        if i >= self.len:
            raise IndexError()
        # получаем i элемент
        return self.memory_obj[self.memory_addr[i]]

    def append(self, value):
        self.len += 1
        # если места мало копируем массив в более просторное место
        if self.len >= self.max_len // 2:
            # копирование
            self.max_len *= 2
            self.memory_addr2 = np.zeros((self.max_len,), dtype=np.uint16)
            self.memory_addr2[:self.max_len // 4] = self.memory_addr[:self.max_len // 4]
            self.memory_addr = self.memory_addr2
        self.seti(self.len - 1, value)


class Node:
    def __init__(self, link_value, link_next, link_prev):
        # ссылка на свое значение
        self.link_value = link_value
        # ссылка на свое значение
        self.link_next = link_next
        self.link_prev = link_prev


class DoubleLinkedList:
    def __init__(self):
        self.memory_addr = []  # [0] * self.max_len
        self.memory_obj = []  # не чистите никогда за время работы
        self.len = 0  # какой объем массива заполнен (по сути длина массива)
        self.start = 0
        self.finish = 0

    def append(self, value):
        self.len += 1
        self.memory_obj.append(value)
        # if self.start is None:
        #     self.start = 0
        # if self.finish is None:
        #     self.finish = 0

        if self.len == 1:
            self.start = len(self.memory_addr)
            self.finish = len(self.memory_addr)
        # новый нод
        node = Node(len(self.memory_obj) - 1, self.start, self.finish)
        self.memory_addr.append(node)

        # если в списке есть чтото еще
        if self.len > 1:
            #ставим ему новый нод как ссылку на следущий
            self.memory_addr[self.finish].link_next = len(self.memory_addr) - 1
        # обновляем финиш
        self.finish = len(self.memory_addr) - 1
        # зацикливаем массив
        self.memory_addr[0].link_prev = self.finish

    def remove(self, link_el):
        if self.len > 1:
            # переустанавливеам ссылки на следущий и предыдущий у следущего и предыдущего
            node_prev = self.memory_addr[link_el].link_prev
            node_next = self.memory_addr[link_el].link_next

            self.memory_addr[node_prev].link_next = node_next
            self.memory_addr[node_next].link_prev = node_prev
            # переустанавливаем старт и финиш если надо
            if link_el == self.start:
                self.start = node_next
            if link_el == self.finish:
                self.finish = node_prev
        else:
            self.start = 0
            self.finish = 0

        self.len -= 1

    def insert(self, link_el, value):
        if self.len > 0:
            # переустанавливеам ссылки на следущий и предыдущий у следущего и предыдущего
            node_next = self.memory_addr[link_el].link_next
            node_prev = link_el
            self.memory_obj.append(value)
            node = Node(len(self.memory_obj) - 1, node_next, node_prev)
            self.memory_addr.append(node)
            self.memory_addr[link_el].link_next = len(self.memory_addr) - 1
            # переустанавливаем  финиш если надо
            if link_el == self.finish:
                self.finish = len(self.memory_addr) - 1
        else:
            raise IndexError()

        self.len += 1

    def search(self, index):
        link_now = self.start
        #идем по следущим ссылкам массива пока не найдем нужный индекс
        while link_now != self.finish and index > 0:
            link_now = self.memory_addr[link_now].link_next
            index -= 1
        if index == 0:

            return link_now
        raise IndexError()

    def show(self):
        s = ""
        i = self.start
        while True:
            # идем по следущим ссылкам массива пока не найдем финиш
            s += str(self.memory_obj[self.memory_addr[i].link_value]) + " "
            i = self.memory_addr[i].link_next
            if i == self.finish:
                s += str(self.memory_obj[self.memory_addr[i].link_value]) + " "
                return s.strip()

    def get(self, index):
        return self.memory_obj[self.search(index).link_value]

    def getin(self, index):
        return self.memory_obj[self.memory_addr[index].link_value]

class Stack:
    # спомощью дабллинкера делаем более простую структуру
    def __init__(self):
        self._array = DoubleLinkedList()

    def push(self, value):
        self._array.append(value)

    def pop(self):
        self._array.remove(self._array.finish)

    def top(self):
        return self._array.getin(self._array.finish)

    def len(self):
        return self._array.len

    def show(self):
        return self._array.show()


class Queue:
    # тоже самое а что тут еще писать
    def __init__(self):
        self._array = DoubleLinkedList()

    def push(self, value):
        self._array.append(value)

    def pop(self):
        self._array.remove(self._array.start)

    def top(self):
        return self._array.getin(self._array.start)

    def len(self):
        return self._array.len

    def show(self):
        return self._array.show()