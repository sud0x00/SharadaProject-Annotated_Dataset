import os
SOURCE_DIR = "temp"

# Step 1: Read the names of all folders
folder_names = os.listdir(SOURCE_DIR)  # Assuming the program is executed in the directory containing the folders

# Step 2: Create a dictionary with folder names and corresponding values
folder_dict = {}
for i, folder_name in enumerate(folder_names):
    folder_dict[folder_name] = i + 1

# Step 3: Rename files inside folders
for folder_name, value in folder_dict.items():
    folder_path = os.path.join(SOURCE_DIR, folder_name)
    files = os.listdir(folder_path)
    for file_name in files:
        if file_name.startswith(folder_name):
            new_file_name = f'{value}_{file_name.split("_", 1)[1]}'  # Extract the random string after the underscore
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)

# Step 4: Rename folders
for folder_name, value in folder_dict.items():
    old_folder_path = os.path.join(SOURCE_DIR, folder_name)
    new_folder_path = os.path.join(SOURCE_DIR, str(value))
    os.rename(old_folder_path, new_folder_path)
