import sys
import os
import glob
import re
import subprocess

#vedere se il file esiste in src
#mi recupero la variabile e incremento quella
#altrimenti set variabile v.1.0.0 e pusho il file

#prende la versione, il vecchio file e il nuovo file da parametro shell
#es. py change_viewer.py 1.0.0
repo_url = "https://github.com/Carraro-Riccardo/Carraro-Riccardo.github.io"
target_directory = "./tmp"
branch_name = "docs"
subprocess.run(["git", "clone", "--branch", branch_name, repo_url, target_directory], check=True)


first_file  = sys.argv[1]
second_file = sys.argv[2]

file_name_only = second_file[:-4]
search_pattern = f"{file_name_only}*.pdf"
matching_file = glob.glob("./"+search_pattern)[0]

pattern = r"_v(\d+\.\d+\.\d+)\.pdf"
str_version = re.search(pattern, matching_file).group(1)

version_components = str_version.split('.')
x = int(version_components[0])
y = int(version_components[1])
z = int(version_components[2])

first_file_content  = ""
second_file_content = ""

with open(first_file) as file:
    first_file_content = file.read()

with open(second_file) as file:
    second_file_content = file.read()

def diff_letters(first, second,x,y,z):
    if first != second:
        z = z + 1
    if first.count("=") < second.count("="):
        y = y + 1
    return str(x) + "." + str(y) + "." + str(z)

new_version = diff_letters(first_file_content, second_file_content,x,y,z)

print("vecchia versione:\t" + str_version + "\nnuova versione:\t\t" + new_version)

os.rename(matching_file, file_name_only+"_v"+new_version+".pdf")

with open(first_file, "w") as file:
    file.write(second_file_content)
#aggiunta step al changelog per aggiornare la variabile
#rimuoviamo il vecchio il pdf e mettiamo il nuovo con la nuova version


#mettere il diff in un file d'appoggio
