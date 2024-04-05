




primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')


if primeiro_valor > segundo_valor:
    print(
           f'{primeiro_valor = }'
           f' é maior do que '
           f'{segundo_valor = }'
          )
elif segundo_valor > primeiro_valor:
     print( 
            f'{segundo_valor=}'
            f' é maior do que '
            f'{primeiro_valor=}'
           )
else:
     print(f'Os valores {primeiro_valor=} e {segundo_valor=} são iguais')  

