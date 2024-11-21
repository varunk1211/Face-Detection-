import pickle
import numpy as np
import cv2
import face_recognition

cap = cv2.VideoCapture(0)
cv2.namedWindow("window",cv2.WINDOW_NORMAL)
file = open("encodeFile.p","rb")
encodeListKnownWithId = pickle.load(file)
cv2.resizeWindow("window",1080,780)
file.close()

encodeListknown, studentId = encodeListKnownWithId
print(studentId)
while True:
    success,img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    faceCurrentTime=face_recognition.face_locations(imgs)
    currentFrame = face_recognition.face_encodings(imgs, faceCurrentTime, num_jitters=1)

    for encodeface, facloc in zip(currentFrame, faceCurrentTime):
        matches = face_recognition.compare_faces(encodeListknown,encodeface)
        distance = face_recognition.face_distance(encodeListknown, encodeface)
        print(matches,distance)

        matchIndex = np.argmin(distance)
        print("matchindex",matchIndex)
        if matches[matchIndex]:
            name = studentId[matchIndex]
            cv2.putText(img,f"{name}",(10,90),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),3)
            print("known face was detected", studentId[matchIndex])
        else:
            cv2.putText(img, f"not detected", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 244, 90), 3)

    cv2.imshow("window",img)
    if cv2.waitKey(25) & 0xff == ord('q'):
       break