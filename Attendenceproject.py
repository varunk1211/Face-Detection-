import pickle

import cv2
import numpy as np
import face_recognition
import os

from main import studentId

path = 'Imagesof'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
#
encodeListKnown = findEncodings(images)
encodeListKnownWithId=[encodeListKnown,classNames]
print(encodeListKnownWithId)
# Save the encodings and class names to a pickle file
file=open('encodeFile.p',"wb")
pickle.dump(encodeListKnownWithId,file)
file.close()

