s = "7" * 47
while "2222" in s or "7777" in s:
    s = s.replace("2222", "77")
    s = s.replace("7777", "22")
print(s)