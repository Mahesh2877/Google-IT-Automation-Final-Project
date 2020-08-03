#!/usr/bin/env python3

import sys
import os
import requests
import reports
import emails


#Here, we receive the directory that contains the text description files
#We generate the body of the PDF to be sent.
#This PDF will contain the "Fruit name" and "Total weight"
def process_data(directory):
  summary = ""

#Open each file in the directory and read the first two lines["name", "weight"]
#Add the contents read to the "summary" variable
#We use the HTML break tag("<br/>") instead of "\n", because the generate_report()
#function works as a HTML reader.
  for filename in os.listdir(directory):
      with open(directory + '/' + filename, 'r') as f:
          line = f.readline()
          summary = summary + "name: " + line + '<br/>'
          line = f.readline()
          summary = summary + "weight: " + line + '<br/>' + '<br/>'
  print("Data generated\n")
  print("{}\n".format(summary))

#"summary" variable will hold the text string that will become the body of the PDF
  return summary

def main():
  print("Main method called\n")
  """Process the JSON data and generate a full report out of it."""
  summary = process_data("/home/[username]/supplier-data/descriptions")


#We call the "generate_report" function defined in the "reports.py" script
#The PDF will be generated in the "/tmp/processed.pdf" path.
  print("Sending the report to be generated\n")
  reports.generate_report(
  attachment = "/tmp/processed.pdf",
  title = "Processed Update on August 2nd 2020",
  paragraph = summary
  )


#We call the "generate_email" function defined in the "emails.py" script
#The PDF to be attached will be taken from the "/tmp/processed.pdf" path.
  print("Sending the email\n")
  message = emails.generate_email(
  sender = "automation@example.com",
  recipient = "[username]@example.com",
  subject = "Upload Completed - Online Fruit Store",
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
  attachment_path = "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == '__main__':
     main()
