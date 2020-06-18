# Plants Classification
To train our model, it is necessary to change its structure to make it work on Colab. Indeed, the original dataset folder for training contains more than 180 000 images and xml files which creates timeout issues.

To organize the dataset, use the following script:
* get_folder : Creates subfolders for each class
