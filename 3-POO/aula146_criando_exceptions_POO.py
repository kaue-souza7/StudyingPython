# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...

class OtherError(Exception):
    ...


def levantar():
    exception = MyError('a', 'b', 'c')
    exception.add_note('Olha a nota 1')
    exception.add_note('Voce errou isso')
    raise exception

try:
    levantar()
except (MyError, Exception) as error:
    print
    print(error)
    exception = OtherError('Vou lançar de novo')
    exception.add_note('Mais uma nota')
    exception.__notes__ += error.__notes__.copy()
    
    raise exception from error