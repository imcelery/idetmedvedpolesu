
a = []
with open("27-B.txt", "r") as f:
    k = int(f.readline())
    n = int(f.readline())
    for i in range(n):
        a.append(int(f.readline()))

# maxses = [[a[0], 0], [a[1], 1], [a[2], 2]]
# mlen = 2
ms = 0
# l = 0
# r = 2
# for i in range(3, n):
#     r += 1
#     while maxses[mlen][0] < a[r]:
#         maxses.append([a[r], r])
#     if a[r - 1] < a[r]:
#         while r - l > 3 * k:
#             l += 1
#             ms = max(a[l] + a[r] + max(a[l + 1: r - 1]), ms)
# print(ms)
ms = 0
for i in range(n):
    for j in range(i + 3 * k, n):
            ms = max(ms, a[i] + a[j] + max(a[i + 1: j - 1]))
    print(ms)
print(ms)
