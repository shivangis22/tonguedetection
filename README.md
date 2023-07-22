# TongueDiseaseNet - A Deep Learning Solution for Tongue Disease Detection and Diagnosis
TongueDiseaseNet is an innovative and advanced deep-learning project that aims to revolutionize the diagnosis of various tongue diseases using tongue images. Leveraging the power of machine learning and artificial intelligence, this project offers a reliable and efficient tool to detect and identify oral lichens, leukaemia, hairy tongue, oral cancer, and oral thrush.

## Table of Contents
[Introduction] (Introduction)
[Dataset] (Dataset)
[Deep Learning model] (Deep learning model)
[API] ( ### API)
[Web Application] (Web Application)
[Key Features] (Key Features)
[Impact] (Impact)

## Introduction
TongueDiseaseNet is dedicated to advancing the diagnosis of tongue diseases through the application of cutting-edge deep-learning techniques. By utilizing a comprehensive and diverse dataset of tongue images, the project's aim is to achieve accurate disease classification and offer valuable insights to healthcare professionals and individuals.

## Dataset
To ensure the quality and diversity of data, the TongueDiseaseNet team collected thousands of tongue images from various sources using web scraping techniques. This unique and curated dataset forms the foundation on which the entire system is built, facilitating accurate and reliable disease identification.

## Deep Learning Model
The core of TongueDiseaseNet is a robust deep-learning model developed using the TensorFlow Keras library. After undergoing rigorous training on the prepared dataset, the model can achieve an impressive accuracy rate of 90 per cent in disease classification. This high accuracy ensures trustworthy predictions, supporting healthcare professionals in making well-informed decisions.

## API
TongueDiseaseNet offers a fast and responsive API powered by FastAPI. The API serves as the core interface, allowing users to submit tongue images in JPG format for analysis. The model processes the input image and generates detailed insights into the detected disease, including the confidence of the prediction and recommended treatment options, along with information about symptoms and causes.

## Web Application
For easy and seamless interaction with the application, the TongueDiseaseNet team has developed a user-friendly Flask web application. Within this web application, users can effortlessly upload their tongue images, obtain the predicted results, and explore valuable information provided about the identified disease.

### Homepage

![Screenshot (259)](https://github.com/shivangis22/tonguedetection/assets/71970506/9131b358-7c28-4097-a4ea-31bde86c0289)

### Uploading image

![Screenshot (261)](https://github.com/shivangis22/tonguedetection/assets/71970506/9ef31c02-6627-4a3f-82e2-66284b63171f)

### Result of prediction

![Screenshot (262)](https://github.com/shivangis22/tonguedetection/assets/71970506/037d237c-3ab5-476e-8aad-9567bbf965e0)

## Installation and setup
Pull the contents of the repository and install the required libraries using the command 
```
pip install -r /path/to/requirements.txt
```

## Key Features
* Disease Detection: The model accurately classifies tongue images to identify various diseases such as oral lichens, leukaemia, hairy tongue, oral cancer, and oral thrush.
* High Accuracy: With a precision of 90 percent, TongueDiseaseNet provides reliable and trustworthy predictions, aiding healthcare professionals in making well-informed decisions.
* Informative Results: Along with the predicted disease, the system presents the confidence level of the diagnosis and offers in-depth details about the disease, including symptoms, causes, and potential treatments.
* User-Friendly Interface: The Flask web application allows users to effortlessly upload tongue images and receive rapid results without the need for complex technical expertise.

## Impact
TongueDiseaseNet holds the potential to significantly enhance the speed and accuracy of tongue disease diagnosis, enabling early detection and proactive treatment. With its state-of-the-art technology and accessible interface, this project is poised to make a positive impact on healthcare and improve the lives of countless individuals affected by tongue diseases. The system's reliable predictions and informative insights empower healthcare professionals to take timely and appropriate actions, ultimately leading to better patient outcomes.

## Future Scope
The future scope of the TongueDiseaseNet project is promising and opens up new possibilities in the field of medical diagnosis. By enhancing the dataset and gathering data from local hospitals and health centers, the deep-learning model can be trained to predict an even broader range of tongue diseases with higher accuracy. The inclusion of diverse data from various geographical locations and demographics will improve the system's ability to identify rare and region-specific tongue diseases, making it more comprehensive and globally applicable. Furthermore, as the dataset grows, the model can be fine-tuned to detect early-stage and less common tongue diseases, contributing to earlier interventions and better patient outcomes. The potential integration of medical records and patient history with tongue images could also pave the way for a more personalized and precise diagnostic approach. With continuous research and development, TongueDiseaseNet has the capacity to become an indispensable tool for healthcare professionals, significantly improving tongue disease diagnosis and treatment worldwide.


