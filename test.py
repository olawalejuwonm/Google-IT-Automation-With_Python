import PIL
from PIL import Image
import os
# im = Image.open("bride.jpg")
# im.rotate(45).show()
# im = Image.open("example.jpg")
# new_im = im.resize((640,480))
# new_im.save("example_resized.jpg")
# help(PIL)
# use PIL to perform the following operations:
# Iterate through each file in the folder
# For each file:
# Rotate the image 90° clockwise
# Resize the image from 192x192 to 128x128
# Save the image to a new folder in .jpeg format
#  make sure to save the updated images in the folder: /opt/icons/

# iterate through each file in the images folder
# for filename in os.listdir("images"):
#     #check if the file ends in .tt

for filename in os.listdir("images"):
    # change file format to .ttif
    # os.rename("images/" + filename, "images/" + filename.replace(".tiff", ".jpeg"))
    try:

        im = Image.open("images/" + filename)
        # rotate the image 90° clockwise
        new_im = im.rotate(90)
        # resize the image from 192x192 to 128x128
        new_im = new_im.resize((128,128))
        # save the image to a new folder in .jpeg format
        #create /opt/icons/ folder if it doesn't exist
        print(os.path.exists("opt/icons/"))
        if not os.path.exists("opt/icons/"):
            os.makedirs("/opt/icons/")
        # new_im.convert("RGB").save("/opt/icons/" + filename.replace(".ttif", ".jpeg"), "jpeg")
        # make sure to save the updated images in the folder: /opt/icons/
    # catch any errors and print the error message
    except Exception as e:
        print(e)
        print("Error processing image: " + filename)
        continue
    