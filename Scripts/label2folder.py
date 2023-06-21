import os
import shutil

# Path to the folder containing the files
folder_path = 'E:/June/temp/temp'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Iterate over each file
for file_name in files:
    if os.path.isfile(os.path.join(folder_path, file_name)):
        # Split the file name into label and random string
        label, random_string = file_name.split('_', 1)
        
        # Create the destination folder path
        destination_folder = os.path.join(folder_path, label)
        
        # Check if the destination folder exists, otherwise create it
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Move the file to the destination folder
        shutil.move(os.path.join(folder_path, file_name), os.path.join(destination_folder, file_name))

print("Files moved successfully!")