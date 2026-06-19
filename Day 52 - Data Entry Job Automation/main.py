import requests
from bs4 import BeautifulSoup

# Form Links
# https://forms.gle/gJwFFDrKRXUugiC37

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)

property_details = []

html = response.content
soup = BeautifulSoup(html, 'html.parser')

property_cards = soup.find_all('article', attrs={"data-test" : "property-card"})

for card in property_cards:


    link = card.find('a', class_='StyledPropertyCardDataArea-anchor')
    raw_address = card.find('address').text
    raw_price = card.find('span', class_="PropertyCardWrapper__StyledPriceLine").text

    address = raw_address.strip()
    price = raw_price.replace('+/mo', '')

    property_details.append([address, price, link['href']])
