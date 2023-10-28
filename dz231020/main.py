import time

import cv2  # pip install opencv-python
import pytesseract
import pyautogui
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "Y://idetmedvedpolesu//dz231020//teseract//tesseract"
text = ""
newtext = ""
a = 0
with open("output.txt", "w") as f:
    while True:
        pil_img = pyautogui.screenshot()
        open_cv_image = np.array(pil_img)
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        img = open_cv_image[-130:-115, -620:-500, :]
        newtext = pytesseract.image_to_string(img)
        newtext = newtext.replace('@', '0')
        newtext = newtext.replace('e', '0')
        newtext = newtext.replace('(', '')
        newtext = newtext.strip()
        if newtext != text:
            f.write(newtext)
            f.write("\n")
            text = newtext
            a += 1
            print(text)
            if a > 30:
                break
