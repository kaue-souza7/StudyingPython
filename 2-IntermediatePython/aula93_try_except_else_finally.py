# Try, except, else, finally
# ////**** POSSO COLOCAR QUANTOS EXCEPT FOR PRECISO ****\\\\

a = 0
# b = 2
# print(b / a)

try:
    a = 0
    # b = 2
    print(a / b)
except ZeroDivisionError:
    print('Não é possivel dividir por zero!')
# except NameError:
#     print('Alguma variavel não existe!')
except (Exception, NameError) as error:
    print(f'{error}, ' 
          'Alguma variavel não existe!')
    print(error.__class__.__name__)



