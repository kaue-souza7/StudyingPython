# Example de uso de set's
letras = set()
while True:
    letra = input('Digite a letra: ')
    if len(letra) > 1 or letra == ' ' or letra.isdigit():
        print('Não digite mais que uma letra, '
              'numero nem espaços vazios!')
        continue
    letras.add(letra)

    print(letras)
    