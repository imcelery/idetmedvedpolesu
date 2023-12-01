import json

d = {"1" : [], "2" : [], "3" : [], "4" : [], "5" : [], "6" : [], "7" : [], "8" : [], "9" : [], "10" : [], "11" : [], "12" : [], "13" : [], "14" : [], "15" : [], "16" : [], "17" : [], "18" : [], "19" : [], "20" : [], "21" : [], "22" : [], "23" : [], "24" : []}
a = []
with open("russian_nouns.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        a.append(i)
with open("dobavka.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        a.append(i)
a = sorted(a)
for i in a:
    d[str(len(i))].append(str(i))

for i in d.keys():
    print(i + " " + str(len(d[i])))

with open("words.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False)