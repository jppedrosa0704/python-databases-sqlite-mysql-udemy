# SQLite3 com Python

Projeto de estudo utilizando `sqlite3` com Python para aprender operações básicas de banco de dados:

* Criação de tabelas
* Inserção de dados
* Inserção segura com placeholders (`?`)
* Inserção com dicionários
* Leitura de dados (`SELECT`)
* Atualização (`UPDATE`)
* Exclusão (`DELETE`)
* Uso de `executemany`

---

# Tecnologias utilizadas

* Python 3
* SQLite3
* pathlib

---

# Estrutura do projeto

```bash
.
├── aula_205_a.py
├── aula_206_b.py
└── db.sqlite3
```

---

# Funcionalidades

## Aula 205

Arquivo responsável por:

* Criar conexão com banco SQLite
* Criar tabela `customers`
* Resetar IDs automáticos
* Inserir registros manualmente

### Tabela criada

| Campo  | Tipo    |
| ------ | ------- |
| id     | INTEGER |
| name   | TEXT    |
| weight | REAL    |

---

## Aula 206

Arquivo responsável por:

* Inserção segura usando `?`
* Inserção múltipla com `executemany`
* Inserção usando dicionários
* `DELETE`
* `UPDATE`
* `SELECT`
* Listagem dos dados

---

# Exemplos utilizados

## Inserção simples

```python
cursor.execute(sql, ['Fátima', 62])
```

---

## Inserção múltipla

```python
cursor.executemany(
    sql,
    [["Natália", 63], ["Daniele", 65]]
)
```

---

## Inserção com dicionário

```python
cursor.executemany(sql, (
    {'nome': 'Bruce', 'peso': 78},
    {'nome': 'Madona', 'peso': 61}
))
```

---

# Como executar

## Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

---

## Execute os arquivos

```bash
python aula_205_a.py
```

```bash
python aula_206_b.py
```

---

# Observações importantes

## SQL Injection

Evite montar SQL diretamente com `f-string`.

❌ Não recomendado:

```python
f'SELECT * FROM users WHERE name = "{name}"'
```

✅ Recomendado:

```python
cursor.execute(
    'SELECT * FROM users WHERE name = ?',
    [name]
)
```

---

# Conceitos aprendidos

* CRUD com SQLite
* Conexão com banco de dados
* Cursor
* Commit
* Placeholder `?`
* `executemany`
* Uso de dicionários
* Organização de arquivos
* Uso de `Pathlib`

---


