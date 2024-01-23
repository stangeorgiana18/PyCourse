import shutil
import os 
import re


# extract the instructions
# by default it creates an extracted_content file

shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip')


with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

    
phone_pattern = r'\d{3}-\d{3}-\d{4}'


def search(file, pattern= r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    
    # grab the text of the file
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return '' # or pass --> None


# walk through all the files 
results = []
for folder, sub_folders, files in os.walk(os.getcwd()+'/extracted_content'):

    for f in files:
        full_path = folder + "/" + f
        #print(full_path)

        results.append(search(full_path))

for r in results:
    if r != '':
        print(r.group())
    

# 719-266-2837