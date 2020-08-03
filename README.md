# IT Automation Coursera Certificate Final Project
This is the code I wrote for the final test of the "IT Automation with Python" specialization on coursera.org, offered by Google.
Link to specialization - https://www.coursera.org/professional-certificates/google-it-automation;

## Problem Statement
We are an online fruit store owner. Our supplier has sent us a list of fruits and their weights that they have supplied to us.\
The exact information shared is in (image, text) format. An image of the fruit, followed by its text description.\
We need to upload this information onto your official website so our customers can see the updated inventory for purchase.\
Once the website is updated, we will also need to send an email to our supplier attaching a report of the final list of fruits and their weight for confirmation.\
We will also need to continuously monitor the health of the system in parallel and generate an email if the system is in poor health.

## Detailed Solution
### Processing the images
We first write "changeImage.py". This script receives the image files and processes them to be in a format that can be uploaded onto our website.\
The images are sent in a large size, with a ".tiff" extension.\
For the website - the ideal size for the images is (600 by 400) pixels and the ideal format is JPEG.\
This script essentially converts the images to these standards and saves them in the same directory.\
At the end of this script, the directory will have two copies of the images - the original format and the processed format.

### Uploading the images
We then write "supplier_image_upload.py". This script essentially, uploads the image files to the website using the post() method of requests module.\
We use "os.listdir()" to iterate through the image files we processed in the above step.\
Since this directory now contains two versions of the same image(same name, different extension), we only upload the image file if it ends with the right ".jpeg" extension.\
Once this is executed, our websites directory will store the image files but not display them.

### Uploading the text description
We then write "run.py". Here, we upload the text description of each fruit.\
The description and of each fruit is given in a separate file, maintaining the same name as the image file but with a ".txt" description.\
We iterate through these files, reading them line by line. Each file contains three lines - ["Fruit name", "Total Weight", "Description"]. \
We add each line to a temporary dictionary which will be uploaded to the website. The dictionary will also contain a fourth element, the name of the corresponding image file.\
Since the image files are already stored in the website directory, we simply need to attach the ".jpeg" filename to each fruits description.\
Uploading this dictionary to the website will enable the website to add all the dictionary's contents - ["Name", "Weight", "Description", "Image"] to it's document.\
Once this script is run, users will be able to view the updated inventory on our website.

### Sending the report email
We then write three more files - "reports.py", "emails.py" and "report_email.py".\
The latter will import and call the former two files.\
In "report_email.py", we prepare the summary paragraph that will be written in the PDF report to be sent.\
We then, call the "reports.py" file and pass this summary paragraph along with information on the PDF's title, the pathname where we want the PDF to be generated, etc.\
The "reports.py" file will then accept these information, create the PDF for us and store it in the proposed pathname. It will not return anything to the calling function.\
Once control is sent back to "report_email.py", we then call "emails.py" to send the actual email to the supplier. We add information on the recipient email address, subject and body of the email and the attachment file to be added.\
The "emails.py" file accepts these information, and sends the email for us.

### Health Check
Finally, we write "health_check.py".\
Here, we have to cehck for four things - \
1). CPU utlization going over 80%\
2). Disk space usage going over 80%\
3). Memory available going under 500MB \
4). Hostname "localhost" being successfully resolved to the correct IP address\
\
We import the necessary libraries to perform these checks.\
We call the necessary functions to perform these checks and store the result as a boolean value.\
We check each of the four boolean values, if they are all correct the system is in a healthy state and we need not do anything.\
If even one of the conditions fail, we need to send an email to ourselves with information on which of the conditions failed.\
For this, we again use the "emails.py" file, sending the necessary informtaion like subject line and body of the email. Note that here, there is no need to attach any file.
