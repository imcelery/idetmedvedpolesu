from collections import defaultdict

class Node:
    def __init__(self):
        self.d = defaultdict(Node)
        self.hash = ""
        self.exist = True

    def append(self, path, i=0):
        if i != len(path):
            self.d[path[i]].append(path, i + 1)

    def getHash(self, hashes, name = ""):
        for i in self.d.keys():
            self.hash += self.d[i].getHash(hashes, i)
        if self.hash != "":
            hashes[self.hash].append(self)
        return "(" + name +  self.hash + ")"

    def getList(self, l, path=None):
        if path is None:
            path = []
        for i in self.d.keys():
            if self.d[i].exist:
                l.append(path + [i])
                s = self.d[i].getList(l, path + [i])
                if s is not None:
                    l.append(s)



class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:

        r = Node()
        paths.sort()
        hashes = defaultdict(list)
        for i in paths:
            r.append(i)

        r.getHash(hashes)

        for i in hashes.keys():
            if len(hashes[i]) > 1:
                for j in hashes[i]:
                    j.exist = False
        l = []
        r.getList(l)
        return l