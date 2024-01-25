import requests
import bs4


res = requests.get("https://quotes.toscrape.com")
soup = bs4.BeautifulSoup(res.text, 'lxml')

# the HTML text from the homepage
print(soup) 
# or 
print(res.text)

print(soup.select(".author"))

authors = set()

# the names of all authors on the first page
# name = authors[0].getText()
# print(name)

for name in soup.select(".author"):
   authors.add(name.text)

print(authors, '\n')


# quotes on the first page
print(soup.select(".text"))

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

print(quotes, '\n')


# tags from the home page
print(soup.select(".tag-item"))
print(len(soup.select('.tag-item')))

for item in soup.select('.tag-item'):
    print(item.text)

print('\n')



base_url = 'http://quotes.toscrape.com/page/'

# grab all unique authors from all pages

# first way: knowing the number of pages

example = base_url + str(10)
print(example, '\n') # http://quotes.toscrape.com/page/10

authors = set()

for page in range(1, 11):

    page_url = base_url + str(page)
    res = requests.get(page_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

print(authors, '\n')


# second way: not knowing the number of pages
# what happens if you reach a page that doesn't have any quotes on it?
# looping through the pages until we hit sth that says "No quotes found"

url = 'http://quotes.toscrape.com/page/'

page_url = url + str(1000)

res = requests.get(page_url)

soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup, '\n')

print("No quotes found!" in res.text)

print('\n')

page_still_valid = True
authors_set = set()
page_number = 1

while page_still_valid:

    page = url + str(page_number)

    res = requests.get(page)

    if "No quotes found!" in res.text:
        break 

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select(".author"):
        authors_set.add(name.text)

    page_number += 1


print(authors_set)

