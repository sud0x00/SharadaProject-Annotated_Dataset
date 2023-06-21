# Install poppler: conda install -c conda-forge poppler
# Install pdf2image: pip install pdf2image

import os
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert PDF to images
    pages = convert_from_path(pdf_path)
    
    # Save each page as an image
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f"{filename}_page_{i+1}.png")
        page.save(image_path, "PNG")

def convert_folder_to_images(input_folder, output_folder):
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(".pdf"):
            convert_pdf_to_images(file_path, output_folder)

# Usage example
input__folder = "D:/nlp sanskrit project/test/For OCR - Hard"
output_folder = "D:/nlp sanskrit project/test/test output"

convert_folder_to_images(input__folder, output_folder)
