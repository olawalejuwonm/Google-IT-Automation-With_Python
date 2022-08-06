#! /usr/bin/env python3

import os
import requests

#you'll have to process the .txt files (named 001.txt, 002.txt, ...) in the supplier-data/descriptions/ directory and save them in a data structure so that you can then upload them via JSON. Note that all files are written in the following format, with each piece of information on its own line:

# name
# weight (in lbs)
# description

#he data model in the Django application fruit has the following fields: name, weight, description and image_name. The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

#The final JSON object should be similar to:
#{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}

#Iterate over all the fruits and use post method from Python requests library to upload all the data to the URL http://[linux-instance-external-IP]/fruits

for filename in os.listdir(os.path.join(os.path.dirname(__file__), "supplier-data/descriptions")):
    if filename.endswith(".txt"):
        file_path = os.path.join(os.path.dirname(__file__), "supplier-data/descriptions/", filename)
        with open(file_path, 'r') as opened:
            data = opened.readlines()
            name = data[0].strip()
            weight = int(data[1].strip().replace("lbs", ""))
            description = data[2].strip()
            image_name = filename.replace(".txt", ".jpeg")
            url = "http://35.202.233.207/fruits/"
            jsonFile = {"name": name, "weight": weight, "description": description, "image_name": image_name}
            print(jsonFile)
            r = requests.post(url, data=jsonFile)
            #if status is okay
            if r.ok:
                print("OK")
            else:
                #print error message
                print(r.text)
            # print(r.text)