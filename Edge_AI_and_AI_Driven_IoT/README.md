# Edge AI and AI-Driven IoT

## Description
This project demonstrates the application of AI on edge devices and its integration with IoT systems. It includes a prototype for trash classification and a conceptual design for smart agriculture.

## Key Features
- **Edge AI Prototype**: A lightweight image classification model for sorting trash, optimized for edge devices using TensorFlow Lite.
- **AI-Driven IoT Concept**: A theoretical framework for a smart agriculture system that uses IoT sensors and AI to predict crop yields.

## Dataset (Edge AI)
- **Name**: Trash Type Image Dataset.
- **Source**: [Kaggle](https://www.kaggle.com/datasets/farzadnekouei/trash-type-image-dataset).
- **Classes**: Glass, Paper, Cardboard, Plastic, Metal, Trash.

## Tech Stack
- **Edge AI**: TensorFlow, TensorFlow Lite, Python.
- **IoT Concept**: Sensor integration (Soil moisture, Temperature), Data flow design.

## Project Structure
- `Edge_AI.ipynb`: Notebook for training the trash classification model.
- `trash_model.tflite`: Converted TFLite model for edge deployment.
- `trash_model.h5`: Original Keras model.
- `Theoretical.md`: Documentation for the IoT smart agriculture concept.

## How to Run
1.  **Model Training**: Open `Edge_AI.ipynb` in Jupyter/Colab to view the training process and evaluation.
2.  **IoT Concept**: Read `Theoretical.md` to understand the sensor network and AI integration design.