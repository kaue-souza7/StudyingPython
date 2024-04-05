""" Calculadora com while """

# + - / *




while ...:

    print('Deseja continuar?')
    continuar = input(' "S" para continuar ou "N" sair: ').lower()

    if continuar == 'n':
        print('Obrigado por usar a calculadora, até mais!!!!')
        break
        
        

    if continuar == 's':
        num_1 = input('Digite o primeiro numero: ')
        operador = input('Digite um operador: ')
        num_2 = input('Digite o segundo numero: ')
        
        try:
            num_1 = int(num_1)
            num_2 = int(num_2)
        except:
            print('A calculadora deu algum erro, você não deve ter digitado um numero')
            break


        soma = num_1 + num_2
        subtracao = num_1 - num_2
        divisao = num_1 / num_2
        multiplicacao = num_1 * num_2

        if operador == '+':
            print(f'A soma dos numeros é: {soma}')
        elif operador == '-':
            print(f'A subtração dos numeros é: {subtracao}')
        elif operador == '/':
            print(f'A divisão dos numeros é: {divisao}')
        elif operador == '*':
            print(f'A multiplicação dos numeros é: {multiplicacao}')
        else: 
            print('Você nao digitou um operador')
            break

        
    elif continuar == 's':
        print('Okay cvamos continuar')
    else:
        print('digite "S" or "N"')
        continue

        

        




