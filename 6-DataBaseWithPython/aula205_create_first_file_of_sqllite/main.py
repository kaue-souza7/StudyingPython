import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()

# Delete mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()



# Cria a Tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY  AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL' 
    ')'
)
connection.commit()


# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(:name, :weight)' 
)
cursor.executemany(
    sql, 
    [
        {'name': 'Mário', 'weight': 33},
        {'name': 'Rodolfo', 'weight': 90},
        {'name': 'Ana', 'weight': 41},
        {'name': 'Carol', 'weight': 55},
    ]
) 
connection.commit()

# No execute pode passar um ou muitos valores,
# trabalhando com tuplas listas ou dicionários






 



if __name__ == '__main__':
    print(sql)

    # Delete
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 3')
    connection.commit()

    # Update
    cursor.execute(
        f'UPDATE {TABLE_NAME} ' 
        'SET name="TESTE", weight=67.41 '
        'WHERE id = 1'
    )



    # Select
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        # print(row)
        _id, name, weight = row
        print(_id, name, weight)
    connection.commit()





    cursor.close()
    connection.close()


