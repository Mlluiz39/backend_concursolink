import requests
from bs4 import BeautifulSoup


class GenericScraper:

    def __init__(self, url):

        self.url = url

    def coletar_links(self):

        response = requests.get(self.url, timeout=20)

        soup = BeautifulSoup(response.text, "html.parser")

        links = []

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "concurso" in href.lower() or "edital" in href.lower():

                links.append(href)

        return links