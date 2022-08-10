#! /usr/bin/env python3

import os
import requests

#List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.

# Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.

# you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.

# Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.

# Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.

# If the request is successful, print a success message.


#! /usr/bin/env python3
import os
import requests

#List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
feedback_files = os.listdir("/data/feedback")
for feedback_file in feedback_files:
    if feedback_file.endswith('.txt'):
        file_path = os.path.join("/data/feedback/", feedback_file)
        print(file_path)
        with open(file_path, 'r') as f:
            feedback = f.read()
            print(feedback)
        # you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
        #Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
        splitted_feedback = feedback.split("\n")
        data = {
            "title": splitted_feedback[0],
            "name": splitted_feedback[1],
            "date": splitted_feedback[2],
            "feedback": splitted_feedback[3]
        }
        print(data)
        # Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.
        response = requests.post('http://34.69.129.218/feedback/', data=data)
        # Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
        if response.status_code == 201:
            print('Successfully uploaded feedback to the website!')
        else:
            print('Error uploading feedback to the website!')
            print(response.text)
            print(response.status_code)
            break