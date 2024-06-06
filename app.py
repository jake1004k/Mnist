import numpy as np
import pickle
from flask import Flask, request, render_template, jsonify
from PIL import Image
import io
import base64

app = Flask(__name__)
model = pickle.load(open('mnist_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    img = Image.open(io.BytesIO(base64.b64decode(data.split(',')[1])))
    img = img.resize((28, 28)).convert('L')
    img = np.array(img)
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img)
    predicted_digit = np.argmax(prediction)
    
    return jsonify({'prediction': int(predicted_digit)})

if __name__ == "__main__":
    app.run(debug=True)
