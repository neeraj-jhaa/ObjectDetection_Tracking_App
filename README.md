Object Detection & Tracking Application
Overview
This is an Object Detection and Tracking Application built using YOLOv8 and OpenCV, which detects and tracks objects (especially people) in real-time using a webcam or uploaded video. The app leverages deep learning to detect various objects and provides a user-friendly GUI to interact with the system. The app also includes a tracking feature that tracks detected objects across frames.

Features
Real-Time Object Detection: Detects and tracks objects from the webcam or an uploaded video.

YOLOv8 Object Detection: Uses the latest YOLOv8 model for object detection.

Person Count: Tracks and counts the number of people detected in the video or camera feed.

Tracking: Tracks detected objects across frames and stores them.

Easy-to-use GUI: The application is equipped with an intuitive GUI for seamless interaction.

Stop Button: You can stop the detection process with a button on the interface.

Requirements
To run this project, you will need to install the following dependencies:

Python 3.x

YOLOv8 Pre-trained Model

OpenCV

TensorFlow

Other required Python libraries

You can install all the dependencies via the provided requirements.txt file.

Dependencies
To install the dependencies, open the terminal in your project directory and run:

bash
Copy
Edit
pip install -r requirements.txt
Installation
1. Clone the repository:
First, clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/neeraj-jhaa/ObjectDetection_Tracking_App.git
2. Install required libraries:
Navigate to the project directory and install all the required dependencies:

bash
Copy
Edit
cd ObjectDetection_Tracking_App
pip install -r requirements.txt
3. Download YOLOv8 Model Weights:
You can download the YOLOv8 pre-trained model weights (yolov8n.pt) from the official YOLO website. Place this file in the weights/ folder within your project directory.

Usage
1. Run the Application
To start the application, navigate to the project directory and run the following command:

bash
Copy
Edit
python main.py
2. GUI Interface
Start Detection: Click on the button to start detecting objects using your webcam or video file.

Stop Detection: Press the Stop button on the bottom right of the GUI to terminate the detection process.

Folder Structure
css
Copy
Edit
ObjectDetection_Tracking_App/
├── weights/
│   └── yolov8n.pt
├── main.py
├── requirements.txt
├── README.md
└── other project files...
weights/: Folder containing the YOLOv8 pre-trained model weights (yolov8n.pt).

main.py: The main Python file that runs the application.

requirements.txt: File containing the list of all Python libraries required to run the application.

README.md: This file.

Contributing
If you'd like to contribute to the development of this project, feel free to fork the repository, make improvements or add new features, and create a pull request. Any contributions or feedback are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
YOLOv8 for providing the powerful object detection model.

OpenCV for computer vision functionalities.

TensorFlow and PyTorch for deep learning support.
