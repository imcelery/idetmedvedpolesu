from sort import *
import random
import time
import matplotlib.pyplot as plt
if __name__ == "__main__":
    config = list(range(1, 10000, 100))
    minim, maxim  = -100, 100
    kolvotestov = 1
    #
    d = {"sort_vi": [sort_vi, []], "sort_p": [sort_p, []], "sort_v": [sort_v, []], "sort_serge": [sort_serge, []]}
    m = []
    for i in config:
        a = []

        for j in range(kolvotestov):
            a.append([random.randint(minim, maxim) for _ in range(i)])
        m.append(a)

    for i in d.keys():
        for j in m:
            b = []
            btime = time.time()
            for k in j:
                aboba = d[i][0](k)
            d[i][1].append((time.time() - btime)/kolvotestov)

    fig, ax = plt.subplots()
    for i in d.keys():
        ax.plot(config, d.get(i)[1], label = str(i))
    ax.legend()
    plt.ylabel('time')
    plt.xlabel('len')
    plt.show()

