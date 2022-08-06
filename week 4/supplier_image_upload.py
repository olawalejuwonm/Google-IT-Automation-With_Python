#!/usr/bin/env python3


#takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog

#Complete the script with the same technique as used in the file example_upload.py.

import requests
import os
import os.path

url = "http://localhost/upload/"
for filename in os.listdir(os.path.join(os.path.dirname(__file__), "supplier-data/images")):
    if filename.endswith(".jpeg"):
        file_path = os.path.join(os.path.dirname(__file__), "supplier-data/images/", filename)
        with open(file_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r.text)