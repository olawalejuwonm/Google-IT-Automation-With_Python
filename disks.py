import shutil
du = shutil.disk_usage("/")
print(du)
#cpu usage
# import psutil
# mic = psutil.cpu_percent(0.1)
# print(mic)
#!/usr/bin/env python3
import requests
import socket
def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == "127.0.0.1":
                return True
        else:
                return False


def check_connectivity():
    request = requests.get("http://www.google.com")
    status_code = request.status_code
    if (status_code == 200):
        return True
    else:
        return False
print(check_localhost())
print(check_connectivity())