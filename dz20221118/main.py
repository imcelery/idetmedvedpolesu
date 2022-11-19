import librosa
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np





y, sr = librosa.load('komar-blizkii-zvonkii-chetkii.wav')


def f(l:list, k:int):
    s = len(y)//k
    plt.plot(y[::s])
    plt.xticks(np.arange(0, len(y) / s, s))
    plt.xlabel('секунды')
    plt.ylabel('амплитуда?')

    plt.show()

f(y, 1000)
#negativ_y = [-i for i in y ]

