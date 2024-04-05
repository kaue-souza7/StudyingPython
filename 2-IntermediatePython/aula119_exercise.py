# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json




def add_task(task):
    os.system('cls')
    tasks.append(task)


def call_comand(comand):
    if comand == 'listar':
        listar_tasks(tasks)
    elif comand == 'desfazer':
        desfazer_action()
    else:
        refazer_action()

def read(tasks):
    dados = []
    try:
        with open('aula119.json', 'r', encoding='utf8') as data_base:
            dados = json.load(data_base)
        
    except FileNotFoundError:
        print('Arqquivo não existe')
        save(tasks)
    return dados

def save(tasks):
    dados = tasks
    with open('aula119.json', 'w', encoding='utf8') as data_base:
            dados = json.dump(
                tasks, 
                data_base, 
                indent=2, 
                ensure_ascii=False
            )
    return dados

def listar_tasks(tasks):
    os.system('cls')
    if tasks == []:
        print('Não há nada para listar')
        return
    
    for task in tasks: 
        print(task)

def desfazer_action():
    os.system('cls')
    if tasks == []:
        print('Não há nada para desfazer')
        return
    
    item_apagado = tasks.pop()
    deleted_tasks.append(item_apagado)

def refazer_action():
    os.system('cls')
    if deleted_tasks == []:
        print('Não há nada para refazer')
        return

    item_to_remake = deleted_tasks[-1]
    deleted_tasks.pop()
    tasks.append(item_to_remake)


comands = ['listar', 'desfazer', 'refazer']
tasks = read([])
deleted_tasks = []

while True:
    # os.system('cls')
    # print('Comands: ', *comands, sep=",")
    print(f'Comands: {', '.join(comands)}')
    comand_or_task = input('Enter a task or comand: ').lower()

    
    if comand_or_task in comands:
        call_comand(comand_or_task)
    else:
        add_task(comand_or_task)

    save(tasks)
    
    
 