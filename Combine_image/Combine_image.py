import cv2
import numpy
img1 = cv2.imread("laptop_left.png")
img2 = cv2.imread("laptop_right.png")
img_combin = cv2.hconcat([img1,img2])
cv2.imwrite("Q1_answer.png",img_combin)