#!/usr/bin/env python3

import shutil
import psutil
import emails
import os
import sys
import socket

#Listing out the possible error cases and their corresponding error message
error_cases ={
"CPU": "Error - CPU usage is over 80%",
"Disk": "Error - Available disk space is less than 20%",
"Memory": "Error - Available memory is less than 500MB",
"Hostname": "Error - localhost cannot be resolved to 127.0.0.1"
}

#Check if the CPU utilization percentage is above 80
cpu_perc = ((psutil.cpu_percent(interval= 0.1)) > 80)

#Check if the Disk utilization percentage is above 80
disk_use = ((psutil.disk_usage('/').percent) > 80)

#Check if the Memory space available is less than 500MB
sys_mem = ((psutil.virtual_memory().available) < (500 * 1024 * 1024))

#Check if we are able to resolve the "localhost" hostname to the correct IP
resolve_host = ((socket.gethostbyname('localhost')) == '127.0.0.1')

#Check if any of the above conditions have failed.
#If so, fetch the appropriate error message.
if not cpu_perc:
    subject = error_cases["CPU"]
elif not disk_use:
    subject = error_cases["Disk"]
elif not sys_mem:
    subject = error_cases["Memory"]
elif not resolve_host:
    subject = error_cases["Hostname"]

#If all the conditions failed, the system is in good health.
#Report the same and stop execution.
#If not, call the "generate_email" function to send an email about the error.
if cpu_perc and disk_use and sys_mem and resolve_host:
    print("System is in good health")
    sys.exit(0)
else:
    print("System is not in good health")
    message = emails.generate_email(
    sender = "automation@example.com",
    recipient = "[username]@example.com",
    subject = subject,
    body = " Please check your system and resolve the issue as soon as possible."
    )
    emails.send_email(message)
