from bs4 import BeautifulSoup
import requests


class amazon:

    def __init__(self):
        self.header = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})
        self.soup = None

    def fetch(self, url):
        # HTTP Request
        webpage = requests.get(url, headers=self.header)

        # Soup Object containing all data
        self.soup = BeautifulSoup(webpage.content, "html.parser")

        print("fetch successful")
        return True

    def get_name(self):
        return self.soup.find("span", {"id": "productTitle"}).text.strip()

    def get_price(self):
        txt = self.soup.find("div", {"id": "corePriceDisplay_desktop_feature_div"}).find("span", {"class": "a-offscreen"}).text
        return float(txt[1:])
