import os
import cv2
import numpy as np

haarcasecade_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\haarcascade_frontalface_default.xml"
trainimagelabel_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\TrainingImageLabel\Trainner.yml"
trainimage_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\TrainingImage"
studentdetail_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\StudentDetails\studentdetails.csv"
attendance_path = r"D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\Attendance"
# for choose subject and fill attendance
def UntrainAllImages(trainimage_path, trainimagelabel_path, message, text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the existing trained model
    if os.path.isfile(trainimagelabel_path):
        recognizer.read(trainimagelabel_path)

    # Remove all training images
    if os.path.isdir(trainimage_path):
        for root, dirs, files in os.walk(trainimage_path):
            for file in files:
                os.remove(os.path.join(root, file))
        os.rmdir(trainimage_path)

    # Train the model with an empty dataset
    recognizer.train([], np.array([]))
    recognizer.save(trainimagelabel_path)

    res = "All images untrained successfully"
    message.configure(text=res)
    text_to_speech(res)
