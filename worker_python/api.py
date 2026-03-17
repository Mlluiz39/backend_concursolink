from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from worker_python.database import conectar
from typing import Optional, List
import sqlite3

app = FastAPI(title="API ConcursoLink")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do ConcursoLink"}

@app.get("/concursos")
def buscar_concursos(
    escolaridade: Optional[str] = Query(None, description="Filtro por escolaridade (ex: Qualquer nível)"),
    estado: Optional[str] = Query(None, description="Filtro por estado (ex: SP, RJ, Brasil)"),
    data_abertura: Optional[str] = Query(None, description="Data de abertura (ex: dd/mm/aaaa)"),
    taxa_inscricao: Optional[float] = Query(None, description="Taxa máxima de inscrição"),
    status: Optional[str] = Query(None, description="Status do concurso (ex: Abertos, Em breve)")
):
    conn = conectar()
    conn.row_factory = sqlite3.Row  # Returns dict-like rows
    cursor = conn.cursor()

    query = "SELECT * FROM concursos WHERE 1=1"
    params = []

    if escolaridade:
        query += " AND escolaridade LIKE ?"
        params.append(f"%{escolaridade}%")
    
    if estado:
        query += " AND estado LIKE ?"
        params.append(f"%{estado}%")

    if data_abertura:
        query += " AND data_abertura = ?"
        params.append(data_abertura)

    if taxa_inscricao is not None:
        query += " AND taxa_inscricao <= ?"
        params.append(taxa_inscricao)

    if status:
        query += " AND status LIKE ?"
        params.append(f"%{status}%")

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    return {"metadata": {"count": len(rows)}, "data": [dict(row) for row in rows]}
