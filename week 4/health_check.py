#!/usr/bin/env python3

#will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

# Report an error if CPU usage is over 80%
# Report an error if available disk space is lower than 20%
# Report an error if available memory is less than 500MB
# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

# Import the necessary Python libraries (eg. shutil, psutil) to write this script.

# Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:

#From: automation@example.com
# To: username@example.com
# Replace username with the username given in the Connection Details Panel on the right hand side.
# Subject line:
# Case

# Subject line

# CPU usage is over 80%

# Error - CPU usage is over 80%

# Available disk space is lower than 20%

# Error - Available disk space is less than 20%

# available memory is less than 500MB

# Error - Available memory is less than 500MB

# hostname "localhost" cannot be resolved to "127.0.0.1"

# Error - localhost cannot be resolved to 127.0.0.1

# E-mail Body: Please check your system and resolve the issue as soon as possible.

import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import datetime
import platform
import socket
import subprocess
import sys
import getpass
import re
import shutil


def send_email(email_address, email_body):
    print("Sending email to: " + email_address, email_body)
    """Sends an email to the specified address."""
    # Create a text/plain message
    msg = MIMEText("Please check your system and resolve the issue as soon as possible")
    msg['Subject'] = email_body
    msg['From'] = "automation@example.com"
    msg['To'] = email_address
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()

#Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above

email_address = "student-03-d83a24ce04f1@example.com"
# Check CPU usage
cpu_usage = psutil.cpu_percent()
if cpu_usage > 80:
    email_body = "Error - CPU usage is over 80%"
    send_email(email_address, email_body)
# Check disk usage
disk_usage = psutil.disk_usage('/')
if disk_usage.percent > 20:
    email_body = "Error - Available disk space is less than 20%"
    send_email(email_address, email_body)
# Check memory usage
memory_usage = psutil.virtual_memory()
if memory_usage.available < 500000:
    email_body = "Error - Available memory is less than 500MB"
    send_email(email_address, email_body)
#hostname "localhost" cannot be resolved to "127.0.0.1"
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
if ip_address != "127.0.0.1":
    email_body = "Error - localhost cannot be resolved to 127.0.0.1"
    send_email(email_address, email_body)
    
    
