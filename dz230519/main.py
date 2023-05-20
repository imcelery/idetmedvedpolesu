class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None

    root = Node()
    n = len(nums)
    q = [[0, n, root]]
    while q:
        b, f, n = q.pop()
        i = (b + f) // 2
        n.val = nums[i]

        if b < i:
            d = Node()
            n.left = d
            q.append([i, n, d])

        if f > i:
            d = Node()
            n.right = d
            q.append([n, f, d])

    return root

def searchBST(root, val):
    while root.val != val:
        if root.val > val:
            if root.left:
                root = root.left
            else:
                return None
        else:
            if root.right:
                root = root.right
            else:
                return None
    return root

from collections import deque

def bstToGst(root):
    out = root
    nextdoors = deque()
    while root.right:
        nextdoors.appendleft([root, 1])
        root = root.right
    s = root.val

    w = set([s])
    while nextdoors:
        n, y = nextdoors.popleft()
        # print()
        # print(n.val)
        # print(s)
        if y:

            s += n.val
            n.val = s
            w.add(n.val)
            if n.left:
                if n.left.val not in w:
                    # print(n.left.val)
                    nextdoors.appendleft([n.left, 0])


            r = n.right
            while r:
                if r.val not in w:
                    nextdoors.appendleft([r, 1])
                    r = r.right
                else:
                    break
        else:
            nextdoors.appendleft([n, 1])
            r = n.right
            while r:
                if r.val not in w:
                    nextdoors.appendleft([r, 1])
                    r = r.right
                else:
                    break

    return out


def bstToGst2(root):
    value = 0
    def do(root, value):
        if root is None:
            return None

        if root.right:
            value = do(root.right, value)
        value += root.val
        root.val = value
        if root.left:
            value = do(root.left, value)
        return value
    do(root, value)
    return root

def insertIntoBST(root, val):
    if not root:
        return Node(val)
    n = root
    while True:
        if n.val > val:
            if n.left:
                n = n.left
            else:
                n.left = Node(val)
                break
        else:
            if n.right:
                n = n.right
            else:
                n.right = Node(val)
                break
    return root



n = Node(4, Node(1, Node(0), Node(2, right=Node(3))), Node(6, Node(5), Node(7, right=Node(8))))
nn = insertIntoBST(n, 9)
nnn = bstToGst2(n)

print(nnn.left.val)