# 🚗💤 Driver Drowsiness Detection using YOLO11

## 📌 Overview
This project implements a **Driver Drowsiness Detection** system using **YOLO11**, a state-of-the-art object detection model.  
The system continuously monitors the driver’s face to detect signs of drowsiness, such as **closed eyes, yawning, or head tilts**, and provides **alerts** to prevent accidents.

---

## 🎯 Features
✅ **Real-time drowsiness detection using YOLO11**  
✅ **Detects closed eyes, mouth, and yawning**  
✅ **Generates audio alerts to wake the driver**  
✅ **Works with webcams and dashboard cameras**  
✅ **High accuracy and low latency for real-time performance**  

---

## 🏠 Technologies Used
- **YOLO11** – Object detection model  
- **OpenCV** – Image processing  
- **Python** – Core programming language  
- **NumPy, Pandas** – Data processing  
- **Matplotlib** – Visualization  

---

## 📂 Datasets Used
The model was trained using the following datasets:

📌 **Yawning Detection Dataset**  
Dataset Name: **Drowsiness Detection**  
[Download Here](https://universe.roboflow.com/kuch-naya/drowsiness-detection-wvyt5)  

📌 **Eye & Mouth Detection Dataset**  
Dataset Name: **Eye-Mouth**  
[Download Here](https://universe.roboflow.com/shenmiren6z/eye-mouth-ntiym)  

---

## 📂 Pretrained Model Files
Download the **pretrained YOLO11 model weights** from Google Drive:  
📌 **[Download Model Weights](https://drive.google.com/drive/folders/19HD86tN8uuyuNWTq897MxYhRSK6d_6ni?usp=sharing)**  

After downloading, **place the model files** inside the `models/` directory:
```
/driver-drowsiness-yolo11/
│── models/
│   ├── EYE_MOUTH.pt
│   └── drowsiness.pt
│── detect.py
│── requirements.txt
│── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/driver-drowsiness-yolo11.git
cd driver-drowsiness-yolo11
```

---

### 2️⃣ Install Dependencies
Make sure Python 3.11 is installed, then run:

```sh
pip install -r requirements.txt
```

---

### 3️⃣ Download the YOLO11 Model Weights
- Download the **YOLO11** pretrained weights from **Google Drive**.
- Place the downloaded weight files inside the `models/` directory.

---

## 🔥 Running the Detection System (`detect.py`)

### 1️⃣ Run the script using your webcam
```sh
python detect.py
```
This will **activate the webcam** and begin detecting drowsiness.

---

### **2️⃣ Run the script with a video file**
```sh
python detect.py --source path/to/video.mp4
```
Replace `path/to/video.mp4` with the actual video file.

---

### **3️⃣ Adjust Thresholds (Optional)**
Modify `fatigue_threshold` in **`detect.py`** to change detection sensitivity:

```python
fatigue_threshold = 3  # Time (in seconds) before drowsiness is detected
```

---

## 🏆 Example Output
Once you run the script, the output will:
✅ **Draw bounding boxes around detected eyes and mouth**  
✅ **Display real-time alerts on the screen**  
✅ **Trigger an alarm sound if drowsiness is detected**  

---

## 👥 Contributing
Contributions are welcome! Feel free to:
- **Open an issue** for bugs or feature requests.
- **Submit a pull request** with improvements.

🛡️ **Stay alert, drive safe! 🚗🌬️**

