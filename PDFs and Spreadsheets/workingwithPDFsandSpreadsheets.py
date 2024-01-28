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

# extract an entire column
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

print('\n')

f.close()


# PDF FILES -- portable document format
# no machine readable standard format

import PyPDF2

# opne the file and attach a reader object to it
# rb -- read binary since it's not a normal text file
f = open('Working_Business_Proposal.pdf', 'rb') 

# to make sure we can work with this:
pdf_reader = PyPDF2.PdfReader(f)

# number of pages
print(len(pdf_reader.pages)) # 5

# index 0 for page 1
page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()

print(page_one_text)
# empty string -- pdf file not compatible with PyPDF2; use another library

# then you can use regex to searcg for a particular pattern

f.close()


# WRITE ANOTHER PDF PAGE  
# we cannot write text in the middle of a page with PyPDF2
# PDFs are not designed to be easily editable

# ADD PAGES TO PDF
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]

# grab pages by writing them to a new file
# create a writer object
pdf_writer = PyPDF2.PdfWriter() 

print(type(first_page)) # <class 'PyPDF2._page.PageObject'>

# the page added should be already of specialised file type
# it shouldn't just be a raw py string
pdf_writer.add_page(first_page)

# open a new file and write to it
pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

print('\n')


# add all the text that exists within a PDF file
f = open('Working_Business_Proposal.pdf', 'rb')

# the index of the list corresponds to the page number 
# so I'll have one large string per position in this list
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):

    page = pdf_reader.pages[num]

    pdf_text.append(page.extract_text())

print(pdf_text[0])

print('\n')


# PDF and CSV PUZZLE EXERCISE

# EXTRACT the Google Drive link from the .csv file
# Hint: It's along the diagonal from top left to bottom right
data = open('find_the_link.csv') 
csv_data = csv.reader(data)
data_lines = list(csv_data) # list of lists
#print(data_lines)
print(len(data_lines)) # 66 -- number of rows 


link = ''

'''
for i in range(len(data_lines)):
    link += data_lines[i][i]

'''



'''
link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
''.join(link_list)

'''


# data is the row 
# row_number -- current number of the row we're on
for row_num, data in enumerate(data_lines):

    link += data[row_num]

print(link)


'''
# this did not work - invalid pdf format 
import requests

pdf_response = requests.get(link)
pdf_content = pdf_response.content

# write the binary content to a local pdf file
with open('downloaded_pdf.pdf', 'wb') as pdf_file:
    pdf_file.write(pdf_content)

'''

# download the pdf from the link 
# grab the phone number from the pdf without knowing its format

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfReader(f)
print(len(pdf.pages)) # 17

import re

pattern = r'\d{3}.\d{3}.\d{4}'
    
all_text = ''

for n in range(len(pdf.pages)):

    page = pdf.pages[n]
    page_text = page.extract_text()

    all_text += ' ' + page_text

#print(all_text) # string with all the text
    
print(re.findall(pattern, all_text)) 
# ['000', '000', '000', '505', '503', '445']
# returns a list of matching objects

# the iteration will return the match objects
for match in re.finditer(pattern, all_text):
    print(match)


'''
<re.Match object; span=(650, 653), match='000'>
<re.Match object; span=(18270, 18273), match='000'>
<re.Match object; span=(35890, 35893), match='000'>
<re.Match object; span=(42919, 42922), match='505'>
<re.Match object; span=(42923, 42926), match='503'>
<re.Match object; span=(42927, 42930), match='445'>

# we can see the actual location of the numbers 
'''

print(all_text[42919 : 42919 + 20]) # 505.503.4455. So hor
print(all_text[42900 : 42919 + 20]) # phone number is 505.503.4455. So hor

for match in re.finditer(pattern, all_text):
    print(match)

# <re.Match object; span=(42919, 42931), match='505.503.4455'>
    


# OR
    
pattern = r'\d{3}.\d{3}.\d{4}'

for n in range(len(pdf.pages)):
        
    page  = pdf.pages[n]
    page_text = page.extract_text()
    match = re.search(pattern, page_text)
    
    if match:
        print(match.group())

# 505.503.4455