const express = require('express');
const cors = require('cors');
const Database = require('better-sqlite3');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

const DB_PATH = path.join(__dirname, '..', 'data', 'concursos.db');

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Bem-vindo à API do ConcursoLink' });
});

app.get('/concursos', (req, res) => {
  const { escolaridade, estado, data_abertura, taxa_inscricao, status } = req.query;

  let query = 'SELECT * FROM concursos WHERE 1=1';
  const params = [];

  if (escolaridade) {
    query += ' AND escolaridade LIKE ?';
    params.push(`%${escolaridade}%`);
  }

  if (estado) {
    query += ' AND estado LIKE ?';
    params.push(`%${estado}%`);
  }

  if (data_abertura) {
    query += ' AND data_abertura = ?';
    params.push(data_abertura);
  }

  if (taxa_inscricao !== undefined) {
    query += ' AND taxa_inscricao <= ?';
    params.push(parseFloat(taxa_inscricao));
  }

  if (status) {
    query += ' AND status LIKE ?';
    params.push(`%${status}%`);
  }

  try {
    const db = new Database(DB_PATH);
    const stmt = db.prepare(query);
    const rows = stmt.all(...params);
    db.close();

    res.json({ metadata: { count: rows.length }, data: rows });
  } catch (error) {
    console.error('Erro ao buscar concursos:', error);
    res.status(500).json({ error: 'Erro ao buscar concursos' });
  }
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
