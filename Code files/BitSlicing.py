import numpy as np
import cv2
img=cv2.imread('C:/Image Steganography/Examples/Encoding Image.jpg',0)
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/Orginal Image.jpg',img)
cv2.waitKey(0)
lst = []
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		lst.append(np.binary_repr(img[i][j], width=8))


eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])

cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 7.jpg',cv2.normalize(eight_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 6.jpg',cv2.normalize(seven_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 5.jpg',cv2.normalize(six_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 4.jpg',cv2.normalize(five_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 3.jpg',cv2.normalize(four_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 2.jpg',cv2.normalize(three_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 1.jpg',cv2.normalize(two_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imwrite('C:/Image Steganography/Examples/Bitplanes/bit plane 0.jpg',cv2.normalize(one_bit_img , np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.waitKey(0)
#You can give any destination path for saving the images...