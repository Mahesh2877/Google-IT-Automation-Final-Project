#!/usr/bin/env python3
import requests
import os
import sys

#Identify the directory from which to read the images to be uploaded
directory = '/home/[username]/supplier-data/images/'

#Identify the URL to which we have to upload the images.
#Make sure to end the url with a forward slash
url = "http://[IP Address]/upload/"

#Iterate through the directory, identify the ".jpeg" images, and upload them to the url
for filename in os.listdir(directory):
    if(".jpeg" in filename):
        with open(directory + '/' + filename, 'rb') as opened:
            r = requests.post(url, files = {'file': opened})

sys.exit(0)
