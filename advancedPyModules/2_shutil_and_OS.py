# opening and reading files and folders

# what if we have to open every file in a directory and read and write to it
# how to loop through them and move files around on our computer

# os module and shutil -- easily navigate files and directories and perform actions on them
# such as moving or deleting them

'''
f = open('practice.txt', 'w+')
f.write('This is a test thing.')
f.close()
'''

import os 

print(os.getcwd()) # current working directory

print(os.listdir()) # list everything in the current directory

# list items in another directory
# listdir takes as argument the path of a dir
print(os.listdir('/Users/'))

# move files around
# shell utility module -- move files in diff locations

import shutil

# shutil.move('practice.txt', '/Users/georgianastan/Desktop/github py course/advancedPyModules')

print('\n')
print(os.listdir('/Users/georgianastan/Desktop/github py course/advancedPyModules'))


# send2trash -- safer without permanent removal instead of shutil.rmtree(path)


import send2trash

print(os.getcwd()) # current working directory

# shutil.move('/Users/georgianastan/Desktop/github py course/advancedPyModules/practice.txt', os.getcwd())

print(os.listdir('/Users/georgianastan/Desktop/github py course/advancedPyModules'))

# move file to bin
# send2trash.send2trash('practice.txt')

print(os.listdir('/Users/georgianastan/Desktop/github py course'))

print('\n')

# os.walk('top') -- directory tree generator 
# for each dir in dir tree rooted at the top it's going to yield a tuple:
# the dirpath, dirnames, filenames

file_path = '/Users/georgianastan/Desktop/github py course/Example_Top_level'
for folder, sub_folders, files in os.walk(file_path):

    print(f"Currently looking at {folder}")
    print('\n')
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")

    print('\n')
    print("The files are: ")
    for f in files:
        print(f"\t File: {f}")
    print('\n')

# oswalk looks at folder, subfolders and files -- everything in a dir
# look within directories within directories -- OSWALK REALLY USEFUL
    
