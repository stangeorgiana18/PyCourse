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
example.select(".star-rating Three")