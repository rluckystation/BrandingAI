import requests
from bs4 import BeautifulSoup

# Function to scrape a brand's website
def scrape_brand(brand_url):
    try:
        # Send an HTTP GET request to the brand's website
        response = requests.get(brand_url)
        response.raise_for_status()

        # Parse the content of the website
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract brand name (adjust based on the actual structure of the page)
        brand_name = soup.find('meta', attrs={'property': 'og:site_name'}) or soup.title

        if brand_name:
            print(f"Brand Name: {brand_name.get('content') if brand_name.has_attr('content') else brand_name.text.strip()}")
        else:
            print("Brand name not found!")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the URL: {e}")

# Example usage for Nike and Tesla
scrape_brand('https://www.nike.com')
scrape_brand('https://www.tesla.com')
