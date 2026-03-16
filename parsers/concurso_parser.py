import re


def extrair_salario(texto):

    match = re.search(r'R\$ ?\d[\d\.]+', texto)

    if match:

        return match.group()

    return None


def extrair_vagas(texto):

    match = re.search(r'\d+ vagas', texto.lower())

    if match:

        return match.group()

    return None