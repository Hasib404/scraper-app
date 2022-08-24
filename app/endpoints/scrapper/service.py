import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup

from database import URL, PRODUCTS


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.parsed_data = None
        self.page_count = 1
        self.status = "Complete"

    def __get_page_content(self):
        headers = {
            "User-Agent": "My User Agent 1.0",
        }
        try:
            page = requests.get(self.url, headers=headers, timeout=30)
        except Timeout:
            self.status = "Timedout"
            print("Timeout has been raised.")
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
                        return None
                except:
                    print("No more URLs found")
        if next_url:
            self.page_count += 1

        return next_url

    def __get_product_info(self):
        url_dict = {"url": self.url}
        URL.insert_one(url_dict)

        if self.parsed_data:
            containers = self.parsed_data.findAll(
                "div", {"class": "s-item__wrapper clearfix"}
            )

            for container in containers:
                title = container.find("h3", {"class": "s-item__title"}).text
                price = container.find("span", class_="s-item__price").text
                product_list = {"product": title, "price": price}
                if title and price:
                    PRODUCTS.insert_one(product_list)

    def run_scrapper(self):
        while self.url:
            self.__get_page_content()
            self.__get_product_info()
            next_page_url = self.__get_next_url(self.url)
            self.url = next_page_url
        total_product = PRODUCTS.count_documents({})

        result = {
            "status": self.status,
            "page_collected": self.page_count,
            "total_product": total_product,
        }
        return result
