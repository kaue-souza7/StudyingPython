"""
Crie uma função que receba dois números como parâmetros e retorne a soma deles.
 Em seguida, utilize escopos de variáveis 
para armazenar o resultado e exibi-lo.

"""
num_1 = input('Digite um numero: ')
num_2 = input('Digite outro numero: ')
soma = 0
try:
    int_num_1 = int(num_1)
    int_num_2 = int(num_2)

    soma = int_num_1 + int_num_2
    print(f'A soma dos numeros digitados é: {soma}')

except:
    print('Digite apenas numeros!')







