#taken from: https://www.youtube.com/watch?v=QhD015WUMxE
from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com") #specify page to scrape
soup = BeautifulSoup(page_to_scrape.text, "html.parser") #parse html of page using beautifulsoup
quotes = soup.findAll("span", attrs={"class":"text"}) #
authors = soup.findAll("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)