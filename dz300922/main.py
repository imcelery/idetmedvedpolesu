import requests
url = "https://www.gimp.org/"
r = requests.get(url).text
ssilki = []


def is_sawed(url):
    return url in ssilki


def load_html(url):
    return requests.get(url).text


def save_html(txt, name):
    with open(name, "w",  encoding="utf-8") as f:
        f.write(txt)


save_html(r, "сайт.html")

def findall(r, url, d = [], v = [], start=0,):
    start_i = r.find('<a ', start)
    if start_i != -1:
        c = r.find('>', start_i)
        a = r.find('href="', start_i, c)
        if a != -1:
                a += 6
                b = r.find('"', a)
                if -1 == r.find(url, a, b) and -1 != r.find("https://", a, b):
                    if r[a: b] not in d:
                        d.append(r[a: b])
                else:
                    if r[a: b] not in v:
                        v.append(r[a: b])
        return findall(r, url, d, v, a)
    return d, v

print(findall(r, url))