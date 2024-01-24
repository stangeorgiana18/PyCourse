# GOAL: GET TITLE OF EVERY BOOK WITH A 2 STAR RATING

import requests
import bs4


'https://books.toscrape.com/catalogue/page-2.html'

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
page_number = 12
page = base_url.format(page_number)

print(page)

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')

products = soup.select(".product_pod")
print(len(products)) # first 20 books


# first way of grabbing the books with 2 stars 
example = products[0]
#print(example)

print('star-rating Three' in str(example))

# more efficient tactic
print([] == example.select(".star-rating.Two")) # space needs to be replaced with a dot: star-rating Three

# the title is in a, the linking element
print(example.select('a')) # 2 links: the image and the title of the book
# I'm grabbing the second link at index 1

# grab the title as though it is a dictionary call
title = example.select('a')[1]['title']
print(title)


# WE CAN CHECK IF STH IS 2 STARS (STRING CALL IN, EXAMPLE.SELECT(RATING))
# EXAMPLE.SELECT('a')[1]['title'] to grab the book title


two_star_titles = []

for n in range(1, 51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod") # look for all the books in the soup

    # filter out through these books
    for book in books:
        # if 'star_rating Two' in str(book)
        if len(book.select(".star-rating.Two")) != 0: # if the list is not empty for star rating two
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)
