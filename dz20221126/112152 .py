# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def f(a, b):
    c = (b - a) / 8
    l = ""
    for i in range(1, 6):
        l += str((a + c * i)) + " "
    return l



if __name__ == '__main__':
    inp = input().split()
    a, b = float(inp[0]), float(inp[1])
    print(f(a, b))


