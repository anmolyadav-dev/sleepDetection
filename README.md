
# SLEEP DETECTION AND ALERT FOR ONLINE CLASSES

This project is designed to virtually monitor attendees' engagement during online classes effectively. By utilizing live webcam feeds, the system detects whether attendees are actively participating in the class or are potentially disengaged due to sleep or lack of focus.



## How it works
The provided Python code implements an eye closure detection system using computer vision techniques. Here's a breakdown of how it works:  

* **Eye Aspect Ratio (EAR) Calculation**  
The code calculates the Eye Aspect Ratio (EAR) using the formula:

```bash
  ear = (A + B) / (2.0 * C)
```
where A, B, and C are distances between various landmarks on the eye. If the calculated EAR falls below a threshold value of 0.25, it indicates that the eyes may be drowsy or closed  


* **Alert Generation**  
When the EAR falls below the threshold, a timer is initiated to measure the duration of eye closure. Minor alerts are triggered at regular intervals to prompt the attendee to remain alert. If multiple minor alerts accumulate, a major alert is generated.  

* **Email Notification**  
Upon detection of a major alert, an email notification is sent to the guardian of the attendee to inform them of the potential drowsiness or lack of attentiveness.

## Installation

install dependencies

```bash
  pip install scipy imutils dlib cv2 pygame 
```
    
## Demo

Insert gif or link to demo


## Mandatory Files
- shape_predictor_68_face_landmarks.dat
- emailSender.py   
- assets/alertSound.mp3

## Use of Dependencies

  
**OpenCV** -  For face and eye detection   
**Pygame** -  To get the sound Alert   
**Scipy**  - Used for scientific computing, specifically for calculating distances in this code.   
**Emutils** -  Utilized for various image processing tasks, such as resizing frames,  
**dlib** - Utilized for advanced computer vision tasks like face and facial     landmark detection.  
**Time**-  Used for a count down timer implementation
## Authors

- [@Anmol_Yadav](https://www.github.com/anmolyadav-dev)
- [@Harsh_Arora](https://www.github.com/harsh-323)
- [@AmishKrishna](https://www.github.com/AmishKrishna)
