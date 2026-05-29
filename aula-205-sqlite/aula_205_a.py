import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#cuidado: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()


# Create the table
cursor.execute(
    f'CREATE TABLE If NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL' #Número com ponto flutuante
    ')'
)
connection.commit()
# -------------------------------------------------------------
# Rename de weith para weight
# cursor.execute(
#     'ALTER TABLE customers RENAME column weith to weight'
# )
# -------------------------------------------------------------

# Insert values into the table columns
#CUIDADO: sql injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME}'
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Felipe", 76), '
    '(NULL, "Priscila", 78),'
    '(NULL, "João Paulo", 80)'
)
connection.commit()

cursor.close()
connection.close()
