#! /usr/bin/env python3

import sys
import os
import requests

#Identifying the directory to read the text description files from
directory = '/home/[username]/supplier-data/descriptions'

#Initialize a dictionary which will temprarily store the text descriptions
#before uploading them to the url
data = {}

#Iterating through the files in the directory and adding their data into a dictionary
#The text file contains ["Name", "Weight", "Description"] each in a separate line.
#The url receives data in the format ["Name", "Weight", "Description", "Image Name"]

#We read the file line-by-line and add the read content to the appropriate key in the dictionary
#The "weight" data has to be converted into Integer type
#We also need to add "image_name" information into the dictionary, which is done by
#passing the text file's name as a JPEG format(the image and text file have the same name)
for filename in os.listdir(directory):
    with open(directory + '/' + filename, 'r') as f:
        line = f.readline()
        data["name"] = line.rstrip('\n')
        line = f.readline()
        data["weight"] = int(line.replace(" lbs", ""))
        line = f.readline()
        data["description"] = line.rstrip('\n')
        data["image_name"] = filename.replace(".txt", ".jpeg")

#For each of the text file we read, we cann post() to post/upload the data to the url
    print("Sending this dictionary to the server -\n{}\n".format(data))
    response = requests.post("http://[IP Address]/fruits/", json=data)

#raise_for_status() will call an error if the previous post() failed
    response.raise_for_status()
    print("Processed file {}\n".format(filename))

sys.exit(0)
