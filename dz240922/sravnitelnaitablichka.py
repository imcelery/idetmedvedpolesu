from sort import *
import random
import time
import pandas as pd
if __name__ == "__main__":
    m = []
    m.append([random.randint(-1000, 1000) for _ in range(10000)])
    m.append([random.randint(-1000, 1000) for _ in range(10000)])
    m.append([random.randint(-1000, 1000) for _ in range(10000)])
    d = {"sort_vi": sort_vi, "sort_p" : sort_p, "sort_v" : sort_v,  "sort_serge" : sort_serge}
    a = {}
    for i in d.keys():
        b = []
        for j in m:
            btime = time.time()
            d[i](j)
            b.append(time.time() - btime)
        b.append(sum(b))
        a.update({i:b})
    df = pd.DataFrame(a, index=['test_1', 'test_2', 'test_3', 'sum'])
    print(df)