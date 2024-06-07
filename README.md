# MNIST Digit Classification

This project focuses on classifying handwritten digits from the MNIST dataset using a neural network model. The project is implemented in Python using Flask for local deployment.

## Project Overview

The MNIST dataset is a well-known dataset consisting of 70,000 images of handwritten digits, each of size 28x28 pixels. This project aims to build a neural network model that can accurately classify these images into 10 digit classes (0-9).

## Model Architecture

The neural network model used in this project has the following architecture:
Input layer: Flattened 784-dimensional vector (28x28 images).
Hidden layers: Two dense layers with 128 units each and ReLU activation.
Dropout layer: 25% dropout rate for regularization.
Output layer: Dense layer with 10 units and softmax activation for classification.

## Training

The model is trained using the following parameters:

   Loss function: Sparse categorical crossentropy.
   Optimizer: Adam.
   Metrics: Accuracy.
   Epochs: 13.


## Local Deployment

To run the model locally, a Flask application is used. The application provides an interface where users can draw digits on a canvas and get predictions from the model. 

The Flask application consists of the following components:

  app.py: The main Flask application file that handles the server and prediction logic.

  index.html: The front-end HTML file with a canvas for drawing digits.

  mnist_draw.js: The JavaScript file to handle drawing on the canvas and sending the image data to the server for prediction.

## Prerequisites

  Python 3.x
  Flask
  NumPy
  Pillow
  Keras
  TensorFlow

## File Structure

  app.py: The main Flask application 
  file.templates/index.html: The HTML template for the web interface.
  static/mnist_draw.js: JavaScript file for handling the drawing and prediction logic.
  mnist_model.pkl: The trained neural network model.

## Usage

Open the application in your web browser.Draw a digit on the canvas.Click the "Predict" button to get the model's prediction.
