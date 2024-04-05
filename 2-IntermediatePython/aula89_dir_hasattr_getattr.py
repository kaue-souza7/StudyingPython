# dir, hasattr, getattr em Python
string = 'Luiz'
metodo = 'upper'
if hasattr(string, metodo):
    print('SIM')
    print(getattr(string, metodo)())
    # print(string)
else:
    print('Não existe o metodo', metodo)

# string.zfill(10)
print(string.zfill(10))