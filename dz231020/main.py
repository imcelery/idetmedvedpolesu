
import cv2  # pip install opencv-python
import pytesseract
import pyautogui
import numpy as np

pil_img = pyautogui.screenshot()
pytesseract.pytesseract.tesseract_cmd = "Y://idetmedvedpolesu//dz231020//teseract//tesseract"

open_cv_image = np.array(pil_img)

open_cv_image = open_cv_image[:, :, ::-1].copy()
img = open_cv_image[-115:-95, -630:-30, :]
cv2.imwrite("sasas.png", img)
text = pytesseract.image_to_string(img)

print(int(text.strip()))
