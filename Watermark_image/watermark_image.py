import numpy as np
import cv2 
import math
def watermark(img,wm1):
    h1,w1,c1 = wm1.shape
    h2,w2,c2 = img.shape
    #建立watermark圖，圖型大小與原圖相同且為8bits pixel圖
    wm = np.uint8(np.zeros((h1,w1,c1)))
    water_img = np.uint8(np.zeros((h2,w2,c2)))
    #將原本的浮水印中的pixel整除32成為新的浮水圖（為取8bits中前面3bits作為分類依據）
    for i in range(h1):
        for j in range(w1):
            for k in range(c1):
                wm[i,j,k] = wm1[i,j,k]
    for i in range(h1):
        for j in range(w1):
            for k in range(c1):
                wm[i,j,k] = wm[i,j,k]//32
    #確保原圖中最後3bits皆為0
    for i in range(h2):
        for j in range(w2):
            for k in range(c2):
                img[i,j,k] = (img[i,j,k]//8)*8
    #將改良的浮水圖與原圖相加
    for i in range(h2):
        for j in range(w2):
            for k in range(c2):
                if i<h1 and j<w1 and k<c1:
                    water_img[i,j,k] = int(img[i,j,k])+int(wm[i,j,k])
                else:
                    water_img[i,j,k] = int(img[i,j,k])
    return water_img
def extract(image):
    h,w,c = image.shape
    ext_img = np.uint8(np.zeros((h,w,c)))
    #取浮水印圖最後3bits並還原
    for i in range(h):
        for j in range(w):
            for k in range(c):
                    ext_img[i,j,k] = (image[i,j,k]%8)*32
    return ext_img



def main():
    new_img = cv2.imread('lena.bmp')
    new_wm  = cv2.imread('graveler.bmp')
    result_image = watermark(new_img,new_wm)
    cv2.imwrite('Q5_1_water.png',result_image)
    wat_img = cv2.imread('q5_1_water.png')
    recover_image = extract(wat_img)
    cv2.imwrite('Q5_1_recover.png',recover_image)


if __name__=='__main__':
    main()