
def lenn(n):
    m = [1, 1]
    l = 2

    def get(i):
        if i < len(m):
            return m[i]
        else:
            return get(i-1) + get(i-2)



    while m[l - 1] < n:
        l += 1
        m.append(get(l - 1))


    if m[l - 1] == n:
        return l
    else:
        return -1

if __name__ == "__main__":
    n = int(input())

    print(lenn(n))
