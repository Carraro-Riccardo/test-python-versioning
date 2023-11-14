import sys
import os
import glob
import re
import subprocess

repo_url = "https://github.com/Carraro-Riccardo/test-python-versioning"
target_directory = "./tmp"
branch_name = "main"
subprocess.run(["git", "clone", "--branch", branch_name, repo_url, target_directory], check=True)


file_path  = sys.argv[1]
file_name   = sys.argv[2]
str_version = sys.argv[3]

file_name_only = file_name[:-4]

version_components = str_version.split('.')
x = int(version_components[0])
y = int(version_components[1])
z = int(version_components[2])

new_file_content  = ""
old_file_content = ""

print(file_path+"/"+file_name)
with open(file_path+"/"+file_name) as file:
    new_file_content = file.read()

print("./tmp"+file_path[2:]+"/"+file_name)
with open("./tmp"+file_path[2:]+"/"+file_name) as file:
    old_file_content = file.read()

def diff_letters(first, second,x,y,z):
    if first != second:
        z = z + 1
    if first.count("=") < second.count("="):
        y = y + 1
    return str(x) + "." + str(y) + "." + str(z)

new_version = diff_letters(old_file_content, new_file_content,x,y,z)

print("vecchia versione:\t" + str_version + "\nnuova versione:\t\t" + new_version)
