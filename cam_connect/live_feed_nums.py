import cv2 
from cvzone.HandTrackingModule import HandDetector 
from cvzone.ClassificationModule import Classifier
import numpy as np 
import math
import os

cap = cv2.VideoCapture(0) 
detector = HandDetector(maxHands=1) 
offset = 20
imgSize = 300
previousIndex = 0
word = ""

current_dir = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(current_dir, "..", "model_files", "keras_model.h5"))
labels_path = os.path.abspath(os.path.join(current_dir, "..", "model_files", "labels.txt"))

categorizer = Classifier(model_path, labels_path)

counter = 0

while True:
    ret, frame = cap.read()
    cv2.imshow('Webcam Feed', frame)

    imgOut = frame.copy()
    hands, img = detector.findHands(frame) 

    if hands:
        hand = hands[0] 
        x, y, w, h = hand['bbox']  

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255  
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset] 
        imgCropShape = imgCrop.shape 
        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = categorizer.getPrediction(imgWhite, draw=False)
            #print(labels[index]) # see output real time
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = categorizer.getPrediction(imgWhite, draw=False)

        cv2.putText(imgOut, index+1, (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 0, 255), 2)
        cv2.rectangle(imgOut, (x-offset, y-offset), (x + w+offset, y + h+offset), (255, 0, 255), 4)

        
        cv2.imshow("ImageCrop", imgCrop) 
        cv2.imshow("ImageWhite", imgWhite)
    
        cv2.imshow("Image", imgOut)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
