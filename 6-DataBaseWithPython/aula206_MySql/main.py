# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import pymysql.cursors
import dotenv
import os 
dotenv.load_dotenv()

TABLE_NAME='customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOTS'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

# print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:


        # CREATING TABLE
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # WARNING: THIS CLEAR THE TABLE
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()




        # INSERTING DATA WITH TUPLE AND PLACEHOLDERS
        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                '(name, age) '
                'VALUES '
                '(%s, %s) ' # PLACEHOLDERS
            )
            data = (
                ('Luiz', 81),
                ('Carlos', 65), 
                ('Roberta', 61)
            )
            result = cursor.executemany(sql, data)
            # print(sql, data)
            # print(result)
        connection.commit()

        



        # INSERTING DATA WITH DICTIONARY AND PLACEHOLDERS 
        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                '(name, age) '
                'VALUES '
                '(%(name)s, %(age)s) ' # PLACEHOLDERS
            )
            data2 = (
                {'name': 'Kauê', 'age': 18},
                {'name': 'Thairine', 'age': 27},
                {'name': 'Alceu', 'age': 70},
            )
            
            result = cursor.executemany(sql, data2)
            # print(sql)
            # print(data2)
            # print(result)
        connection.commit()




        # READING VALUES FROM THE DATABASE
        with connection.cursor() as cursor:
            # menor_id = int(input('Digite o menor ID: '))
            # maior_id = int(input('Digite o maior ID: '))
            menor_id = 1
            maior_id = 6
            column = 'id'
            sql = (
                f'SELECT * FROM {TABLE_NAME} '
                f'WHERE {column} > %s AND {column} < %s'
            )
            cursor.execute(sql, (menor_id, maior_id))
            # print(cursor.mogrify(sql, (menor_id, maior_id)))

            datas = cursor.fetchall()

            # for row in datas:
            #     print(*row)
        connection.commit()


        # DELETING ROWS WITH 'DELETE', 'WHERE' AND 'PLACEHOLDERS'
        # with connection.cursor() as cursor:
        #     # id_removed = input('ID remove is: ')
        #     sql = (
        #         f'DELETE FROM {TABLE_NAME} '
        #         'WHERE id = %s '
        #     )
        #     cursor.execute(sql, (2)) #, (id_removed))
        
        #     cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        #     datas = cursor.fetchall()

        #     for row in datas:
        #         print(*row)

        # connection.commit()


        print()
        print()

        # EDITING WITH UPDATE, WHERE AND PLACEHOLDERS 
        with connection.cursor() as cursor:
            new_name = 'Kauê'
            sql = (
                f'UPDATE {TABLE_NAME} '
                'SET name = %s, age = %s '
                'WHERE id = %s '
            )
            cursor.execute(sql, ('Kauê', 102, 6))
            resultAffectedRows = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

            data0 = cursor.fetchall()

            for row in data0:
                print(row)

            print('AffectedRows', resultAffectedRows)
            print('rowscount', cursor.rowcount)

            cursor.scroll(-5)
            print('rownumber: ', cursor.rownumber)         

            # TESTING lastrowid
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                '(name, age) '
                'VALUES '
                '(%s, %s) ' # PLACEHOLDERS
            )
            data = (
                ('Luiz', 81),
                ('Carlos', 65), 
                ('Roberta', 61)
            )
            result = cursor.executemany(sql, data)

            print('lastrowid', cursor.lastrowid)   
            
        connection.commit()




