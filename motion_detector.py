import cv2,time
cap = cv2.VideoCapture(cv2.CAP_DSHOW)
ret,fram1 = cap.read()
ret,fram2 = cap.read()
while True:
    diff = cv2.absdiff(fram1,fram2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i,contour in enumerate(contours):
        (x,y,w,h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour)>1000:
            #print("recording...")
            cv2.imwrite(f"rec{i}.jpg",fram1)
            #cv2.rectangle(fram1,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.imshow('recording',fram1)
    #cv2.imshow('diff',thresh)
    fram1=fram2
    ret,fram2 = cap.read()
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

