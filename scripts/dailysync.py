#!/usr/bin/env python
import subprocess
import os
src = "./data/prod/"
dest = "./data/prod_backup/"
# use multiprocessing
from multiprocessing import Pool
#run rsync in parallel
#os.walk() generates the file names in a directory tree by walking the tree either top-down or bottom-
def run(task):
    # Do something with task here
    subprocess.call(["rsync", "-arq", src, dest])
    print("Handling {}".format(task))
tasks = []
for dirpath, dirnames, filenames in os.walk(src):
    print(dirpath)
    print(dirnames)
    print(filenames)
    tasks.append(filenames)
    
if __name__ == "__main__":
  print("Total tasks: {}".format(len(tasks))) 
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool     
  p.map(run, tasks)
    



  
