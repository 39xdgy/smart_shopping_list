from bs4 import BeautifulSoup
import requests


# add your user agent 
header = {
    "User-Agent":"Defined"
}
 # The webpage URL
url = "https://api.scrapingdog.com/scrape?api_key=635752a08fc4e26b38226434&dynamic=false&url=https://www.walmart.com/ip/Flashforge-3D-Printer-Adventurer-3-Auto-Leveling-FDM-Printing-Machine-Enclosure-Chamber-150X150X150MM/926206083"


#target_url="https://api.scrapingdog.com/scrape?dynamic=false&url=http://www.walmart.com/ip/SAMSUNG-58-Class-4K-Crystal-UHD-2160P-LED-Smart-TV-with-HDR-UN58TU7000/820835173"

#response = requests.get(url)
# HTTP Request
webpage = requests.get(url)

# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "html.parser")

#print(soup)

name = soup.find("h1", {"class": "b lh-copy dark-gray mt1 mb2 f3"}).text

print(name)

price = soup.find("span", {"itemprop": "price"}).text

print(price)