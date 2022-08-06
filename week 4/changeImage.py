#!/usr/bin/env python3

# The raw images from images subdirectory contains alpha transparency layers. So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. Use convert("RGB") method for converting RGBA to RGB image.

import os
import PIL
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
#Size: Change image resolution from 3000x2000 to 600x400 pixel
#Format: Change image format from .TIFF to .JPEG

for filename in os.listdir(os.path.join(os.path.dirname(__file__), "supplier-data/images")):
    if filename.endswith(".tiff"):
        file_path = os.path.join(os.path.dirname(__file__), "supplier-data/images/", filename)
        im = Image.open(file_path)
        im = im.convert("RGB")
        im.thumbnail((600, 400))
        im.save(file_path.replace(".tiff", ".jpeg"), "JPEG")
        print(filename)
