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
    address = card.find('address', attr={"data-test" : "property-card-addr"})
    price = card.find('span', class_="PropertyCardWrapper__StyledPriceLine").text

    property_details.append([link['href'], address, price])

print(property_details[0])