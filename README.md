# 🔥 Fire Detection System using Python & OpenCV

This project is a simple yet effective fire detection system using computer vision. It uses color thresholding and contour detection with OpenCV to identify fire in video frames in real-time or from a recorded video.

## 📌 Features

- Real-time fire detection using webcam or video file
- Frame-by-frame analysis with color-based filtering
- Bounding box on detected fire areas
- Alarm trigger or action-ready setup (can be extended)

## 🛠️ Technologies Used

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## 🖥️ How It Works

1. Captures video frames from a webcam or video file.
2. Converts each frame to HSV color space.
3. Applies a color range mask for fire-like colors.
4. Finds contours in the masked image.
5. Marks and tracks the fire regions on the video.

## 🚀 How to Run

### 🔧 1. Install Dependencies

```bash
pip install opencv-python numpy
