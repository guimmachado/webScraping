from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page.text, 'html.parser')
quotes = soup.find_all('span', attrs={'class': 'text'})
authors = soup.find_all('small', attrs={'class': 'author'})

file = open('quotes.csv', 'w')
writer = csv.writer(file)

writer.writerow(['Quotes', 'Authors'])

for quote, author in zip(quotes, authors):
    print(quote.text + ' - ' + author.text)
    writer.writerow([quote.text, author.text])
file.close()