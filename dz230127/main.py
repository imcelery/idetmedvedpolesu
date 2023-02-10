from typing import Dict, List
from collections import deque



def bo(al: Dict[str, List[str]], s: deque, fin: str, alreafyposidely: []):
    if s[len(s) - 1] == fin:
        return s
    n = al[s[len(s) - 1]]
    for i in n:
        if i not in alreafyposidely:
            ns = s.copy()
            ns.append(i)
            alreafyposidely.append(i)
            a = bo(al, ns, fin, alreafyposidely)
            if type(a) == deque:
                return a
            else:
                alreafyposidely.extend(a)
    return alreafyposidely
    #возращаем очередь если нашли путь а если нет возращем список пройденных вершин


def dfs(al: Dict[str, List[str]], start: str, finish: str) -> List[str]:
    s = deque()
    s.append(start)
    #вызываем рекурсию
    a = bo(al, s, finish, [start])
    #если вернулась очередь то ответ есть
    if type(a) == deque:
        return list(a)
    else:
        return "нет такого"


def bfs(al: Dict[str, List[str]], start: str, finish: str) -> List[str]:


    o = deque()
    o.append(start)
    #ловарь путей ко всем пройденным вершинам чтобы восстановить обратный путь
    puti = {}
    #чтобы знать когда из цикла выходить
    f = False

    while len(o) != 0:
        a = o.popleft()
        for i in al[a]:
            if i not in puti.keys():
                o.append(i)
                puti.update({i : a})
                if i == finish:
                    #готча
                    f = True
                    break


        if(f):
            break
    #если нашли
    if f:
        o = [finish]

        n = finish
        while True:
            n = puti[n]
            o.append(n)
            if n == start:
                break
        return list(reversed(o))
    else:
        return 'нет такого'



def main(filename: str, from_city: str, to_city: str):
    with open(filename, "r") as f:
        al = eval(f.readline())
    print(dfs(al, from_city,to_city))
    print(bfs(al, from_city,to_city))

if __name__ == "__main__":
    # python main.py adjacency_list.txt москва екатеринбург
    #датасет фиговый екб нету
    main("list.txt", "Москва", "Тула")