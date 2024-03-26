"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.


- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.


- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


# palavra_secreta = 'empreendorismo'
# tentativas = 0
# chutar_palavra = ''
# palavra_chutada = ''

# while ...:

#     letra_digitada = input('Digite uma letra: ')

#     if letra_digitada in palavra_secreta:
#         tentativas += 1
#         print(f'"{letra_digitada}" // Tentativas: {tentativas}x')
#         chutar_palavra = input('Deseja chutar a palavra? [S]im or [N]ão? ').lower()
#         if chutar_palavra == 's':
#             palavra_chutada = input('Digite a palavra: ')
#             if palavra_chutada == palavra_secreta:
#                 print('Parabéns você acertou a palavra! E ganhou o jogo!')
#             else:
#                 print('Você errou a palavra! E perdeu o jogo')
#         else:
#             continue
        
#     elif letra_digitada not in palavra_secreta:
#         tentativas += 1
#         print(f'* Tentativas: {tentativas}x')

import os

palavra_secreta = 'navio'
letras_acertadas = ''
tentativas  = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1 
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'

    print(palavra_formada)



    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou! Parabéns!')
        print('A palavra era: ', palavra_secreta)
        print('Tentativas: ', tentativas,'x')
        letras_acertadas = ''
        tentativas  = 0
        
        
        
        

