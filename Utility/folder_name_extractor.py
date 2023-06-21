# -*- coding: utf-8 -*-
import os

def extract_subfolder_names(file_path, main_folder_path):
    subfolder_names = []
    for root, dirs, files in os.walk(main_folder_path):
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            subfolder_names.append(folder_path)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for subfolder_name in subfolder_names:
            file.write(subfolder_name + '\n')

# Example usage:
file_path = 'C:/NLP Sanskrit/temp2/file2.txt'
main_folder_path = 'E:/Dataset - temp/large'
extract_subfolder_names(file_path, main_folder_path)
