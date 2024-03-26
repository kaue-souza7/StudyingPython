# Operadores lógicos
# and / or / not
# or - Qualquer condição verdadeira avalia 
# toda a expressão como verdadeiras.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que vc ja viu)
# 0 0.0 '' False
# tambem existe o tipo None que é
# usado para representar um não valor 


entrada = input('[E]ntrar [S]air: ')

if entrada == 's' or entrada == 'S':
    print('Saiu')

senha_digitada = input('Senha: ')


senha_permitida = '123456'

# if condicao:
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    
    print('Entrar')
elif entrada == 'S' or entrada == 's':
    print('Sair')
else:
    print('Tente novamente')


# Avaliação de curto circuito
# print(False or False or 0 or 'abc')

