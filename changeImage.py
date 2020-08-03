#!/usr/bin/env python3
import os
import sys
from PIL import Image

#The directory from where we'll collect the images to be Processed
directory = '/home/[username]/supplier-data/images/'

#Iterate through the directory files, process the images and store them in the same directory
#The "processing" part includes -
#1). Resizing the image to (600 x 400) pixel
#2). Converting the image type to "RGB"
#3). Saving the images as ".jpeg" instead of the original ".tiff"
for filename in os.listdir(directory):
    if(".tiff" in filename):
         with open(directory + '/' + filename, 'r') as f:
             im = Image.open(fp = directory + '/' + filename)
             # Provide the target width and height of the image
             im_resized = im.resize(size = (600, 400))
             #Converting the image file to 'RGB'
             im_resized_convert = im_resized.convert("RGB")
             # Save the image in the right format
             im_resized_convert.save(fp = ("/home/[username]/supplier-data/images/" + filename.replace(".tiff", ".jpeg")))
sys.exit(0)
