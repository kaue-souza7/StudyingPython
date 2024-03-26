
import os
import sys
stock = {
    'product127': {'Nome do produto': 'Computador - Dell22', 
                   'Marco do produto': 'Dell',
                   'Valor': 3000,
                   'Qtd. estoque': 3},
    'product101': {'Nome do produto': 'Computador - Dell33', 
                   'Marco do produto': 'Dell',
                   'Valor': 1500,
                   'Qtd. estoque': 2},
    'product114': {'Nome do produto': 'Computador - Dell18', 
                   'Marco do produto': 'Asus',
                   'Valor': 2550,
                   'Qtd. estoque': 2},
    'product166': {'Nome do produto': 'Geladeira - Big2', 
                   'Marco do produto': 'Eletrolux',
                   'Valor': 4699,
                   'Qtd. estoque': 2},
    'product145': {'Nome do produto': 'Geladeira - little10', 
                   'Marco do produto': 'Brastemp',
                   'Valor': 3499,
                   'Qtd. estoque': 1},
    'product131': {'Nome do produto': 'Celular - S22', 
                   'Marco do produto': 'Samsung',
                   'Valor': 3199,
                   'Qtd. estoque': 3},
    'product122': {'Nome do produto': 'Celular - Xr', 
                   'Marca do produto': 'Apple',
                   'Valor': 2499,
                   'Qtd. estoque': 5},
    'product154': {'Nome do produto': 'Televisão - Smart4K', 
                   'Marco do produto': 'Samsung',
                   'Valor': 3899,
                   'Qtd. estoque': 4},

}




# for eletronic, attribute in stock.items():
#             print()
#             print()
#             print(eletronic)
#             for key, value in attribute.items():
#                 print(f'{key}: {value}')




# stock['chave3'] = {'Name': 'Kaue'}


# LIST VIEW 
# for eletronic, attribute in stock.items():
#     print()
#     print()
#     print(eletronic)
#     for key, value in attribute.items():
#         print(f'{key}: {value}')


# listando opções para o usuário

action = [
    'Choose a number',
    '1 - too add product',
    '2 - remove product',
    '3 - see product of stock',
    '4 - value of stock',
    '5 - Exit'
]


import random

# Gerando um código para o produto

num_1 = str(random.randint(1,9))
num_2 = str(random.randint(1,9))
num_3 = str(random.randint(1,9))
next_product = 'product' + num_1 + num_2 + num_3

while True:
    print()
    print()
    for options in action:
        print(options)

    number_typed = input('Enter a number: ')

    if not number_typed.isdigit():
        print('enter numbers only')
        continue

        
    elif number_typed == '1':
        print()
        # add_product =  input('Enter a product: ')
        name_product =  input('Enter a name of product: ')
        brand_product = input('Enter a brand of product: ')
        value_product = float(input('Enter a value of product: '))
        amount_stock = int(input('Enter a amount of stock: '))


        stock[next_product] = {'Nome do produto': name_product,
                               'Marca do produto': brand_product,
                               'Valor': value_product,
                               'Qtd. estoque': amount_stock}
        
        for eletronic, attribute in stock.items():
            print()
            print()
            print(eletronic)
            for key, value in attribute.items():
                print(f'{key}: {value}')
        
        


    elif number_typed == '2':
        print()
        for eletronic, attribute in stock.items():
            print()
            print(eletronic, '|', attribute['Nome do produto'])
        try:

            product_remove = str(input('Enter the product number to be removed: '))
            product_removed = 'product' + product_remove
            stock.pop(product_removed)

        except KeyError:
            print('Digite o numero de um produto existente!')
            continue
        except:
            print('Digite apenas numero, especificamente de um produto!')

        for eletronic, attribute in stock.items():
                print()
                print(eletronic, '|', attribute['Nome do produto'])



    elif number_typed == '3':
        
        os.system('cls')
        print()
        for eletronic, attribute in stock.items():
            print()
            print()
            print(eletronic)
            for key, value in attribute.items():
                print(f'{key.upper()}: {value}')



    elif number_typed == '4':
        print()
        value_stock = float(0)
        for eletronic, attribute in stock.items():
            stock_product_value = attribute['Valor'] * attribute['Qtd. estoque']
            value_stock += stock_product_value
        print(f'O valor de estoque total é de: R${value_stock}')

        

    elif number_typed == '5':
        break






        
    

