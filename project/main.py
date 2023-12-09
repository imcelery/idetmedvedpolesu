import pyautogui
import numpy as np
import time
x1 = 1330
y1 = 990
b = False
#pyautogui.mouseInfo()
while True:
    pil_img = pyautogui.screenshot()
    open_cv_image = np.array(pil_img)
    nb = sum(open_cv_image[y1, x1]) < 100
    if nb != b:
        with open("pupu.txt", "a") as f:
            f.write(str(int(nb)) + "\n")
        b = nb
    time.sleep(0.01)