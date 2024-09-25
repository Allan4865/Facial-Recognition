# Facial-Recognition
This project implements a **real-time facial recognition system** using a custom-trained **Convolutional Neural Network (CNN)** in Python. The application captures live video, processes the frames, and identifies individuals based on a custom-trained model. It is built using **Flask** for the backend and **HTML/JavaScript** for the frontend.

## Features:
- **Custom-Trained CNN**: A CNN model trained with images of both authorized users and individuals that need to be recognized.
- **Live Video Recognition**: The system processes frames from a live video feed to identify individuals in real time.
- **Flask Backend**: Manages routes and processes live video feeds, interacting with the custom-trained model to recognize faces.
- **HTML/JS Frontend**: Provides a live video interface with real-time recognition results. JavaScript handles video streaming and backend interaction.
- **Recognition/Unrecognized Status**: The system displays the recognized person's name or "Not Recognized" if the individual isn't found in the database.

## Tech Stack:
- **Python**: For backend logic and model training.
- **Flask**: Handles server-side operations.
- **HTML/CSS/JS**: Frontend for live video streaming and results display.
- **OpenCV**: Captures and processes video for real-time face recognition.
- **TensorFlow/Keras**: Trains and runs the CNN model.

## Usage:
- **Live Video Feed**: Captures live video, analyzing each frame for facial recognition.
- **Recognition**: The custom CNN identifies people based on the trained dataset.
- **Result**: Displays the recognized individual’s name or "Not Recognized" for unidentified persons.
