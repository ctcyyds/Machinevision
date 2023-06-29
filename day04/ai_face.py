from heimarobot import FaceSwapper

import cv2 as cv
import numpy as np

if __name__ == "__main__":
    face_swapper = FaceSwapper()
    trump1 = cv.imread("img/liyunlong.jpg")
    target = cv.imread("img/dongzhuo.jpg")

    sourceFace = face_swapper.get_source_face(trump1)

    dst = face_swapper.predict(sourceFace, target)

    cv.imshow("trump1", trump1)
    cv.imshow("1", target)
    cv.imshow("dst", dst)
    cv.waitKey()
