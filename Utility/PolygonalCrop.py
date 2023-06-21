from PIL import Image, ImageDraw, ImageOps
import json
import random
import string
import os
import numpy as np


# Folder path containing the images and annotation files
folder_path = 'D:/nlp sanskrit project/June/13.6.23/to check/temp'

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Construct the full file paths for the image and annotation files
        image_file = os.path.join(folder_path, filename)
        annotation_file = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.json")

        # Load the annotation file
        with open(annotation_file, 'r', encoding='utf-8') as f:
            annotation = json.load(f)

        # Get the image dimensions
        image_height = annotation['imageHeight']
        image_width = annotation['imageWidth']

        # Open the original image
        image = Image.open(image_file)

        # Loop through each shape in the annotation
        for shape in annotation['shapes']:
            # Extract the group ID and label
            group_id = shape['group_id']
            label = shape['label']

            # Check if label is equal to "||" and change it to ".."
            if label == '||':
                label = 'fs2'

            if label == '|':
                label = 'fs1'
            
            if label == '|| || ||':
                label = 'fs3'

            if label == '?':
                label = 'unk'

            if label == '.':
                label = 'period'


            # Generate a random string of length 10
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            # Extract the coordinates for the shape
            coordinates = shape['points']

            # Create a new image with a transparent background
            cropped_image = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))

            # Create a draw object to draw the polygon on the new image
            draw = ImageDraw.Draw(cropped_image)

            # Convert the coordinates to integer tuples
            int_coordinates = [(int(point[0]), int(point[1])) for point in coordinates]

            # Draw the polygon on the new image
            draw.polygon(int_coordinates, fill=(255, 255, 255, 255))

            # Create a mask from the drawn polygon
            mask = ImageOps.invert(cropped_image.convert('L'))

            # Apply the mask to the original image
            masked_image = Image.new("RGBA", image.size)
            masked_image.paste(image, (0, 0), mask=cropped_image)

            # Find the bounding box of the polygon
            bbox = masked_image.getbbox()

            # Crop the masked image using the bounding box
            if bbox:
                cropped_image = masked_image.crop(bbox)

                # Create a new rectangular image with the determined background color
                rectangular_image = Image.new("RGB", (cropped_image.width, cropped_image.height), (255, 255, 255))
                rectangular_image.paste(cropped_image, (0, 0), cropped_image)

                # Create the new filename with group ID, label, and random string
                new_filename = os.path.join("D:/nlp sanskrit project/June/13.6.23/to check/temp10", f"{label}_{random_string}.jpg")

                # Save the rectangular image as JPEG
                rectangular_image.save(new_filename, format='JPEG', quality=90)
