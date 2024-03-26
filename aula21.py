# Operadores lógicos
# and or not
# and - Todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que vc ja viu)
# 0 0.0 '' False
# tambem existe o tipo None que é
# usado para representar um não valor 

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# if condicao:
if entrada == 'E' and senha_digitada == '123456':
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito
# print(True and True and True)
# print(True and '' and True)

