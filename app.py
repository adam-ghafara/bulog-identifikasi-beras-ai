import base64
from flask import Flask, request, render_template
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = Flask(__name__, template_folder='templates')

########################
#### 
#### LOAD MODEL
####
########################
model = load_model('./model/rice_model.h5')

class_labels = [0,1,2]

def image_loader(image, target):
    image = image.resize(target)
    image = img_to_array(image)
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

if __name__ == '__main__':
    app.run(debug=True)