# isinsrance - para saber se o objeto é de determmminado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2),
         {0, 1}, {'nome': 'Luiz'}]

for item in lista:
    if isinstance(item, set):
        print('Set')
        # item.add()
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('str')

        # item.upper()
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('num')
        
        print(item, item * 2)
    
    else:
        print('OUTRO')
        print(item)
