# Flask Web Render
import base64
from flask import Flask, render_template
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

# Load the model
model = load_model('model.h5')

class_labels = [0,1,2]

def image_loader(image, target):
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

# Web Render

# Landing Page
@app.route('/')
def index():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Identify page
@app.route('/identify', methods=['GET', 'POST'])
def identify():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # PIL Image
            img = Image.open(file)
            # Image Preprocessing
            preprocessing = prepare_image(img, target=(256, 256))
            # Class Prediction
            predict = model.predict(preprocessing)
            # Get the class label
            predict_label = class_labels[np.argmax(predict)]
            # Convert image for display in html
            img.seek(0)
            image_data = io.BytesIO()
            img.save(image_data, format='PNG')
            image_data = image_data.getvalue()
            img_data = "data:image/png;base64," + base64.b64encode(image_data).decode('utf-8')
            model_accuracy = np.max(predict) * 100
            return render_template('identify.html', img_data=img_data, predict_label=predict_label, model_accuracy=model_accuracy)
    return render_template('identify.html')

if __name__ == '__main__':
    app.run(debug=True)