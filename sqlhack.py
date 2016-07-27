import os
import sys

# change to traditional hackers' color
os.system("color 0a")

url = ""

def get_sqlmap(options):
    command = "sqlmap -u " + url + " " + options
    process = os.popen(command)
    result = str(process.read())
    return result

def interact():
    os.system("sqlmap --wizard")




