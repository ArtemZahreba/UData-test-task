import requests
from bs4 import BeautifulSoup
from static import HEADERS
import json

# URL of the first page to scrape
URL = 'https://kelm-immobilien.de/immobilien/page/1/'

# Predefined variables to store the data
urls = []  # URLs of the property listings
names = []  # Names of the properties
pictures = []  # Pictures of the properties
price = []  # Prices of the properties
description = []  # Descriptions of the properties
phone_number = []  # Phone numbers for contact
country = []  # Countries of the properties (constant 'DE')
location = []  # Locations of the properties
email = []  # Email addresses for contact

# Loop through multiple pages on the website to collect some data
for i in range(1, 5):
    URL = f'https://kelm-immobilien.de/immobilien/page/{i}/'

    response = requests.get(
        url=URL,
        headers=HEADERS
    )

    soup = BeautifulSoup(
        response.text,
        'lxml'
    )

    list_of_offers = soup.find_all(
        name='h3',
        class_='property-title'
    )

    names += [i.text for i in list_of_offers]
    urls += [i.find(name='a').get("href") for i in list_of_offers]
    price += [
        i.text.replace('\u202fEUR', '') for i in soup.find_all(
            name='div',
            class_='dd col-xs-7'
        ) if 'EUR' in i.text]
    location += [
        i.text.strip() for i in soup.find_all(
            name='div',
            class_='property-subtitle'
        )]

# Loop through the property pages to collect additional data
for i in urls:
    response = requests.get(
        url=i,
        headers=HEADERS
    )

    soup = BeautifulSoup(
        response.text,
        'lxml'
    )

    try:
        email_ = soup.find(
            name='div',
            class_='dd col-sm-7 u-email value'
        ).text.strip()
    except:
        email_ = 'None'
    try:
        phone_number_ = soup.find(
            name='div',
            class_='dd col-sm-7 p-tel value'
        ).text.strip()
    except:
        phone_number_ = 'None'
    try:
        description_ = soup.find(
            name='div',
            class_='property-description panel panel-default'
        ).text.strip()
    except:
        description_ = 'None'

    try:
        list_pictures = soup.find_all(
            name='img',
        )[1: -4]
    except:
        list_pictures = [-1]

    if list_pictures == [-1]:
        continue

    email.append(email_)
    phone_number.append(phone_number_)
    pictures.append([i.get('src') for i in list_pictures])
    description.append(description_)

# Variable to hold the final result for JSON output
result = {}

# Number of elements in the names list
n = len(names)

# Loop to write data to the result variable for JSON output
for i in range(n):
    title = names[i]
    url = urls[i]
    picture = pictures[i]
    rent_price = price[i]
    descriptions = description[i]
    phone_numbers = phone_number[i]
    emails = email[i]
    country = 'DE'
    locations = location[i]

    result[title] = {
        'url': url,
        'title': title,
        'status': '',
        'pictures': picture,
        'rent_price': rent_price,
        'description': descriptions,
        'phone_number': phone_numbers,
        'email': emails,
        'country': country,
        'location': locations
    }

# Filename for the JSON output
filename = 'data.json'

# Save data to a JSON file
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print(f"Data saved to file {filename}")
