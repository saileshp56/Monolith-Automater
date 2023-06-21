import os
import subprocess
from urllib.parse import urlparse

def getFileName(s):
    # parses the URL for the path (the part after the domain)
    temp = urlparse(s).path

    # the path contains the first '/' which we do not want
    if temp[0] == "/":
        temp = temp[1:]
    i = 0
    arr = list(temp)

    while i < len(arr):
        if arr[i] == "/":
            arr[i] = "-"
        i+=1

    # returns the entire path connected by dashes (-)
    # a '/' in the name causes an error
    return ''.join(arr)

# folder to put the files into if it does not already exist
output_dir = 'archive'
os.makedirs(output_dir, exist_ok=True)

with open('input.txt', 'r') as file:
    urls = file.read().splitlines()
for url in urls:
    # gets a file_name that will be unique across the same domain
    file_name = getFileName(url)
    print(file_name)
    # runs the command
    command = f'monolith {url} -o {output_dir}/{file_name}.html'
    subprocess.run(command, shell=True)
