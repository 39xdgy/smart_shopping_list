from bs4 import BeautifulSoup
import requests


class walmart:

    def __init__(self):
        self.__header = {"User-Agent":"Defined"}
        self.__wrap_around = "https://api.scrapingdog.com/scrape?api_key=635752a08fc4e26b38226434&dynamic=false&url="
        self.soup = None

    def fetch(self, url):
        # HTTP Request
        webpage = requests.get(self.__wrap_around + url,headers=self.__header)

        # Soup Object containing all data
        self.soup = BeautifulSoup(webpage.content, "html.parser")

        print("fetch successful")
        return True

    def get_name(self):
        return self.soup.find("h1", {"class": "b lh-copy dark-gray mt1 mb2 f3"}).text.strip()

    def get_price(self):
        txt = self.soup.find("span", {"itemprop": "price"}).text.split("$")[1]
        return float(txt)
