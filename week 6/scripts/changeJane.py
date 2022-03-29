#!/usr/bin/env python3
import sys
import subprocess

with open(sys.argv[1], 'r') as f:
    for line in f:
        oldname = line.strip()
        #use replace() function to replace "jane" with "jdoe" in old name
        newname = oldname.replace("jane", "jdoe")
        print(oldname)
        #Now, invoke a subprocess by calling run() function. This function takes arguments used to launch the process. These arguments may be a list or a string.
#mmand to rename the files in the file system. This command moves a file or directory. It takes in source file/directory and destination file/directory as parameters. We'll move the file with old name to the same directory but with a new name.
        subprocess.run(["mv", ".." + oldname, ".." + newname])
        #close the file