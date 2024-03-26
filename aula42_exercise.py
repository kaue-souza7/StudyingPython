text = 'Hi, my name is Kaue, i do like to play soccer, to study and technology, i love love technology, technology is my life'

i = 0
tamanho_string = len(text)
letra_apareceu_mais_vezes = ''
qtd_letra_apareceu_mais_vezes = 0

while i < tamanho_string:


    letra_atual = text[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = text.count(letra_atual)

    if qtd_letra_atual > qtd_letra_apareceu_mais_vezes:
        qtd_letra_apareceu_mais_vezes = qtd_letra_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezez foi "{letra_apareceu_mais_vezes}" aparecendo {qtd_letra_apareceu_mais_vezes}x')

    