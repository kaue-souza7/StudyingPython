convidados = ['Gabreil', 'Lucas', 'Caio', 'Carol', 'Laura', 'Maria'] 
print(f'Sua lista a seguir: ', end="\n" 
      f'{convidados}')
print(end='\n')

acao = input('Você deseja: '
             '1 - Inserir // '
             '2 - Substituir // '
             '3 - Deletar: ' 
             '')


if acao == '1':
    insercao = input('Digite o nome para colocar: ')
    convidados.append(insercao)
    print('O nome foi inserido com sucesso!', end='\n' 
            f'{convidados}')
elif acao == '2':
    indice_subs = input('Começando da esquerda pra direita digite o numero da pessoa que deseja mudar! ')
    print(f'A pessoa selecionada para a substituição é: {convidados[int(indice_subs) - 1]}')
    nome_subs = input('Digite o nome que queira colocar no lugar:')
    convidados[int(indice_subs) - 1] = nome_subs
    print(f'Sua lista atualizada é: {convidados}')
elif acao == '3':
    indice_del = input('Começando da esquerda pra direita digite o numero da pessoa que deseja deletar! ')
    print(f'A pessoa selecionada para a exclusão é: {convidados[int(indice_del) - 1]}')
    pessoa_deletada = convidados[int(indice_del) - 1]
    convidados.pop(pessoa_deletada)
    print('Sua lista atualizada é:', convidados)
else:
    print('Digite apenas 1, 2 ou 3!')

