import os
import numpy as np
import pandas as pd
from PIL import Image
import pickle

# Path to the main folder containing subfolders with images
main_folder = 'C:/NLP Sanskrit/temp2/TEMP'

# Dictionary mapping folder names to corresponding values
value_dict={'1': '-', '2': 'fs', '3': 'a', '4': 'RRi', '5': 'e', '6': 'ka', '7': 'kRRi', '8': 'kShi', '9': 'ga', '10': 'gA', '11': 'gI', '12': 'ge', '13': 'go', '14': 'gre', '15': 'ghna', '16': 'ghne', '17': '~Nkho', '18': 'cha', '19': 'chyA', '20': 'ja', '21': 'NaH', '22': 'NA', '23': 'ta', '24': 'tA', '25': 'ti', '26': 'tI', '27': 'tmA', '28': 'tre', '29': 'tvA', '30': 'da', '31': 'dI', '32': 'dRRi', '33': 'de', '34': 'dda', '35': 'dma', '36': 'dvi', '37': 'dhi', '38': 'dhiM', '39': 'na', '40': 'naH', '41': 'nA', '42': 'nu', '43': 'ntA', '44': 'ntra', '45': 'ndaH', '46': 'ndi', '47': 'nmau', '48': 'nva', '49': 'nve', '50': 'nsiM', '51': 'pa', '52': 'pA', '53': 'pI', '54': 'pu', '55': 'pU', '56': 'pCha', '57': 'bha', '58': 'bhA', '59': 'bhe', '60': 'bhra', '61': 'ma', '62': 'maH', '63': 'mA', '64': 'me', '65': 'mo', '66': 'm', '67': 'ya', '68': 'yA', '69': 'yu', '70': 'ye', '71': 'ra', '72': 'raH', '73': 'rA', '74': 'rNa', '75': 'rtre', '76': 'rma', '77': 'la', '78': 'lA', '79': 'li', '80': 'le', '81': 'lya', '82': 'va', '83': 'vA', '84': 'vAM', '85': 'vi', '86': 'vI', '87': 'vyA', '88': 'sha', '89': 'shu', '90': 'shU', '91': 'shRRi', '92': 'sho', '93': 'shyA', '94': 'shrI', '95': 'shva', '96': 'Sha', '97': 'ShiH', '98': 'Shu', '99': 'Shka', '100': 'ShTu', '101': 'ShNAH', '102': 'sa', '103': 'stvaM', '104': 'sya', '105': 'ha', '106': 'hi', '107': 'OM', '108': '1'}

# Initialize lists to store data for each column
image_array_list = []
folder_name_list = []
value_list = []

# Iterate over subfolders and images
for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)
    if os.path.isdir(folder_path):
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            if image_name.endswith('.jpg') or image_name.endswith('.png'):  # Adjust file extensions as needed
                # Read the image as a numpy array
                image_array = np.array(Image.open(image_path))
                image_array_list.append(image_array)
                folder_name_list.append(folder_name)
                value_list.append(value_dict.get(folder_name))

# Create the dataframe
data = {
    'Image Array': image_array_list,
    'Folder Name': folder_name_list,
    'Value': value_list
}

df = pd.DataFrame(data)
output_file = "C:/NLP Sanskrit/temp2/dataframe.p"
with open(output_file, 'wb') as file:
    pickle.dump(df, file)

print("DataFrame saved as .p file successfully.")
