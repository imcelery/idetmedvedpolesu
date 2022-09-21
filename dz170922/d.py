def d(n, a, b):
    a = a + b
    a = list(set(a))
    if len(a) == n:
        return "I become the guy."
    return "Oh, my keyboard!"


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    print(d(n, a[1:], b[1:]))