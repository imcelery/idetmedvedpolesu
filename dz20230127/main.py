from typing import Dict, List
from collections import deque

import sys


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

# ПОМЕНЯТЬ ДА ИЗМЕНИТЬ
def dfs(al: Dict[str, List[str]], start: str, finish: str) -> List[str]:
    s = deque()
    s.append(start)
    a = bo(al, s, finish, [start])
    if type(a) == deque:
        return list(a)
    else:
        return "нет такого"


def bfs(al: Dict[str, List[str]], start: str, finish: str) -> List[str]:
    o = deque()
    o.append(start)
    while True:
        a = o.popleft()
        if a == finish:
            break
        else:
            for i in al[start]:
                o.append(i)


def main(filename: str, from_city: str, to_city: str):
    pass

if __name__ == "__main__":
    print(dfs({"a" : ["b", "c"], "b" : ["d"], "c" : ["d"]}, "a", "d"))
    print(bfs({"a": ["b", "c"], "b": ["d"], "c": ["d"]}, "a", "d"))
    # python main.py adjacency_list.txt москва екатеринбург
    filename, from_city, to_city = sys.argv[1], sys.argv[2], sys.argv[3]
    main(filename, from_city, to_city)