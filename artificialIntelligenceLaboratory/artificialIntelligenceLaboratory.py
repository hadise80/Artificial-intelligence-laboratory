import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") ;

img = cv2.imread("img.jpg") ;

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY) ;

face = face_cascade.detectMultiScale(gray, scaleFactor=1.3 , minNeighbors=3) ;

for (x , y , w , h) in face :
    cv2.rectangle(img, (x,y), (x+w , y+h), (0 , 0 , 255), 30) ;

cv2.imwrite("output.png" , img) ;