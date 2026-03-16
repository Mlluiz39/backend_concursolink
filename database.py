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
        link TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()


def salvar(link):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO concursos (link) VALUES (?)",
        (link,)
    )

    conn.commit()
    conn.close()