import requests
from bs4 import BeautifulSoup
from .base_scraper import BaseScraper
from parsers.concurso_parser import (
    extrair_escolaridade, 
    extrair_estado, 
    extrair_data_abertura, 
    extrair_taxa
)

class PCIScraper(BaseScraper):

    def __init__(self):
        super().__init__()
        self.url = "https://www.pciconcursos.com.br/concursos/"

    def buscar_vagas(self):
        response = requests.get(self.url, timeout=20)
        soup = BeautifulSoup(response.text, "html.parser")

        concursos = []
        cards = soup.select(".ca")  # cards de concursos do pci

        for card in cards:
            titulo_element = card.find("a")
            if not titulo_element:
                continue
                
            titulo = titulo_element.text.strip()
            link = titulo_element["href"]
            
            # Pegar o texto inteiro do card para buscar as outras informações
            texto_completo = card.text.strip()
            
            # Extrair atributos usando o parser
            escolaridade = extrair_escolaridade(texto_completo)
            estado = extrair_estado(titulo) # no PCI a sigla do estado costuma estar no titulo
            data_abertura = extrair_data_abertura(texto_completo)
            taxa_inscricao = extrair_taxa(texto_completo)
            
            # Definir status
            # Exemplo simples, se não achou data ou se conter "Previsto", colocamos "Em Breve", senão "Abertos"
            status = "Abertos"
            if "previsto" in texto_completo.lower():
                status = "Em breve"

            concursos.append({
                "titulo": titulo,
                "link": link,
                "escolaridade": escolaridade,
                "estado": estado,
                "data_abertura": data_abertura,
                "taxa_inscricao": taxa_inscricao,
                "status": status
            })

        return concursos