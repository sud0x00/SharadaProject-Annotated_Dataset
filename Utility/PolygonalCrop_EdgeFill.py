from PIL import Image, ImageDraw, ImageOps
import json
import random
import string
import os
import numpy as np

# Function to calculate the average color of the edge pixels
def calculate_average_color(image, factor):
    width, height = image.size
    edge_pixels = []
    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y))[3] != 0:  # Check if pixel is not transparent
                if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                    edge_pixels.append(image.getpixel((x, y)))
    average_color = tuple(np.mean(edge_pixels, axis=0, dtype=int))
    adjusted_color = tuple([int(channel/factor) for channel in average_color])
    return adjusted_color

# Folder path containing the images and annotation files
folder_path = 'E:/to edit/test'

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
                label = 'fs'

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

                # Calculate the average color of the edge pixels
                average_color = calculate_average_color(cropped_image,10)

                # Create a new rectangular image with the determined background color
                rectangular_image = Image.new("RGBA", (cropped_image.width, cropped_image.height), average_color)
                rectangular_image.paste(cropped_image, (0, 0), cropped_image)

                # Create the new filename with group ID, label, and random string
                new_filename = os.path.join("E:/to edit/test/temp1", f"{label}_{random_string}.jpg")

                # Save the rectangular image
                rectangular_image.save(new_filename, format='JPG')
