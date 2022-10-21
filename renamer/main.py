import os

def rename(oldname, newname, directory):
    res = os.system(directory)
    # + " git mv " + oldname + " " + newname

if __name__ == '__main__':
    path = "Y:\idetmedvedpolesu"
    dirs = os.listdir(path=path)
    for i in dirs:
        if i[:2] == "dz" and len(i) != 10:
            d = i[2:4]
            m = i[4:6]
            y = i[6:8]
            rename(i, "dz20"+y+m+d, path)
