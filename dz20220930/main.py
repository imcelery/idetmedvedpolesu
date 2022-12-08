import requests



def is_sawed(url, pages):
    return url in pages


def load_html(url):
    return requests.get(url).text


def save_html(txt, name):
    with open(name, "w",  encoding="utf-8") as f:
        f.write(txt)


def findall(r, url, d=[], v=[], start=0):
    start_i = r.find('<a ', start)
    if start_i != -1:
        c = r.find('>', start_i)
        a = r.find('href="', start_i, c)
        if a != -1:
            a += 6
            b = r.find('"', a) - 1
            if -1 == r.find(url, a, b) and -1 != r.find("https://", a, b):
                if r[a: b] not in d:
                    d.append(r[a: b])
            else:
                if r[a: b] not in v:
                    v.append([r[a: b], a, b])
        return findall(r, url, d, v, start=c)
    return d, v


def rename(url, r, v):
    a = []
    a.append(r[v[0][1] - 1])
    for i in range(0, len(v)):
        urln = url + r[v[i][1]: v[i][2]]
        a.append(urln)
        if i == len(v):
            a.append(r[v[i][2]: v[i + 1][1]])
        else:
            a.append(r[v[i][2]: len(r)])
    return "".join(a)

def renameallandsafe(main_url, url = None, pages = [], inpages = []):
    if url == None:
        url = main_url
    if not is_sawed(url, pages):
        r = load_html(url)
        d, v = findall(r, url)

        r = rename(url, r, v)

        name = url[8:].replace("/", "_")
        save_html(r, f"site/{name}.txt")
        pages.append(url)

        for i in v:
            if i[0] not in inpages:

                inpages.append(i[0])
                m, n = renameallandsafe(main_url, f"{main_url}{i[0]}", pages, inpages)
                for j in m:
                    if j not in pages:
                        pages.append(m)

                for j in n:
                    if j not in inpages:
                        pages.append(n)

    return pages, inpages






if __name__ == "__main__":
    url = "https://www.gimp.org"
    renameallandsafe(url)