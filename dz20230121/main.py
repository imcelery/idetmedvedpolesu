import pandas as pd

def main():
    roads = pd.read_csv("roads.csv", encoding="cp1251", sep=";")
    roads = roads["Наименование автомобильных дорог"].str.strip().str.replace("\xa0" , " ").str.replace(" к ", " - ").str.replace("г. ", "", regex=True)\
    .str.replace(".* от", "", regex=True).str.replace('".*"', '', regex=True).str.strip().str.split(" - ").tolist()
    #adjience_matrix(roads, "matrix.csv")
    list_ribbles(roads, "ribbles.txt")
    #adjience_list(roads, "list.txt")

def list_ribbles(roads, path):
    ribbles = []
    for i in roads:
        for j in (range(len(i) - 1)):
            a = (i[j], i[j + 1])
            if a not in ribbles and reversed(a) not in ribbles:
                ribbles.append(a)
    with open(path, "w") as f:
        f.write(str(ribbles))

def adjience_list(roads, path):
    adjacency = {}
    for i in roads:
        for j in (range(len(i) - 1)):
            if i[j] not in adjacency.keys():
                adjacency.update({i[j]: [i[j+1]]})
            elif i[j+1] not in adjacency[i[j]]:
                adjacency[i[j]].append(i[j + 1])

            if i[j + 1] not in adjacency.keys():
                adjacency.update({i[j + 1]: [i[j]]})
            elif i[j] not in adjacency[i[j + 1]]:
                adjacency[i[j + 1]].append(i[j])
    with open(path, "w") as f:
        f.write(str(adjacency))

def adjience_matrix(roads, path):
    points = []
    for i in roads:
        for j in i:
            if j not in points:
                points.append(j)
    l = len(points)
    pointsdict =  {k:v for k, v in zip(points, list(range(l)))}

    matrix = [[0 for _ in range(l)] for __ in range(l)]
    for i in roads:
        for j in (range(len(i) - 1)):
            matrix[pointsdict.get(i[j])][pointsdict.get(i[j + 1])] = 1
            matrix[pointsdict.get(i[j + 1])][pointsdict.get(i[j])] = 1


    data = pd.DataFrame(matrix, columns=points, index = points)
    data.to_csv(path)

if __name__ == '__main__':
    main()