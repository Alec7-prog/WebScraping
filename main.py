import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://webscraper.io/test-sites/e-commerce/static').text

max_cost = int(input("What is your budget? : "))
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_ = "col-md-4 col-xl-4 col-lg-4")

for product in soup:
    product = soup.find('div', class_ = 'col-md-4 col-xl-4 col-lg-4')
    cost = int(product.find('h4', class_ = 'price float-end card-title pull-right').text.replace('$', ''))
    if cost < max_cost:
        title = product.find('a', class_ = 'title').text    
        reviews = product.find('p', class_ = 'review-count float-end').text
    
        print(f'''
            Product: {title} 
            Cost: {cost}
            Reviews: {reviews}
        ''')