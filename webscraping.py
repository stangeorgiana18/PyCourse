# techniques involving automating gathering of data from a website
# main focus: become expert in looking up information and generalizing the process 
# of web scraping and apply so you can apply it to unique situations
# idea: poiny py to a particular either CSS tag or HTML element and grab info baseed off that

# BeautifulSoup and requests libraries

import requests
import bs4

# inspect each source and a particular element

result = requests.get('http://www.example.com')
print(type(result)) # <class 'requests.models.Response'>

print(result.text, '\n') # the html document

# (text_string, string_code_for_what_engine_to_use_to_parse_through_the_HTML_text)
soup = bs4.BeautifulSoup(result.text, "lxml") 

print(soup) # raw string --> soup object grabbing things based on tags/elements

title_tags = soup.select('title')
print(title_tags) # [<title>Example Domain</title>] - list

paragraph_tags = soup.select('p')
print(paragraph_tags)

# [<p>This domain is for use in illustrative examples in documents. You may use this
# domain in literature without prior coordination or asking for permission.</p>, <p><a href="https://www.iana.org/domains/example">More information...</a></p>]


first_item_text = soup.select('title')[0].getText()
print(first_item_text) # Example Domain

site_paragraphs = soup.select('p')

print(type(site_paragraphs[0])) # <class 'bs4.element.Tag'>
# not a string, but a bs object, so I can use getText()

print(site_paragraphs[0].getText()) # first paragraph
print('\n')


# GRABBING ALL ELEMENTS OF A CLASS 

# all the strings in the table of contents 
# ability: to inspect a particular element on a page and grab an associated class

res = requests.get('https://en.wikipedia.org/wiki/Tuna')
soup = bs4.BeautifulSoup(res.text, 'lxml')

#print(soup)

print(soup.select('.vector-toc-text'))
first_item = soup.select('.vector-toc-text')[0]
print(first_item) # <div class="vector-toc-text">(Top)</div>

print(first_item.text, '\n')

for item in soup.select('.vector-toc-text'):
    print(item.text)

