# -*- coding: utf-8 -*-
import cv2 as cv 


capture = cv.VideoCapture(0)# 0Ϊ���
print(capture.isOpened())

success,frame = capture.read()
while True:
    cv.imshow("frame",frame)
    # ��ʱ
    cv.waitKey(1)
    success,frame = capture.read()

# �ͷ���Դ
capture.release()