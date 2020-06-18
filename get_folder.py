# Change dataset structure to make it usable on Drive & Colab
import os
import shutil
import xml.etree.ElementTree as ET
import csv
import pandas as pd
import sys

# Get arguments
# dataset_path = '/Users/Pierre/Documents/Plants_App/Dataset/PlantClef/train'


def get_dataframe(dataset_path):

	# Initiate dataframe & list
	columns_name = ['ObservationId', 'MediaId', 'Vote', 'Content', 'ClassId', 'Family', 'Genus', 'Species', 'Author', 'Date', 'Location', 'Latitude', 'Longitude', 'YearInCLEF','ObservationId2014', 'ImageId2014', 'LearnTag']
	data = []

	# Go through all xml files
	for xml_file in os.listdir(dataset_path):
		# Select xml files
		if xml_file[-3:] == 'xml':
			xml_file  = os.path.join(dataset_path,xml_file)
			# Parse xml files
			tree = ET.parse(xml_file)
			root = tree.getroot()
			columns = [child.text for child in root]
			data.append(columns)

	df = pd.DataFrame(data = data, columns = columns_name)

	return df

def main(dataset_path):
	# Constants
	csv_file = os.path.join(dataset_path,os.path.basename(dataset_path + '.csv'))
	
	# Create label dataframe from xml files
	df = get_dataframe (dataset_path)

	# Save csv
	df.to_csv (csv_file, index = False, header=True)

	labels_path = dataset_path + '/labels/'
	images_path = dataset_path + '/images/'

	# Create new dataset folder
	os.mkdir(labels_path)
	os.mkdir(images_path)

	# Create folders for each class and move images into them
	for mediaId, classId in zip(df["MediaId"], df["ClassId"]):
		# Get xml file and image file paths
		xmlFile  = os.path.join(dataset_path,(str(mediaId) + '.xml'))
		imgFile = xmlFile[:-3] + 'jpg'

		# Get new folders paths
		imgClassFolderPath = images_path + classId
		labelClassFolderPath = labels_path + classId

		# Create class folder if doesn't already exist
		if not os.path.isdir(imgClassFolderPath):
			os.mkdir(imgClassFolderPath)
		if not os.path.isdir(labelClassFolderPath):
			os.mkdir(labelClassFolderPath)
		
		# Move xmlFile and imgFile if both exist
		if os.path.isfile(imgFile) and os.path.isfile(xmlFile):
			shutil.move(xmlFile, labelClassFolderPath)
			shutil.move(imgFile, imgClassFolderPath)

if __name__ == "__main__":
    main(sys.argv[1])

	


