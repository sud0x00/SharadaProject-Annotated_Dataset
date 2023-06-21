import cv2
import numpy as np
import os

# Folder path containing the images
folder_path = 'E:/Dataset - dump/gds/129'

# Output folder to save the processed images
output_folder = 'E:/Dataset - dump/temp'

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Construct the full file path
        image_path = os.path.join(folder_path, filename)

        # Read the image using OpenCV
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Thresholding / Binarization
        ret, imgf = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        # Resize the image to a consistent size using OpenCV
        resized_image = cv2.resize(imgf, (32, 32))

        # Save the processed image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_image)

# Continue with your further processing or model training
