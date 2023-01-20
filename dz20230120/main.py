import math
from collections import deque


def first_unique_number(l: list) -> list:
    minel = 0
    maxel = 0
    for i in l:
        if minel > i:
            minel = i

        if maxel < i:
            maxel = i
    b = [0 for _ in range(0, maxel - minel + 1)]

    for i in l:
        b[i - minel] += 1

    o = []
    for i in l:
        if b[i - minel] == 1:
            o.append(i)
    return o

def sort_stack(s: deque)-> None:
    s2 = deque()
    s3 = deque()


    # сортируем первые два элемента
    s2.append(s.pop())
    s3.append(s.pop())

    if s2[len(s2) - 1] < s3[len(s3) - 1]:
        s.append(s2.pop())
        s.append(s3.pop())
    else:
        s.append(s3.pop())
        s.append(s2.pop())


    for i in range(len(s) - 2):
        for j in range(i + 2):
            s2.append(s.pop())
        kos = 0
        for j in range(i + 2):


            if s[len(s) - 1] > s2[len(s2) - 1]:
                s3.append(s2.pop())

            else:
                s2.append(s.pop())
                kos = 1
                break
        if not kos:
            s2.append(s.pop())

        for j in range(len(s3)):
            s2.append(s3.pop())

        for j in range(len(s2)):
            s.append(s2.pop())

def generate_binary_number(n: int) -> list[str]:
    s = [deque() for _ in range(math.ceil(math.log2(n)))]
    b = 0
    for i in range(len(s)):
        s[i].append(b)
    b = int(not b)
    for _ in range(n):
        s[0].append(b)
        if b == 0:
            bo = 1
        else:
            bo = 0
        for i in range(1, len(s)):
            if bo:
                if s[i][len(s[i]) - 1] == 1:
                    bo = 1
                else:
                    bo = 0
                s[i].append(int(not s[i][len(s[i]) - 1]))
            else:

                s[i].append(s[i][len(s[i]) - 1])
        b = int(not b)
    o = []
    for _ in range(n):
        om = ""
        for i in range(len(s)- 1, -1, -1):
            om += str(s[i].popleft())
        o.append(om)
    return o


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.previous: Node = None

    def __repr__(self):
        return "Node: " + str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        self._len = 0
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            self.tail = node
            self._len += 1
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                self.tail = node
                self._len += 1

    def __len__(self):
        return self._len

    def __add__(self, b):
        self.tail.next = b.head
        self.tail = b.tail
        return self

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, key):
        if key > len(self):
            raise Exception("некоректный индекс")
        node = self.head
        i = 0
        while key > i:
            node = node.next
            i += 1
        return node.data

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        self.tail.next = node
        self.tail = node

    def search(self, target_node_data):
        for node in self:
            if node.data == target_node_data:
                return node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        node = self.search(target_node_data)
        new_node.next = node.next
        node.next = new_node
        if self.tail == node:
            self.tail = new_node
        return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                if previous_node.next is None:
                    self.tail = previous_node
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

def merge_sort(l):
    if len(l) > 1:
        a = merge_sort(LinkedList([l[i] for i in range(len(l) // 2)]))
        b = merge_sort(LinkedList([l[i + len(l) // 2] for i in range(len(l) - len(l) // 2)]))
        ca = 0
        cb = 0
        o = LinkedList()
        while ca < len(a) and cb < len(b):
            if a[ca] > b[cb]:
                o.add_last(Node(b[cb]))
                cb += 1
            else:
                o.add_last(Node(a[ca]))
                ca += 1
        if ca + 1 == len(a):
            for i in range(cb, len(b)):
                o.add_last(Node(b[i]))
        else:
            for i in range(ca, len(a)):
                o.add_last(Node(a[i]))
    else:
        return l


def del_dublicate_linked_list(l: LinkedList) -> None:
    pass


if __name__ == '__main__':
    print(merge_sort(LinkedList([2,3,7,2,3])))


