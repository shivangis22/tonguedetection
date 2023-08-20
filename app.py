from flask import Flask, render_template, request
import numpy as np
import io

from io import BytesIO
from PIL import Image
import tensorflow as tf
import json


from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
#from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50

app = Flask(__name__)

MODEL= tf.keras.models.load_model(r".\saved_model\1")
CLASS_NAMES= ['hairytonguedataset',
 'healthytonguedataset',
 'leokoplakiatonguedataset',
 'oralcancerdataset',
 'orallichensdataset',
 'oralthrushdataset']

disease_dictionary= dict()

with open(r".\saved_model\details.json", 'r') as source_file:
    CONDITION_DATA = json.load(source_file)
    if 'disease_condition' in CONDITION_DATA:
     disease_con= CONDITION_DATA['disease_condition']


@app.route('/', methods=['GET'])
def hello_word():
    return render_template('index.html')

def read_file_as_image(data)-> np.ndarray:
    image = Image.open(BytesIO(data))
    image= image.resize((256, 256)).convert("RGB")
    image= np.array(image)
    return image


@app.route('/', methods=['POST'])
def predict():
    image= request.files['imagefile']
    image= Image.open(image) 
    with io.BytesIO() as buf:
       image.save(buf, 'jpeg')
       image = buf.getvalue()
    

    global disease_dictionary
    image= read_file_as_image(image)
    
    img_batch= np.expand_dims(image,0)

    
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    for i in disease_con:
        if 'predicted_class' in i:
            condition_name = i['predicted_class']
            disease= i['condition']
            description = i['description']
            symptoms= i['symptoms']
            causes= i['causes']
            treatments= i['treatment']
            if (condition_name== predicted_class):

            
             disease_dictionary = {
                "Disease": disease,
                "Description": description,
                "Symptoms": symptoms,
                "Causes": causes,
                "Treatments": treatments
             }


    return render_template('index.html', prediction=disease_dictionary.get("Disease"), description= disease_dictionary.get("Description"), symptoms= disease_dictionary.get("Symptoms"), causes= disease_dictionary.get("Causes"), treatment= disease_dictionary.get("Treatments") , confidence= confidence )


if __name__ == '__main__':
    app.run(debug=True)