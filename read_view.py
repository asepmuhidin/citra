import cv2

img = cv2.imread("gambar2.jpeg")
cv2.imshow("Citra", img)
cv2.waitKey(0)
cv2.destroyAllWindows()