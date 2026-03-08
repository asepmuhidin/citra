import cv2

img = cv2.imread("gambar2.jpeg")

def ambil_pixel(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b,g,r = img[y,x]

        print("Koordinat :",x,y)
        print("Blue :",b)
        print("Green :",g)
        print("Red :",r)

cv2.imshow("Image",img)
cv2.setMouseCallback("Image",ambil_pixel)
cv2.waitKey(0)
cv2.destroyAllWindows()