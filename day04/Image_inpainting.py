# -*- coding: gbk -*-
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("img/itheima_inpaint.jpg")
height, width = img.shape[0:2]
mask = np.zeros((height, width), np.uint8)


def onMouse(event, x, y, flags, param):
    global img, mask
    if event == cv.EVENT_LBUTTONDOWN:
        print("左键按下")
    elif event == cv.EVENT_LBUTTONUP:
        img = cv.inpaint(img, mask, 10, cv.INPAINT_TELEA)
        cv.imshow("img", img)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        # 绘制mask图像
        cv.circle(mask, (x, y), 5, 255, -1)
        cv.imshow("mask", mask)


cv.imshow("img", img)

cv.setMouseCallback("img", onMouse, 123)
cv.waitKey(0)
