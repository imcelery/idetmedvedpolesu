def substring(s: str, substr: str) -> [int]:
    a = []
    for i in range(len(s)):
        b = 1
        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                b = 0
                break
        if b:
            a.append(i)
    return a
if __name__ == '__main__':
    print(substring("abcabcabc", "abc"))


