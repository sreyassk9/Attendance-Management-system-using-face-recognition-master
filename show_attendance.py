import tkinter as tk
from tkinter import *
import os
import csv
import pyttsx3

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

attendance_path = "D:\Downloads\Attendance-Management-system-using-face-recognition-master (1)\Attendance-Management-system-using-face-recognition-master\Attendance"

def show_attendance(subject, date):
    if subject == "" or date == "":
        t = "Please enter the subject and date!!!"
        # Display error message or perform text-to-speech
        return

    attendance_file = os.path.join(attendance_path, subject, f"{subject}_{date}.csv")
    if not os.path.isfile(attendance_file):
        t = f"No attendance record found for {subject} on {date}!"
        # Display error message or perform text-to-speech
        return

    root = Tk()
    root.title(f"Attendance of {subject} - {date}")
    root.configure(background="black")

    with open(attendance_file, newline="") as file:
        reader = csv.reader(file)
        r = 0

        for col in reader:
            c = 0
            for row in col:
                label = Label(
                    root,
                    width=10,
                    height=1,
                    fg="yellow",
                    font=("times", 15, "bold"),
                    bg="black",
                    text=row,
                    relief=RIDGE,
                )
                label.grid(row=r, column=c)
                c += 1
            r += 1

    root.mainloop()

def subjectchoose(text_to_speech):
    def on_show_attendance():
        subject = subject_entry.get()
        date = date_entry.get()
        show_attendance(subject, date)

    # Create the subject window
    subject_window = Tk()
    subject_window.title("Subject and Date")
    subject_window.geometry("500x300")
    subject_window.configure(background="black")

    subject_label = Label(
        subject_window,
        text="Enter the Subject",
        width=15,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    subject_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    subject_entry = Entry(
        subject_window,
        width=20,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 15, "bold"),
    )
    subject_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    date_label = Label(
        subject_window,
        text="Enter the Date",
        width=15,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    date_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    date_entry = Entry(
        subject_window,
        width=20,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 15, "bold"),
    )
    date_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    show_button = Button(
        subject_window,
        text="Show Attendance",
        command=on_show_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=15,
        relief=RIDGE,
    )
    show_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    subject_window.mainloop()

subjectchoose(text_to_speech)
