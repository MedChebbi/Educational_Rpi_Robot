import cv2
import numpy as np

def main():
    face_cascade = cv2.CascadeClassifier('../resources/cascades/haarcascade_frontalface_alt2.xml') #load the face detection haarcascade model
    cap= cv2.VideoCapture(0)
    _, frame = cap.read()

    rows,cols,_=frame.shape

    while (True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w] # you can use this if you need to extract only the face you have detected in grayscale
            roi_color = frame[y:y, x:x+w]  # you can use this if you need to extract only the colored face you have detected 

            Color = (0,0,255) #BGR not RGB !
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),Color,1)
        cv2.imshow('Smile',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()