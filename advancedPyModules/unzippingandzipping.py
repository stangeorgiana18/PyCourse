f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()


 # COMPRESS the file and insert it a zip file

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
# w bcs we're writing to it

# write to the compressed file
comp_file.write('fileone.txt', compress_type = zipfile.ZIP_DEFLATED)

comp_file.write('filetwo.txt', compress_type= zipfile.ZIP_DEFLATED)

comp_file.close()

# EXTRACT the items from a zip file

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')



# ARCHIVE AN ENTIRE FOLDER 
# USING SHELL UTILITY LIBRARY 

import shutil

dir_to_zip = '/Users/georgianastan/Desktop/github py course/advancedPyModules/extracted_content'
output_filename = 'example'

# (where_to_output_the_zip_version, format, what_we're_zipping)
shutil.make_archive(output_filename, 'zip', dir_to_zip)

# EXTRACT USING SHELL UTILITY

# (filename/path, what_should_the_extract_dir_call_it, format)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')



