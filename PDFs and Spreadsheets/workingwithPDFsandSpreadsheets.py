# CSV files -- comma separated variables 
# .csv files only contain the raw data from the spreadsheet
# if you export excel files or Google Spreadsheets to .csv

# popular space for libraries that don't come built in with Puthon


# PANDAS -- full data analysis library, visualisations and data analysis
# data science courses include it
# huge library with many facets to it


# OPENPYXL -- library spec. designed for excel files
# python-excel.org tracks various other excel based Python libraries


# GOOGLE SHEETS PYTHON API - directly make changes to spreadsheets hosted online
# a local script will reach out through the internet through the API call and 
# edit the sheets hostedon your Google Drive
# more complex syntax, available in may program. lang., it's not py specific 


import csv


# GRAB INFORMATION


# Open the file
data = open('example.csv') # add encoding to read characters in case of unicode error
# data = open('example.csv', encoding = 'utf-8')
# be aware of the special symbols in the file

# call csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

# UnicodeDecodeError

#print(data_lines)


# loop through the data_lines to actually read data information

# the column names / the column header at index 0
print(data_lines[0]) # ['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']

# number of rows 
print(len(data_lines)) # 1001

for line in data_lines[:5]:
    print(line)

print('\n')

# we may extract any row we want
print(data_lines[10])

# extract a single value / the email
print(data_lines[10][3])

# extract an entire columns
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print('\n')

print(all_emails, '\n')

print(data_lines[10]) # notice the first and last names are separated 

# list of full names
full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])

print(full_names, '\n')


# WRITE TO A CSV FILE

file_to_output = open('to_save_file.csv', mode = 'w', newline = '') # always choose the mode
csv_writer = csv.writer(file_to_output, delimiter = ',') # delimiter = separator of columns 

# for tab separated/.tsv files: delimiter = '\t'

# csv.writer is the sister of csv.reader: you can also pass delimiter parameter in csv.reader

# write a single row, pass in a single row item
csv_writer.writerow(['a', 'b', 'c'])

# write multiple rows, it takes in a list of lists
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']]) # pay attention to '[]' !!!

# close the file
file_to_output.close()

# instead of overwriting, just add rows to the file by changing the mode:
f = open('to_save_file.csv', mode = 'a', newline= '')

csv_writer = csv.writer(f)

print(csv_writer.writerow(['1', '2', '3'])) # print the number of characters written
# also the commas and the newline is counted --> 7

f.close()


