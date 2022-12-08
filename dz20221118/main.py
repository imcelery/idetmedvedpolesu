import librosa
import soundfile as sf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

def show(l:list, sr:int,  k=-1):
    if k == -1:
        k = len(l)
    t = len(l)/sr
    graf = l[::len(l)//k]
    plt.plot(graf)
    labels = np.arange(0, t, step=1)
    x = np.arange(0, len(graf), step=len(graf)//t)
    plt.xticks(x, labels)
    plt.xlabel('время (секунды)')

    plt.show()

def get_hige(y:list):
    znak = -(y[0] - y[1])
    i = 1
    if znak > 0:
        while y[i] < y[i + 1]:
            i += 1
        return y[i + 1]
    if znak < 0:
        while y[i] > y[i + 1]:
            i += 1
        return y[i + 1]





def get_frequency(l:list, sr:int, begin=0):

    i = begin
    z = l[begin] > 0
    x = l[i] > 0
    while x == z:
        i += 1
        if i >= len(l):
            return None
        x = l[i] > 0
    sb = i

    i += 1
    if i >= len(l):
        return None
    z = l[i] > 0
    x = l[i] > 0
    while x == z:
        i += 1
        if i >= len(l):
            return None
        x = l[i] > 0

    return int(len(l) / (i - sb) / (len(l)/sr) / 2)

def get_middle_frequency(l:list, sr:int, interval=500):
    a = []
    for i in range(0, len(l), interval):
        b = get_frequency(l, sr, i)
        if b is not None:
            a.append(b)
    return sum(a) // len(a)

def sinosoida(frequency, amplitude, sr, t=1):
    s = list(map(lambda x: amplitude * math.sin(2 * frequency * x * 3.14), np.arange(0, t, 1/sr)))
    sf.write('stereo_file1.wav', s, sr, 'PCM_24')
    return s

if __name__ == "__main__":

    y, sr = librosa.load('zvuk-komara-pisk-komara-28624.wav')

    show(y, sr)



