import cv2
from ultralytics import YOLO
import numpy as np
import threading
from tkinter import *
from tkinter import filedialog
import os

# Load YOLOv8 model
model = YOLO("weights/yolov8n.pt")

# Global variables
stop_flag = False
person_count = 0

def start_detection(video_path=None):
    global stop_flag, person_count
    stop_flag = False
    person_count = 0

    if video_path:
        cap = cv2.VideoCapture(video_path)
        output_name = os.path.basename(video_path)
    else:
        cap = cv2.VideoCapture(0)
        output_name = "webcam_output.avi"

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(f'output/{output_name}', fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret or stop_flag:
            break

        # Run detection
        results = model(frame)
        annotated_frame = results[0].plot()

        # Count number of people detected
        labels = results[0].names
        boxes = results[0].boxes.cls.cpu().numpy()
        people = [label for label in boxes if labels[int(label)] == 'person']
        person_count = len(people)

        # Display people count on frame
        cv2.putText(annotated_frame, f'People Detected: {person_count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Real-Time Detection", annotated_frame)
        out.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def open_video():
    video_path = filedialog.askopenfilename()
    if video_path:
        threading.Thread(target=start_detection, args=(video_path,)).start()

def start_webcam():
    threading.Thread(target=start_detection).start()

def stop_detection():
    global stop_flag
    stop_flag = True

# GUI Setup
root = Tk()
root.title("Object Detection & Tracking App")

root.geometry("350x200")
root.configure(bg="#202020")

title = Label(root, text="Object Detection with YOLOv8", font=("Arial", 16), fg="white", bg="#202020")
title.pack(pady=10)

btn_webcam = Button(root, text="Start Webcam Detection", command=start_webcam, width=25, bg="#1f8ef1", fg="white")
btn_webcam.pack(pady=5)

btn_video = Button(root, text="Select Video for Detection", command=open_video, width=25, bg="#1f8ef1", fg="white")
btn_video.pack(pady=5)

btn_stop = Button(root, text="Stop Detection", command=stop_detection, width=25, bg="#eb4d4b", fg="white")
btn_stop.pack(pady=5)

root.mainloop()
