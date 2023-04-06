import numpy as np
import cv2 
import math

def image_rotate(image, degree):
    # First we will convert the degrees into radians
    rads = math.radians(degree)
    imh = image.shape[0]
    imw = image.shape[1] 
    #Set the size of rotating image
    dim = (round(math.sqrt(imh*imh+imw*imw)),round(math.sqrt(imh*imh+imw*imw)),image.shape[2])
    # We consider the rotated image to be of the same size as the original
    rot_img = np.uint8(np.zeros(dim))

    # Finding the center point of rotated (or original) image.
    height = rot_img.shape[0]
    width  = rot_img.shape[1]
    midx,midy = (width//2+1, height//2+1)

    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
            y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)
            #將x,y調至中間
            y+=midy/(math.sqrt(2))
            x+=midx/(math.sqrt(2))
            #將x,y設回整數
            x=round(x)
            y=round(y)

            if (x>=0 and y>=0 and x<image.shape[0] and  y<image.shape[1]):
                rot_img[i,j,:] = image[x,y,:]

    return rot_img 

def main():
    img1 = cv2.imread("laptop_left.png")
    img2 = cv2.imread("laptop_right.png")
    img_combin = cv2.hconcat([img1,img2])
    r_image = image_rotate(img_combin,15)
    cv2.imshow("Q2",r_image)
    cv2.waitKey(3000)
    cv2.imwrite("Q2_answer.png",r_image)

if __name__=='__main__':
    main()