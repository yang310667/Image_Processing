import numpy as np
import cv2 
import math
from PIL import Image

def extract(image):
    h,w,c = image.shape
    ext_img = np.uint8(np.zeros((h,w,c)))
    #取浮水印圖最後3bits並還原
    for i in range(h):
        for j in range(w):
            for k in range(c):
                    ext_img[i,j,k] = (image[i,j,k]%8)*32
    return ext_img


def PSNR(ori_img,img,size_of_pixel):
     h,w,c = ori_img.shape
     MSE = 0.0
     for i in range(h):
          for j in range(w):
               for k in range(c):
                    MSE += (ori_img[i,j,k]-img[i,j,k])**2
     MSE = MSE/(h*w*c)
     psnr = 10*math.log((size_of_pixel-1)**2/MSE,10)
     return psnr
                    
img = cv2.imread('Q5_1_water.png')


img_com_10  = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 10])[1]
img_com_50  = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])[1]
img_com_100 = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])[1]

img_decom_10  = cv2.imdecode(np.frombuffer(img_com_10, np.uint8), cv2.IMREAD_COLOR)
img_decom_50  = cv2.imdecode(np.frombuffer(img_com_50, np.uint8), cv2.IMREAD_COLOR)
img_decom_100 = cv2.imdecode(np.frombuffer(img_com_100, np.uint8), cv2.IMREAD_COLOR)

ori_img = cv2.imread("lena.bmp")


psnr_10  = PSNR(ori_img,img_decom_10,256)
psnr_50  = PSNR(ori_img,img_decom_50,256)
psnr_100 = PSNR(ori_img,img_decom_100,256)

print("PSNR_10: ",psnr_10)
print("PSNR_50: ",psnr_50)
print("PSNR_100: ",psnr_100)

img_ext_10  = extract(img_decom_10)
img_ext_50  = extract(img_decom_50)
img_ext_100 = extract(img_decom_100)

cv2.imwrite('Q5_2_10.png',img_ext_10)
cv2.imwrite('Q5_2_50.png',img_ext_50)
cv2.imwrite('Q5_2_100.png',img_ext_100)
