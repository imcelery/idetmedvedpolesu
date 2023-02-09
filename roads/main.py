
import requests
import math
import numpy as np
import mapnik

def parse(site):
    text = requests.get(site).text
    towns = {}
    n = text.find("</h2>")
    f = text[n:].find("<h2>") + n
    text = text[n:f]

    a = text.find("coordinates-items-left")
    while a != -1:
        a = a + 24
        f = text[a:].find("<") + a
        nk = text[f:].find("coordinates-items-right") + 25 + f
        nf = text[nk:].find("<") + nk


        towns.update({text[a:f]: list(map((lambda x : float(x)),reversed(text[nk:nf].split(", "))))})

        a = text[nf:].find("coordinates-items-left")
        if a == -1:
            break
        a += nf
    return towns

def graf(file):
    chords = parse("https://time-in.ru/coordinates/russia")

    with open(file, "r", encoding='utf-8') as f:
        ribbles = eval(f.readline())

    vert = []
    chribbles = []
    for i in ribbles:
        if i[0] in chords.keys() and i[1] in chords.keys():
            if i[0] not in vert:
                x, y = chords[i[0]]
                vert.append((x, y))

            if i[1] not in vert:
                x, y = chords[i[1]]
                vert.append((x, y))
            chribbles.append((chords[i[0]], chords[i[1]]))


    return vert, chribbles

if __name__ == "__main__":
    m = mapnik.Map(1800, 700)
    m.background = mapnik.Color('steelblue')


    polygons = mapnik.PolygonSymbolizer()
    polygons.fill = mapnik.Color('lightgreen')

    rules = mapnik.Rule()
    rules.symbols.append(polygons)

    style = mapnik.Style()
    style.rules.append(rules)
    m.append_style('Russia', style)

    layer = mapnik.Layer('world')
    layer.datasource = mapnik.Shapefile(file="data/RUS_adm0.shp")
    layer.styles.append('Russia')
    m.layers.append(layer)

    s = mapnik.Style()  # style object to hold rules
    r = mapnik.Rule()  # rule object to hold symbolizers
    point_sym = mapnik.PointSymbolizer()
    r.symbols.append(point_sym)  # add the symbolizer to the rule object

    l = mapnik.LineSymbolizer()
    r.symbols.append( l)  # add the symbolizer to the rule object
    s.rules.append(r)
    m.append_style('towns', s)

    ds = mapnik.MemoryDatasource()
    ctx = mapnik.Context()
    vert, chriddles = graf("r.txt")

    for i in vert:
        geom = mapnik.Geometry.from_wkt(f"POINT({i[0]} {i[1]})")
        f = mapnik.Feature(ctx, 1)
        f.geometry = geom
        ds.add_feature(f)

    for i in chriddles:
        geom = mapnik.Geometry.from_wkt(f"LINESTRING({i[0][0]} {i[0][1]}, {i[1][0]} {i[1][1]})")
        f = mapnik.Feature(ctx, 1)
        f.geometry = geom
        ds.add_feature(f)

    layer = mapnik.Layer('memory')
    layer.datasource = ds
    layer.styles.append('towns')

    m.layers.append(layer)

    m.zoom_to_box(mapnik.Box2d(180, 30, 20, 85.0))
    mapnik.render_to_file(m, 'world.png', 'png')
