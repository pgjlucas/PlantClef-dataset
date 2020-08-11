# Plants Management

## Scope
The goal of this project is to develop a mobile app helping the management of indoor plants, with key features, such as watering reminders or diseases detection.

Four notebooks are associated to the automation part of the app:
* A notebook to analyse the data for classification (Analysis_Classif.ipynb),
* A notebook to analyse the data for detection (Analysis_Detect.ipynb),
* A notebook to train and evaluate our image classification model (Classification.ipynb),
* A notebook to train and evaluate our object detection model (Detection.ipynb).

The notebooks will be uploaded and updated progressively on this github repository.

## Working Environment
To achieve this project, we chose to use AWS SageMaker to:
* Analyze and process our data,
* Train, fine tune and deploy our models.

## Data
To train our model, we used two datasets:
* PlantClef for classification (https://www.imageclef.org/lifeclef/2016/plant),
* PlantDoc for disease detection (https://public.roboflow.ai/object-detection/plantdoc).
