from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import json

app= FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
     print(disease_con)


    

@app.get("/home")
async def main():

    return "Hello, world!"

def read_file_as_image(data)-> np.ndarray:
    image = Image.open(BytesIO(data))
    image= image.resize((256, 256)).convert("RGB")
    image= np.array(image)
    return image

@app.post("/predict")
async def predict( file: UploadFile):
    global disease_dictionary
    image= read_file_as_image(await file.read())
    
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
            #  print(disease_dictionary)

             

   
       
    return {
        'class': predicted_class,
        'confidence': float(confidence),
        'disease_data': disease_dictionary
        
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
    

