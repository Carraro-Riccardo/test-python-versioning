import sys
import os
import glob
import re
import subprocess

repo_url = "https://github.com/Carraro-Riccardo/test-python-versioning"
target_directory = "./tmp"
branch_name = "main"
subprocess.run(["git", "clone", "--branch",  branch_name, repo_url, target_directory,  "--quiet"], check=True)

file_path  = sys.argv[1]
file_name   = sys.argv[2]
str_version = "1.0.0"

file_name_only = file_name[:-4]

search_pattern = f"{file_name}*.pdf"
matching_file = glob.glob("./tmp/"+file_path+"/"+search_pattern)

if len(matching_file) != 0:
    re_pattern = r"_v(\d+\.\d+\.\d+)\.pdf"
    str_version = re.search(re_pattern,"./tmp/"+file_path+"/"+matching_file[0]).group(1)


version_components = str_version.split('.')
x = int(version_components[0])
y = int(version_components[1])
z = int(version_components[2])

new_file_content  = ""
old_file_content = ""

with open(file_path+"/"+file_name+".typ") as file:
    new_file_content = file.read()

with open("./tmp/"+file_path+"/"+file_name+".typ") as file:
    old_file_content = file.read()

def diff_letters(first, second,x,y,z):
    if first != second:
        z = z + 1
    if first.count("=") < second.count("="):
        y = y + 1
    return str(x) + "." + str(y) + "." + str(z)

new_version = diff_letters(old_file_content, new_file_content,x,y,z)

print(new_version)
