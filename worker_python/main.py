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

            if "pciconcursos.com.br" in url:
                from scrapers.pci_scraper import PCIScraper
                scraper = PCIScraper()
                links_data = scraper.buscar_vagas()
            else:
                scraper = GenericScraper(url)
                # O GenericScraper atual só devolve string links. Vamos adaptar para formato dict compatível
                raw_links = scraper.coletar_links()
                links_data = [{"link": l, "titulo": None, "escolaridade": None, "estado": None, "data_abertura": None, "taxa_inscricao": None, "status": None} for l in raw_links]

            for data in links_data:
                salvar(
                    link=data.get("link"),
                    titulo=data.get("titulo"),
                    escolaridade=data.get("escolaridade"),
                    estado=data.get("estado"),
                    data_abertura=data.get("data_abertura"),
                    taxa_inscricao=data.get("taxa_inscricao"),
                    status=data.get("status")
                )

            print(f"{len(links_data)} links encontrados")

            time.sleep(random.uniform(2,5))

        except Exception as e:

            print("Erro ao acessar:", url)
            print(e)


if __name__ == "__main__":
    main()