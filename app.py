import numpy as np
import pickle
from flask import Flask, request, render_template, jsonify
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load the model
model = pickle.load(open('mnist_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['image']
        
        img = Image.open(io.BytesIO(base64.b64decode(data.split(',')[1])))
        
        img = img.resize((28, 28)).convert('L')
        
        img = np.array(img)
        
        img = img / 255.0
        
        img = img.flatten().reshape(1, 784)

        
        print("Processed image shape:", img.shape)
        print("Processed image array:", img)

        
        prediction = model.predict(img)
        predicted_digit = np.argmax(prediction)
        
        
        print(f"Prediction: {predicted_digit}")

        return jsonify({'prediction': int(predicted_digit)})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True,port=5001)
