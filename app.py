import os
import numpy as np
from PIL import Image
import cv2
import json
import datetime

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from keras.models import load_model

app = Flask(__name__)

# Load the trained model
model = load_model('my_model.keras')
print('✅ Model loaded. Check http://127.0.0.1:5000/')

# Upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def getResult(img_path):
    image = cv2.imread(img_path)
    if image is None:
        raise ValueError(f"Could not read image at path: {img_path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image).resize((64, 64))
    img = np.array(img).astype('float32') / 255.0
    input_img = np.expand_dims(img, axis=0)

    predictions = model.predict(input_img)
    tumor_probability = predictions[0][1] * 100
    binary_result = "Yes" if tumor_probability >= 30 else "No"

    return tumor_probability, binary_result

def save_history(image_name, prediction, probability):
    record = {
        "timestamp": datetime.datetime.now().isoformat(),
        "image": image_name,
        "prediction": prediction,
        "probability": f"{probability:.2f}%"
    }
    with open('history.json', 'a') as f:
        f.write(json.dumps(record) + "\n")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def upload():
    try:
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(file_path)

        tumor_probability, binary_result = getResult(file_path)
        save_history(filename, binary_result, tumor_probability)

        result = (
            f"The probability of tumor presence is: {tumor_probability:.2f}%<br>"
            f"Tumor presence: <strong>{binary_result}</strong>"
        )

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
