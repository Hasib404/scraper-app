import requests
from bs4 import BeautifulSoup
import csv


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.parsed_data = None

    def __get_page_content(self):
        headers = {
            "User-Agent": "My User Agent 1.0",
        }

        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        self.parsed_data = soup

        return None

    def __get_next_url(self, url):
        next_url = None

        if url:
            page_next_content = self.parsed_data.find(
                "a", {"class": "pagination__next"}
            )

            if page_next_content:
                next_url = page_next_content["href"]
            else:
                try:
                    print("Trying again to reach the URL!")
                    page_next_content = self.parsed_data.find(
                        "a", {"class": "pagination__next"}
                    )

                    if page_next_content:
                        next_url = page_next_content["href"]
                    else:
                        print("Tried again to fetch the next page url but FAILED")
                        return None
                except:
                    print("Next URL not avialable")
        return next_url

    def __get_product_info(self):
        if self.parsed_data:
            containers = self.parsed_data.findAll(
                "div", {"class": "s-item__wrapper clearfix"}
            )
            for container in containers:
                title = container.find("h3", {"class": "s-item__title"}).text
                price = container.find("span", class_="s-item__price").text
                print(title)
                print(price)

    def run_scrapper(self):
        while self.url:
            self.__get_page_content()
            self.__get_product_info()

            next_page_url = self.__get_next_url(self.url)
            self.url = next_page_url
            print(self.url)


s = Scrapper(
    "https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?rt=nc&_dmd=1"
)
s.run_scrapper()
