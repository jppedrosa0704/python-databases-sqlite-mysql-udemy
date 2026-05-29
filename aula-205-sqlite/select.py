import sqlite3
from aula_205_b import DB_FILE, TABLE_NAME

connection = sqlite3.Connection(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
)

for row in cursor.fetchall():
    # print(row)
    # _id = row[0]
    # name = row[1]
    # weight = row[2]
    # print(_id, name, weight)
    _id, name, weight = row
    print(_id, name, weight)


# select com filtro
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3" ' #Posso definir qual índice usando 'where'
)

print()

row = cursor.fetchone() #selecina a primeira linha da tabela
print(row)


cursor.close()
connection.close()