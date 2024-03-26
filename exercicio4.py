"""
Suponha que você tenha uma lista de dicionários,
onde cada dicionário representa 
um aluno com suas notas em diferentes disciplinas.
Escreva um programa que calcule 
a média de cada aluno e adicione essa média 
como uma nova chave em cada dicionário.
"""
students = [
    '': {"nome": "João", "notas": [8, 7, 6, 9]},
    {"nome": "Maria", "notas": [9, 8, 9, 10]},
    {"nome": "Pedro", "notas": [7, 8, 7, 8]},
    {"nome": "Ana", "notas": [10, 9, 10, 10]}
]

while True:
    student_new = {}

    insert_name = input('Enter a name: ')
    insert_note = input('Enter a note: ')

    student_new = {'Name': insert_name, 'Note': [insert_note]}

    students.append(student_new)
    
    for student in students:
        print(student)


    want_to_continue = input('Want add student new [Y]es or [N]o: ').lower
    if want_to_continue == 'y':
        continue
    elif want_to_continue == 'n':
        break
    else:
        print('Enter y or n only')

    
  









