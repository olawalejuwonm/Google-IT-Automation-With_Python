# with open("spiders.txt") as file:
#     for line in file:
#         print(line.strip().upper())
# file = open("spiders.txt")
# lines = file.readlines() #to list
# file.close()
# lines.sort() 
# print(lines) 

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")
import os
import datetime
# os.remove("novel.rx")
# os.rename("ssidk.py", "disks.py")
# print(os.path.exists("novel.txt"))
# print(os.path.getsize("novel.txt"))
# print(os.path.getmtime("novel.txt")) # last mdified unix timestamp from january 1 1970
# timestamp = os.path.getmtime("novel.txt")
# print(datetime.datetime.fromtimestamp(timestamp))
# print(os.path.abspath("novel.txt"))
# print(os.getcwd()) #Return a unicode string representing the current working directory.

# os.mkdir("new_dir")
# os.chdir("new_dir")
# print(os.getcwd()) #Return a unicode string representing the current working directory.
# os.rmdir("new_dir")
# res = os.listdir("venv")
# dir = "venv"
# for name in os.listdir(dir):
#     fullname = os.path.join(dir, name) #window specific for joining eaither with backslash in windows \ or forward slash / in mcos
#     if os.path.isdir(fullname):
#         print("{} is a directory.".format(fullname))
#     else:
#         print("{} is a file".format(fullname))
import csv
# f = open("novel.txt")
# csv_f = csv.reader(f)
# for row in csv_f:
#     print( row)
# f.close()

# hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
# with open("hosts.csv", "w") as hosts_csv:
#     writer = csv.writer(hosts_csv)
#     writer.writerows(hosts)

# with open("softwares.csv") as software:
#     reader = csv.DictReader(software)
#     # print(reader)
#     for row in reader:
#         print(row)
#         # print(("{} has {} users").format(row["name"], row["users"]))

users = [{'name': 'Juwon', 'version': ' 8.9', 'status': 'development', 'users': '1000'}, {'name': 'Juwon', 'version': ' 8.9', 'status': 'development', 'users': '1000'},
{'name': 'Juwon', 'version': ' 8.9', 'status': 'development', 'users': '1000'},
{'name': 'Juwon', 'version': ' 8.9', 'status': 'development', 'users': '1000'},
{'name': 'Juwon', 'version': ' 8.9', 'status': 'development', 'users': '1000'}]
keys = ["name", "version", "status", "users"]
with open("gen_doc.csv", "w") as bd:
    writer = csv.DictWriter(bd, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

# print(res) 