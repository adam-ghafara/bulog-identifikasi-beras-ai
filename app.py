import base64
from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np
import io
import requests

app = Flask(__name__, template_folder='templates')

########################
#### 
#### LOAD MODEL
####
########################

# model_url='https://drive.google.com/uc?export=download&id=44ysaM2ldbSXfWNecUdj2iN_GMThHFS'
# model_loader = requests.get(model_url, stream=True)
# with open('./model/rice_model.h5', 'wb') as file:
#     for chunk in response.iter_content(1024):
#         if chunk:
#             file.write(chunk)

# Load The Model from the URL directory
# model_from_url = tf.keras.models.load_model(model_loader)

# step_1 = tf.keras.models.load_model('./model/rice_model.h5')
# step_2 = tf.keras.models.load_model('./model/rice_model.h5')
# step_3 = tf.keras.models.load_model('./model/rice_model.h5')

model = tf.keras.models.load_model('./model/rice_model.h5')

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
            img = Image.open(io.BytesIO(file.read()))
            # Preprocess the image
            preprocessed_image = image_loader(img, target=(256, 256))
            preprocessed_image = np.array(preprocessed_image, dtype='float32')
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
            model_accuracy = prediction[0][predicted_class] * 100
            return render_template('hasil-identifikasi.html', image=image_render, predicted_class=predicted_class, final_accuracy=model_accuracy)
    return render_template('identifikasi.html')

# Identify with 2 steps (Still in Development)
# @app.route('/identify', methods=['GET', 'POST'])
# def identify():
#     if request.method == 'POST':
#         file = request.files['image']
#         if file:
#             img = Image.open(io.BytesIO(file.read()))
#             # Preprocess the image
#             preprocessed_image = image_loader(img, target=(256, 256))
#             preprocessed_image = np.array(preprocessed_image, dtype='float32')
#             # Predict the image (Step 1)
#             prediction = step_1.predict(preprocessed_image)
#             # Step 1 Class
#             step_1_class = class_labels[np.argmax(prediction)]
#             # Step 1 Accuracy
#             step_1_accuracy = prediction[0][step_1_class] * 100
#             # Predict the image (Step 2)
#             prediction = step_2.predict(preprocessed_image)
#             # Step 2 Class
#             step_2_class = class_labels[np.argmax(prediction)]
#             # Step 2 Accuracy
#             step_2_accuracy = prediction[0][step_2_class] * 100
#             # Process the image to be displayed
#             img.seek(0)
#             image_stream = io.BytesIO()
#             img.save(image_stream, format='PNG')
#             image_render = image_stream.getvalue()
#             image_render = "data:image/png;base64," + base64.b64encode(image_render).decode('utf-8')
#             # Display to HTML
#             return render_template('hasil-identifikasi.html', image=image_render, step_1_prediction=step_1_class, step_1_accuracy=step_1_accuracy, step_2_prediction=step_2_class, step_2_accuracy=step_2_accuracy)
#     return render_template('identifikasi.html')

if __name__ == '__main__':
    app.run(debug=True)