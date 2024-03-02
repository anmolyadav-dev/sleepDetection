from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import time
import pygame
from emailSender import SendEmail

pygame.init()
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

thresh = 0.25
frame_check = 70
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
start_time = time.time()
closed_eye_time = 0
start_time1=time.time()
seconds = 0
secondsFace=0
n=0
mincount=0
majorcount=0
while True:
    ret, frame=cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    
    
    
    
    nofaceTime=0
    for subject in subjects:
        secondsFace=0
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        
        if ear < thresh:
            flag+=1
            #print(flag)
            closed_eye_time += time.time() - start_time
            if int(closed_eye_time) >= 6:
                cv2.putText(frame, "****************ALERT!****************", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "****************ALERT!****************", (10,325),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                #print ("Drowsy")
                
            if (int(closed_eye_time) % 6==0) and (int(closed_eye_time) > seconds):
                mincount+=1
                print(mincount)
                
                
        else:
            flag = 0
            closed_eye_time = 0
            seconds = 0
			
    
        start_time = time.time()
    else:
        
        # print(int(time.time() - start_time))
        nofaceTime += time.time() - start_time
        if int(nofaceTime) >= 6:
                
                cv2.putText(frame, "****************ALERT!****************", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "****************ALERT!****************", (10,325),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        if (int(nofaceTime) % 6==0) and (int(nofaceTime) > secondsFace):
                mincount+=1
                print(mincount)
                
        

    if (int(nofaceTime) > secondsFace 	) :
        print("Eyes not detected for:", int(nofaceTime), "seconds")
    secondsFace = int(nofaceTime) 
    
    if (int(closed_eye_time) > seconds 	) :
        print("Eyes closed for:", int(closed_eye_time), "seconds")
        
    seconds = int(closed_eye_time) 
    
    if(mincount>5):  #for every 36 seconds of unattentiveness a alert will be notified on the screen
        majorcount+=1;
        sound = pygame.mixer.Sound('assets/alertSound.mp3')
        sound.play()
        mincount=0

    if(majorcount>2): #for every 3 minutes of untattentiveness a mail will be sent 
        print("Sending mail...\nPlease be Attentive.")
        SendEmail("darkSavour1@gmail.com")
        print("Mail Sent.")
        break
        
    if(int(time.time() - start_time1)%60==0):
         mincount=0


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(20) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
