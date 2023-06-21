from PIL import Image, ImageDraw, ImageOps
import json
import random
import string
import os
import numpy as np

# Folder path containing the images and annotation files

src_folder = 'E:/Dataset - temp/large'
dest_folder = 'E:/June/temp/temp'

# Iterate over the files in the folder
for file_name in os.listdir(src_folder):
    # Check if the file is an image
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        # Construct the full file paths for the image and annotation files
        image_file = os.path.join(src_folder, file_name)
        annotation_file = os.path.join(src_folder, f"{os.path.splitext(file_name)[0]}.json")
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
            shape_type = shape['shape_type']
            group_id = shape['group_id']
            label = shape['label']
            coordinates = shape['points']


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

            if label == '^':
                label = 'oth1'
            
            if label == "-":
                label == 'oth3' 

            # Generate a random string of length 15
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=15))


            # Create a new image with a transparent background
            cropped_image = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))

            # Create a draw object to draw the polygon on the new image
            draw = ImageDraw.Draw(cropped_image)

            # Convert the coordinates to integer tuples
            int_coordinates = [(int(point[0]), int(point[1])) for point in coordinates]

            # Draw the polygon on the new image
            draw.polygon(int_coordinates, fill=(255, 255, 255, 255))


            if shape_type == 'polygon':
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
                    new_filename = os.path.join(dest_folder, f"{label}_{random_string}.jpg")

                    # Save the rectangular image as JPEG
                    rectangular_image.save(new_filename, format='JPEG', quality=90)

            if shape_type == 'rectangle':
                # Find the minimum and maximum x, y coordinates
                x_coordinates = [point[0] for point in int_coordinates]
                y_coordinates = [point[1] for point in int_coordinates]

                left = min(x_coordinates)
                top = min(y_coordinates)
                right = max(x_coordinates)
                bottom = max(y_coordinates)

                # Crop the original image using the bounding box
                cropped_image = image.crop((left, top, right, bottom))

                # Create the new filename with group ID, label, and random string
                new_filename = os.path.join(dest_folder, f"{label}_{random_string}.jpg")

                # Save the cropped image
                cropped_image.save(new_filename, format='JPEG', quality=90)
