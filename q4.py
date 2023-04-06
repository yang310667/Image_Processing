from rembg import remove
from PIL import Image
import numpy as np
import cv2
import math

def resize(image, new_h, new_w):
	#get dimensions of original image
	old_h, old_w, c = image.shape
	#Create an array for the desire image
	resized = np.uint8(np.zeros((new_h, new_w, c)))
	#Calculate horizontal and vertical scaling factor
	x_scale = (old_w ) / (new_w ) if new_h != 0 else 0
	y_scale = (old_h ) / (new_h ) if new_w != 0 else 0
	for i in range(new_h):
		for j in range(new_w):
			#map the corridinate to the old image
			x = i * y_scale
			y = j * x_scale
			#Compute the pixel of the four around corner
			x_floor = math.floor(x)
			x_ceil = min( old_h - 1, math.ceil(x))
			y_floor = math.floor(y)
			y_ceil = min(old_w - 1, math.ceil(y))
            #Bilinear Interpolation 
			if (x_ceil == x_floor) and (y_ceil == y_floor):
				q = image[int(x), int(y), :]
			elif (x_ceil == x_floor):
				q1 = image[int(x), int(y_floor), :]
				q2 = image[int(x), int(y_ceil), :]
				q = q1 * (y_ceil - y) + q2 * (y - y_floor)
			elif (y_ceil == y_floor):
				q1 = image[int(x_floor), int(y), :]
				q2 = image[int(x_ceil), int(y), :]
				q = (q1*(x_ceil - x)) + (q2*(x - x_floor))
			else:
				v1 = image[x_floor, y_floor, :]
				v2 = image[x_ceil, y_floor, :]
				v3 = image[x_floor, y_ceil, :]
				v4 = image[x_ceil, y_ceil, :]

				q1 = v1 * (x_ceil - x) + v2 * (x - x_floor)
				q2 = v3 * (x_ceil - x) + v4 * (x - x_floor)
				q = q1 * (y_ceil - y) + q2 * (y - y_floor)

			resized[i,j,:] = q
	return resized

def remove_bg(image):
    input_img = Image.open(image)
    output_img = 'output_q4_1.png'
    ouput = remove(input_img)
    ouput.save(output_img)
    return ouput

def overlay(under_img, top_img):
    sizeh = under_img.shape[0]
    sizew = under_img.shape[1]
    c     = under_img.shape[2]
    o_img = np.uint8(np.zeros((sizeh,sizew,c)))
    for i in range(sizeh):
        for j in range(sizew):
            o_img[i,j,:] = under_img[i,j,:]
    for k in range(top_img.shape[0]):
        for m in range(top_img.shape[1]):
            if all(top_img[k,m,:]==0) :
                continue
            else:
                o_img[k,m,:] = top_img[k,m,:]
    return o_img

def main():
	img = cv2.imread('lena.bmp')
	imgu = resize(img,1024,1024)
	cv2.imwrite('output_q4_2.png',imgu)
	imgt = remove_bg('graveler.bmp')
	imgu = cv2.imread('output_q4_2.png')
	imgt = cv2.imread('output_q4_1.png')
	final_img = overlay(imgu,imgt)
	cv2.imwrite("Q4_answer.png",final_img)


if __name__=='__main__':
    main()

