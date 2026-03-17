import sqlite3
import os

DB_PATH = "data/concursos.db"


def conectar():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    return conn


def criar_tabela():

    conn = conectar()

    cursor = conn.cursor()

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

    conn.commit()
    conn.close()


def salvar(link, titulo=None, escolaridade=None, estado=None, data_abertura=None, taxa_inscricao=None, status=None):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO concursos (link, titulo, escolaridade, estado, data_abertura, taxa_inscricao, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (link, titulo, escolaridade, estado, data_abertura, taxa_inscricao, status)
    )

    conn.commit()
    conn.close()