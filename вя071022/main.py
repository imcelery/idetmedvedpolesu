def substring(s: str, substr: str) -> [int]:
    a = []
    for i in range(len(s)):
        if s[i] == substr[0]:
            if s[i: i + len(substr)] == substr:
                a.append(i)
    return a
if __name__ == '__main__':
    print(substring("abcabcabc", "abc"))


