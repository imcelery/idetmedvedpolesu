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



    return s




if __name__ == '__main__':
    print(sort_stack(deque([2, 1, 8, 1, 3, 7])))


