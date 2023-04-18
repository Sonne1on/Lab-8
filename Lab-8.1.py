import cv2
import numpy as np

# загрузка изображения
img = cv2.imread('images/variant-1.jpg')

# 1. перевод в полутоновый формат
def gray(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

# вывод изображения:
cv2.imshow('image', gray(img))

cv2.waitKey(0)
cv2.destroyAllWindows()
