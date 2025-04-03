#!/usr/bin/env python
# coding: utf-8

# In[17]:


import cv2
import torch
import time
import winsound
from ultralytics import YOLO

model1 = YOLO("/models/EYE_MOUTH.pt")  # Model 1 (e.g., Eye detection)
model2 = YOLO("/models/drowsiness.pt")  # Model 2 (e.g., Mouth detection)
cap = cv2.VideoCapture(0)

closed_eye_start = None
fatigue_threshold = 3  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run both models
    results1 = model1(frame)
    results2 = model2(frame)

    detected_labels_1 = set()
    detected_labels_2 = set()

    # Function to draw detections
    def draw_detections(results, frame, color, model, detected_labels):
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                
                if cls in model.names:
                    label = model.names[cls]
                    detected_labels.add(label)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
                    cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Draw detections from both models
    draw_detections(results1, frame, (0, 255, 0), model1, detected_labels_1)  # Green for Model 1
    draw_detections(results2, frame, (255, 0, 0), model2, detected_labels_2)  # Blue for Model 2

    # Fatigue Detection Logic
    current_time = time.time()

    # If eyes are closed
    if "closed_eye" in detected_labels_1:
        if closed_eye_start is None:
            closed_eye_start = current_time
        elif current_time - closed_eye_start > fatigue_threshold:
            cv2.putText(frame, "WARNING: DROWSINESS DETECTED!", (50, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            winsound.Beep(1000, 500)  # Beep sound for alert
    else:
        closed_eye_start = None  # Reset if eyes are open

    # If yawning is detected
    if "Yawning" in detected_labels_2:
        cv2.putText(frame, "WARNING: YAWNING DETECTED!", (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        winsound.Beep(1500, 700)  # Higher frequency beep

    # If drowsy is detected from Model 2
    if "Drowsy" in detected_labels_2:
        cv2.putText(frame, "ALERT: DRIVER DROWSY!", (50, 150), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        winsound.Beep(2000, 1000)  # Long alert beep

    # If both closed eyes and closed mouth for long → High fatigue
    if "closed_eye" in detected_labels_1 and "open_mouth" in detected_labels_1:
        if closed_eye_start is not None and current_time - closed_eye_start > fatigue_threshold:
            cv2.putText(frame, "ALERT: EXTREME FATIGUE DETECTED!", (50, 200), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            winsound.Beep(2500, 1200)  # Long fatigue alert

    # Show the frame
    cv2.imshow("Fatigue Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

