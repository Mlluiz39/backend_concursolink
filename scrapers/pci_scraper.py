import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper


class PCIScraper(BaseScraper):

    def __init__(self):
        super().__init__()
        self.url = "https://www.pciconcursos.com.br/concursos/"

    def buscar_vagas(self):

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        concursos = []

        cards = soup.select(".ca")  # seletor exemplo

        for card in cards:

            titulo = card.text.strip()
            link = card.find("a")["href"]

            concursos.append({
                "titulo": titulo,
                "link": link
            })

        return concursos