# 🎥 Video Object and Person Detector

An interactive web application built with Streamlit that uses YOLOv8 to automatically detect objects and people in videos.

## ✨ Features

- 🎯 Automatic detection of **80+ object categories**
- 👥 Person recognition
- 🚗 Vehicle detection (cars, motorcycles, bicycles)
- 🐕 Animal identification
- 📊 Real-time statistics of detected objects
- ⬇️ Download processed video with annotations
- ⚙️ Adjustable confidence threshold

## 🚀 Live Demo

You can try the application online without installing anything:

**[🔗 Open App on Streamlit Cloud](https://cv-object-and-person-detector.streamlit.app)**

## 📦 Local Installation

### Prerequisites

- Python 3.8 - 3.10 (3.10 recommended)
- pip

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/Acquarts/cv-object-and-person-detector.git
cd cv-object-and-person-detector
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

**Note for Windows:** If you encounter DLL errors with PyTorch, run the included repair script:
```bash
fix_dependencies.bat
```

Note: The first time you run the application, the YOLOv8 model will be automatically downloaded (~6MB).

## 🎮 Usage

1. **Run the application:**

```bash
streamlit run video_detector.py
```

2. **Open your browser:**
   - The application will automatically open at `http://localhost:8501`

3. **Upload a video:**
   - Click "Upload your video"
   - Select a file (MP4, AVI, MOV, MKV)

4. **Adjust settings (optional):**
   - Use the slider in the sidebar to adjust the confidence threshold
   - Higher values = fewer detections but more accurate
   - Lower values = more detections but may include false positives

5. **Detect objects:**
   - Click "🚀 Detect Objects"
   - Wait while the video is processed
   - View results and statistics

6. **Download the result:**
   - Click "⬇️ Download Processed Video"

## 📋 Detectable Objects

The YOLOv8 model can detect the following categories:

### People and Animals
- People
- Dogs, cats, birds, horses, sheep, cows, elephants, bears, zebras, giraffes

### Vehicles
- Cars, motorcycles, airplanes, buses, trains, trucks, boats, bicycles

### Outdoor Objects
- Traffic lights, fire hydrants, stop signs, parking meters, benches

### Indoor Objects
- Sofas, chairs, tables, beds, toilets, TVs, laptops, mice, keyboards
- Cell phones, microwaves, ovens, toasters, refrigerators
- Books, clocks, vases, scissors, teddy bears

### Food and Drink
- Bottles, wine glasses, cups, forks, knives, spoons, bowls
- Bananas, apples, sandwiches, oranges, broccoli, carrots, pizzas, donuts

### And many more... (80+ categories in total)

## 🛠️ Technologies Used

- **Streamlit**: Framework for web interface
- **YOLOv8**: State-of-the-art object detection model
- **OpenCV**: Video processing
- **Ultralytics**: YOLO implementation
- **NumPy**: Numerical operations

## ⚙️ Advanced Configuration

### Change YOLO Model

By default, `yolov8n.pt` (nano) is used, which is fast but less accurate. You can switch to larger models on line 26 of the code:

```python
# Available options:
model = YOLO('yolov8n.pt')  # Nano (faster) ⚡
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium
model = YOLO('yolov8l.pt')  # Large
model = YOLO('yolov8x.pt')  # Extra Large (more accurate) 🎯
```

### Adjust Performance

- For long videos, consider reducing resolution
- Adjust processing FPS if you need more speed
- Use the nano model (yolov8n) for faster processing

## 🐛 Troubleshooting

### DLL Error on Windows (WinError 1114)
This is a common issue with PyTorch on Windows. Solution:
```bash
# Run the included repair script
fix_dependencies.bat
```

Or manually:
```bash
pip install torch==2.0.1 torchvision==0.15.2 --index-url https://download.pytorch.org/whl/cpu
pip install "numpy<2" opencv-python==4.10.0.84
```

### Error Loading Model
```bash
pip install --upgrade ultralytics
```

### OpenCV Issues
```bash
pip install opencv-python-headless==4.10.0.84
```

### Video Won't Play
- Make sure the video is in a compatible format (MP4, AVI, MOV, MKV)
- Try a different codec

### Processing is Very Slow
- Use the `yolov8n.pt` (nano) model
- Reduce input video resolution
- Process only part of the video

## 🌐 Deploy on Streamlit Cloud

To deploy your own version:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository and branch
5. The main file is `video_detector.py`
6. Automatic deployment!

The necessary files are already configured:
- `requirements.txt`: Python dependencies
- `packages.txt`: System dependencies (Linux)
- `.streamlit/config.toml`: App configuration

## 📝 Notes

- The first processing may take longer due to model download
- Processing time depends on:
  - Video duration
  - Video resolution
  - YOLO model used
  - Your hardware capacity
- High-resolution and long-duration videos require more time and resources

## 🤝 Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvement, don't hesitate to report them.

## 📄 License

This project uses:
- YOLOv8: AGPL-3.0 License
- Streamlit: Apache 2.0 License

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8
- [Streamlit](https://streamlit.io/) for the framework
- The Open Source community

---

**Enjoy detecting objects in your videos! 🎬🔍**
