import os
from PIL import Image
import logging

def convert_directory_to_jpg(directory_path):
    """
    Converts all PNG images in the specified directory to JPG format,
    saves them in a subfolder named 'Converted' within the same directory,
    and maintains the original PNG files.
    """
    converted_dir = os.path.join(directory_path, 'Converted')
    os.makedirs(converted_dir, exist_ok=True)

    for filename in os.listdir(directory_path):
        if filename.endswith(".png"):
            try:
                original_path = os.path.join(directory_path, filename)
                image = Image.open(original_path)
                rgb_im = image.convert('RGB')
                basename, _ = os.path.splitext(filename)
                jpg_filename = basename + '.jpg'
                save_path = os.path.join(converted_dir, jpg_filename)
                rgb_im.save(save_path, quality=85)
                logging.info(f'Successfully converted {filename} to JPG format.')
            except Exception as e:
                logging.error(f'Error converting {filename} to JPG format: {e}', exc_info=True)

    logging.info("All PNG files have been converted to JPG format.")