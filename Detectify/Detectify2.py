import cv2
from cv2 import rectangle 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img = cv2.imread("Zendaya.2.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces =  face_cascade.detectMultiScale(gray_img,
                                        scaleFactor = 1.05,
                                        minNeighbors=5)

for x, y, w, h in faces: 
    img = cv2,rectangle(gray_img, (x,y), (x+w, y+h), (0,255,0), 30)

print(type(faces))
print(faces)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()