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

def extrair_escolaridade(texto):
    texto_lower = texto.lower()
    if 'superior' in texto_lower:
        return 'Superior'
    if 'médio' in texto_lower or 'medio' in texto_lower:
        return 'Médio'
    if 'técnico' in texto_lower or 'tecnico' in texto_lower:
        return 'Técnico'
    if 'fundamental' in texto_lower:
        return 'Fundamental'
    if 'alfabetizado' in texto_lower:
        return 'Alfabetizado'
    return 'Qualquer nível'

def extrair_estado(texto):
    # Regex para pegar a sigla do estado geralmente em parênteses: "(SP)" 
    # ou logo após o título / na url. Vamos tentar pegar do texto.
    match = re.search(r'\b([A-Z]{2})\b', texto)
    if match:
        sigla = match.group(1)
        estados_validos = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        if sigla in estados_validos:
            return sigla
    return 'Brasil'

def extrair_data_abertura(texto):
    # Busca formato dd/mm/yyyy
    match = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', texto)
    if match:
        return match.group(1)
    return None

def extrair_taxa(texto):
    # Procura algo como Taxa: R$ 50,00
    match = re.search(r'R\$ ?(\d+[\.,]\d{2})', texto)
    if match:
        val = match.group(1).replace('.', '').replace(',', '.')
        try:
            return float(val)
        except ValueError:
            return None
    return None