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

def main():
    img = cv2.imread("lena.bmp")
    new_img = resize(img,1024,1024)
    cv2.imwrite('Q3_answer.png',new_img)
    

if __name__=='__main__':
    main()
