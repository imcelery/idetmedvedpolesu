import sys

import imlyc
def ad(a):
    a = []
if __name__ == '__main__':
    name = "4.jpg"
    # if len(sys.argv) == 2:
    #     name = sys.argv[1]
    # first_name, ras = name.split(".")
    img = imlyc.ImageL(name)
    img.blur()
    img.save_img("lgrey.jpg")
    i = 1
    while True:
        print(i)
        img = imlyc.ImageL("lgrey.jpg")
        img.blur()
        img.save_img("lgrey.jpg")
        i += 1

