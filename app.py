import base64
from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = Flask(__name__, template_folder='templates')

########################
#### 
#### LOAD MODEL
####
########################

# Load The Model from the URL directory
# model_url = 'https://drive.google.com/uc?export=download&id=1zpvntZFxBHfPFcfk_5qypF4Q5Anqe2dD'
# model = tf.keras.models.load_model(model_url)

# Load The Model Locally
model = tf.keras.models.load_model('../model/final_model_rice.h5')

class_labels = [0,1,2]

def image_loader(image, target):
    image = image.resize(target)
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

########################
#### 
#### RENDER FLASK PAGE
####
########################


# Landing Page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/identify-feedback')
def identify_feedback():
    return render_template('feedback.html')

# Identify page
@app.route('/identify', methods=['GET', 'POST'])
def identify():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            img = Image.open(io.BytesIO(file.read())).convert('RGB')
            # Preprocess the image
            preprocessed_image = image_loader(img, target=(256, 256))
            preprocessed_image = np.array(preprocessed_image) / 255.0
            # Predict the image
            prediction = model.predict(preprocessed_image)
            # Get class with highest probability
            predicted_class = class_labels[np.argmax(prediction)]
            # Display to HTML
            img.seek(0)
            image_stream = io.BytesIO()
            img.save(image_stream, format='PNG')
            image_render = image_stream.getvalue()
            image_render = "data:image/png;base64," + base64.b64encode(image_render).decode('utf-8')
            model_accuracy = np.max(prediction) * 100
            return render_template('hasil-identifikasi.html', image=image_render, predicted_class=predicted_class, final_accuracy=model_accuracy)
    return render_template('identifikasi.html')

if __name__ == '__main__':
    app.run(debug=False)