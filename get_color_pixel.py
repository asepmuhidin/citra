import numpy as np
import cv2

img = cv2.imread("gambar2.jpeg")
b,g,r = img[120,161]

warna = np.zeros((200,200,3),dtype=np.uint8)
warna[:] = [b,g,r]

cv2.imshow("Warna Pixel",warna)
cv2.waitKey(0)