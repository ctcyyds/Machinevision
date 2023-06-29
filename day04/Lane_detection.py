# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 读取视频数据
capture = cv.VideoCapture("img/road.mp4")
capture.isOpened()


def calc_line(y, k, b):
    x = (y - b) / k
    y2 = y / 2
    x2 = (y2 - b) / k
    return (int(x), int(y)), (int(x2), int(y2))


def fetch_roi(img, canny_img):
    # 提取感兴趣的区域
    height, width = frame.shape[0:2]
    points = np.array([[(300, height), (1080, height), (580, 283)]])
    # 创建mask蒙版
    mask = np.zeros_like(img)
    cv.fillPoly(mask, points, 255)
    # 利用mask从canny图中抠出感兴趣的区域
    roi_img = cv.bitwise_and(canny_img, mask)
    return roi_img


def fetch_lines(roi_img):
    rho = 1
    theta = np.pi / 180
    thresh = 20
    lines = cv.HoughLinesP(roi_img, rho, theta, thresh, minLineLength=10, maxLineGap=1)
    return lines


def get_line(height):
    # 将左右两边的多条线段合并成一条线段
    # 计算平均斜率和截距
    left_params = []
    right_params = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        params = np.polyfit((x1, x2), (y1, y2), 1)
        k = params[0]
        b = params[1]
        if k > 0:
            right_params.append(params)
        else:
            left_params.append(params)
    # 计算左右两边的平均值
    avg_left_params = np.average(left_params, axis=0)
    avg_right_params = np.average(right_params, axis=0)

    k = avg_left_params[0]
    b = avg_left_params[1]
    pt_l1, pt_l2 = calc_line(height, k, b)

    k = avg_right_params[0]
    b = avg_right_params[1]
    pt_r1, pt_r2 = calc_line(height, k, b)
    return pt_l1, pt_l2, pt_r1, pt_r2


while True:
    # 读取视频中的一帧数据
    success, frame = capture.read()
    height, width = frame.shape[0:2]
    # 获取灰度图
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 边缘检测
    canny_img = cv.Canny(gray, 50, 100)
    roi_img = fetch_roi(gray, canny_img)
    # 查找所有的线段
    lines = fetch_lines(roi_img)

    pt_l1, pt_l2, pt_r1, pt_r2 = get_line(height)

    # 绘制左右两边的直线
    result_img = frame.copy()
    cv.line(result_img, pt_r1, pt_r2, (0, 0, 255), 10)
    cv.line(result_img, pt_l1, pt_l2, (0, 255, 0), 10)
    cv.imshow("result_img", result_img)
    key = cv.waitKey(50)
    if key == 27:
        break
