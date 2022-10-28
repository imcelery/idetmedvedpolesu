from PIL import Image
import numpy as np
from copy import deepcopy

def hex_to_dec(value: str) -> str:
    razrid = 0
    decnumb = 0
    s = {"1" : 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b":11, "c":12, "d":13, "i":14, "f":15}
    for i in value[::-1]:
        decnumb += s[i] * (16 ** razrid)
        razrid += 1
    return str(decnumb)


def devisors(value: int) -> list[int]:
    m = 2
    a = []
    while value > 1:
        if value % m == 0:
            value /= m
            a.append(m)
        else:
            m += 1
    return a

def dec_to_bin(value: int) -> str:
    b = ""
    while value >= 1:
        if value % 2 == 0:
            value /= 2
            b += "0"
        else:
            b += "1"
            value //= 2
    return b[::-1]

def get_bytes(bin1, bin2, img):
    a = []
    for i in range(len(bin1)):
        for j in range(len(bin2)):
            if bin1[i] == "1" and bin2[j] == "1":
                a.append(img[i, j])
    return a


def get_chars(byte_array):
    s = ""
    for i in byte_array:
        if i != 32:
            s += chr(i + 1000)
        else:
            s += chr(i)
    return s


def caesar_encryptor(text: str, n: int) -> str:
    al = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    s = ""
    for i in text:
        s += al[(al.find(i) + n) % len(al)]
    return s


def caesar_decryptor(text: str, n: int) -> str:
    al = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    s = ""
    for i in text:
        s += al[(al.find(i) + n) % len(al)]
    return s


def caesar_brootforce(text: str):
    al = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    for i in range(len(al)):
        print(caesar_decryptor(text, i))

def get_bin_array(img):
    s = ""
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i, j, 0] % 2 == 1:
                s += "1"
            else:
                s += "0"
    return s


def bin_to_dec(bin : str):
    dec = 0
    razrid = 1
    for i in bin[::-1]:
        if i == "1":
            dec += razrid
        razrid *= 2
    return dec

def get_char_from_bin_array(bin_array):
    s = ""
    for i in range(len(bin_array) // 8):
        c = bin_to_dec(bin_array[i*8:(i+1)*8])
        if c != 32:
            s += chr(c + 1000)
        else:
            s += chr(c)
    return s

def vigenere_encryptor(text: str, key:str) -> str:
    keyn = 0
    s = "абвгдеёжзийклмнопрстуфхцчшюъыьэюя "
    ns = ""
    for i in text:
        print(s.find(key[keyn]))
        sdv = s.find(key[keyn]) + s.find(i)
        print(sdv)
        if sdv >= len(s):
            sdv -= len(s)
        ns += s[sdv]
        keyn = (keyn + 1) % len(key)
    return ns


def vigenere_decryptor(text: str, key:str) -> str:
    keyn = 0
    s = "абвгдеёжзийклмнопрстуфхцчшюъыьэюя "
    ns = ""
    for i in text:
        sdv = s.find(i) - s.find(key[keyn])
        if sdv < 0:
            sdv = len(s) + sdv
        ns += s[sdv]
        keyn = (keyn + 1) % len(key)
    return  ns


if __name__ == '__main__':

    v1 = hex_to_dec("1f933b5")
    v2, v3 = devisors(int(v1))
    v4 = dec_to_bin(v2)
    v5 = dec_to_bin(v3)

    filepath = "11.png"
    with Image.open(filepath) as img:
        img.load()
    img = np.asarray(img)
    shfr = get_chars(get_bytes(v4, v5, img))
    caesar_brootforce(shfr)
    print(" ")
    filepath = "222.bmp"
    with Image.open(filepath) as img:
        img.load()
    img = np.asarray(img)
    bin_array = get_bin_array(img)

    chars = get_char_from_bin_array(bin_array)

    print(vigenere_decryptor(chars, "не  ошибается  тот  кто ничего  не  делает"))

