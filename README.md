# Plants Management

## Scope
The goal of this project is to develop a mobile app helping the management of indoor plants, with key features, such as watering reminders or diseases detection.

Four notebooks are associated to the development automation part of the app:
* A notebook to analyse the data for classification,
* A notebook to analyse the data for detection,
* A notebook to train and evaluate our image classification model,
* A notebook to train and evaluate our object detection model.

The notebooks will be updated progressively on this github repository.

## Working Environment
To achieve this project, we chose to use AWS. We used AWS s3 to store our raw data and AWS SageMaker to:
* Analyze and process our data,
* Train, fine tune and deploy our models.

## Data

To train our model, we used two datasets:
* PlantClef for classification (https://www.imageclef.org/lifeclef/2016/plant),
* PlantDoc for disease detection (https://public.roboflow.ai/object-detection/plantdoc).
