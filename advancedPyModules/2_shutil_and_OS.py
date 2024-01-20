# opening and reading files and folders

# what if we have to open every file in a directory and read and write to it
# how to loop through them and move files around on our computer

# os module and shutil -- easily navigate files and directories and perform actions on them
# such as moving or deleting them

f = open('practice.txt', 'w+')
f.write('This is a test thing.')
f.close()

import os 

print(os.getcwd()) # current working directory

print(os.listdir()) # list everything in the current directory

# list items in another directory
# listdir takes as argument the path of a dir
print(os.listdir('/Users/'))

# move files around
# shell utility module -- move files in diff locations

import shutil

shutil.move('practice.txt', '/Users/georgianastan/Desktop/github py course/advancedPyModules')

print(os.listdir('/Users/georgianastan/Desktop/github py course/advancedPyModules'))

