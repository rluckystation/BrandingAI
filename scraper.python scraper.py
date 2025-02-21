خخ



python scraper.py

python scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_brand_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# Example usage
url = 'https://www.nike.com'
brand_info = scrape_brand_info(url)
print(brand_info)

import requests
from bs4 import BeautifulSoup

def scrape_brand_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# Example usage
url = 'https://www.nike.com'
brand_info = scrape_brand_info(url)
print(brand_info)

