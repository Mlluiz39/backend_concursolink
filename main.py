from config import SOURCES
from scrapers.generic_scraper import GenericScraper
from database import salvar, criar_tabela
import time
import random


def main():

    criar_tabela()

    for url in SOURCES:

        try:

            print("Coletando:", url)

            scraper = GenericScraper(url)

            links = scraper.coletar_links()

            for link in links:
                salvar(link)

            print(f"{len(links)} links encontrados")

            time.sleep(random.uniform(2,5))

        except Exception as e:

            print("Erro ao acessar:", url)
            print(e)


if __name__ == "__main__":
    main()