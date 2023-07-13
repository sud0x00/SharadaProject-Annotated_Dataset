Dataset generation

The characters to be extracted are annotated using labelme. The images and their respective json files are placed in a folder. Then the following steps can be followed to extract the images. 

Order of execution : 

1. Crop Script -> Annotated characters are cropped and placed in a folder 
2. Label 2 Folder -> The characters are moved into folders representing their labels
3. Label Operations -> It provides insight on the label folder (number of images , deletion of outliers)
4. Renaming the folders -> The characters are provided group numbers to avoid unicode encoding errors while training. The group numbers can be random or the following system can be used. 

poly_rect_crop.py => label2folder.py => label_operations.py => rename_folder.py

● All the characters starting with each of the 34 consonants क, ख, ग, घ , ... श, ष, स, ह, ळ will be
added into into 34 different groups. \
● Group 1 contains क, का, क, क, ..., कं, कः, and all compound letters that start with क are
included in this group. क्क , क्खी, क्या, क्ले, क्ली, क्षी, etc. all come in this group. \
● All Vowel letters - अ, आ, इ, ई, ... अं, अः, ॐ are placed in Group 34. \
● All punctuation marks are placed in Group 35. \
● All digits 0, 1, 2, ...9 and other numbers are placed in Group 36. \
● Group 37 is reserved for all the letters which do not belong to the previous groups. \

