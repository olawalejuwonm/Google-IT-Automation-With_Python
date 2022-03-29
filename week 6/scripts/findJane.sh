#!/bin/bash

# search for all lines that contain the name "jane" and save the file names into a variable
# files=$(grep -l "jane" ../data/ | cut -d ":" -f 1)
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

#check if file names present in files variable are actually present in the file system
#iterate over the files variable and add a test expression within the loop. If the item within the files variable passes the test, add/append it to the file oldFiles.txt.
for file in $files
do
    #check if file is present in the file system at ../data/
    if [ -f ../$file ]
    then
        echo $file >> oldFiles.txt
    fi
done