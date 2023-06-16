import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image

haarcasecade_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\haarcascade_frontalface_default.xml"
trainimagelabel_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\TrainingImageLabel\Trainner.yml"
trainimage_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\TrainingImage"
studentdetail_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\StudentDetails\studentdetails.csv"
attendance_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\Attendance"
# for choose subject and fill attendance
# Train Image
def TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message,text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(trainimagelabel_path)
    res = "Image Trained successfully"  # +",".join(str(f) for f in Id)
    message.configure(text=res)
    text_to_speech(res)


def getImagesAndLables(path):
    # imagePath = [os.path.join(path, f) for d in os.listdir(path) for f in d]
    newdir = [os.path.join(path, d) for d in os.listdir(path)]
    imagePath = [
        os.path.join(newdir[i], f)
        for i in range(len(newdir))
        for f in os.listdir(newdir[i])
    ]
    faces = []
    Ids = []
    for imagePath in imagePath:
        pilImage = Image.open(imagePath).convert("L")
        imageNp = np.array(pilImage, "uint8")
        Id = int(os.path.split(imagePath)[-1].split("_")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids
