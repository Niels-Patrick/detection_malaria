from flask import Blueprint, jsonify, render_template, request, redirect, url_for, current_app
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from config import Config

# Defining a Blueprint for the main routes
main = Blueprint("main", __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/malaria_form', methods=['POST'])
def malaria_form():
    '''
    Predicts whether a cell is infected by the Malaria or not.

    return: a jsonify message with the predicted status
    '''
    try:
        # Fetching data from the form
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']

        if file.filename == "":
            return "No selected file", 400
        filepath = os.path.join(Config.UPLOAD_FOLDER, file.filename)
        file.save(filepath) # Saving the file to the uploads folder

        target_size = (128, 128) # To change the uploaded picture size and adapt it to the model

        # Processing the image
        image = load_img(filepath, target_size=target_size) # Resizing to model input size
        image_array = img_to_array(image) / 255.0 # Converting to array and normalizing
        image_array = np.expand_dims(image_array, axis=0) # Adding batch dimension

        # Predicting the cell status
        model = current_app.model
        prediction = model.predict(image_array)[0][0]
        percentage = prediction * 100
        confidence = percentage if prediction > 0.5 else 100 - percentage
        prediction = (prediction > 0.5).astype(int)

        if prediction == 0:
            prediction = "Parasited"
        else:
            prediction = "Uninfected"

        # The message and prediction result to display under the upload form
        response_message = f"Status : {prediction}, Certitude : {confidence}"
        # Returning the message as JSON
        return jsonify({'message': response_message}), 200
            
    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'message': str(e)}), 500
