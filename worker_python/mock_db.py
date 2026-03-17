import sqlite3
import os

DB_PATH = "data/concursos.db"

def mock_data():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS concursos")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS concursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT UNIQUE,
        titulo TEXT,
        escolaridade TEXT,
        estado TEXT,
        data_abertura TEXT,
        taxa_inscricao REAL,
        status TEXT
    )
    """)
    
    data = [
        ("http://link1.com", "Concurso Banco do Brasil", "Médio", "Brasil", "15/10/2026", 50.0, "Abertos"),
        ("http://link2.com", "Concurso Receita Federal", "Superior", "Brasil", "20/11/2026", 120.0, "Em breve"),
        ("http://link3.com", "Prefeitura de São Paulo", "Qualquer nível", "SP", "01/09/2026", 35.0, "Abertos"),
        ("http://link4.com", "Polícia Civil RJ", "Superior", "RJ", "05/12/2026", 90.0, "Em breve"),
        ("http://link5.com", "Concurso INSS", "Médio", "Brasil", "10/10/2026", 65.0, "Abertos")
    ]
    
    cursor.executemany(
        "INSERT INTO concursos (link, titulo, escolaridade, estado, data_abertura, taxa_inscricao, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
        data
    )
    
    conn.commit()
    conn.close()
    print("Mock data inserted.")

if __name__ == "__main__":
    mock_data()
