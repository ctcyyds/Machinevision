# -*- coding: utf-8 -*-
import cv2 as cv 


capture = cv.VideoCapture(0)# 0为编号
print(capture.isOpened())

success,frame = capture.read()
while True:
    cv.imshow("frame",frame)
    # 延时
    cv.waitKey(1)
    success,frame = capture.read()

# 释放资源
capture.release()