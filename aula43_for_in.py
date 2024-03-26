# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

texto = 'HI, i am Kaue, how are you?'

letra_mais_repetida = ''
qtd_letra_mais_repetida = 0

for letra in texto:

    letra_atual = letra

    if letra_atual == ' ':
        continue

    qtd_atual = texto.count(letra_atual)
    
    if qtd_atual > qtd_letra_mais_repetida:
        qtd_letra_mais_repetida = qtd_atual
        letra_mais_repetida = letra_atual
    



print(letra_mais_repetida)
print(qtd_letra_mais_repetida)
    

