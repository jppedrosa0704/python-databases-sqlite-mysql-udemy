import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.Connection(DB_FILE)
cursor = connection.cursor()

# delete table
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# connection.commit()

# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
# connection.commit()

#creating table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT, '
    'weigth REAL '
    ')'
)

#---------------------------------------#
# insert values into table columns
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight)'
    'VALUES'
    '(?,?)'
)

cursor.execute(sql, ['Fátima', 62])
cursor.executemany(sql, [["Natália", 63 ], ["Daniele", 65]])
connection.commit()

# também é possível inserir dados com dicionário
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight)'
    'VALUES'
    '(:nome,:peso)'
)

# cursor.execute(sql, {'nome': 'malmsteen', 'peso': 72}) #addciona um por vez
cursor.executemany(sql, (
    {'nome': 'Bruce', 'peso': 78},
    {'nome':'Madona', 'peso': 61}
    )
)
# connection.commit()
#---------------------------------------#

# cursor.close()
# connection.close()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 3'
    )
    connection.commit()

# UPDATE atualiza, edita os dados de uma tabela
    # cursor.execute(
    #     f'UPDATE {TABLE_NAME} '
    #     'SET name= "João Paulo" '
    #     'WHERE id = 9'
    # )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
    )
    
    for row in cursor.fetchall():
        _id, name, weigth = row
        print(_id, name, weigth)
    

    connection.commit()
    
cursor.close()
connection.close()

