 # Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

'''
A partir do asterisco so entra argumentos nomeados
TUDO ANTES DO * É POSITIONAL
TUDO DEPOIS É NOMEADOS
'''
def soma(a, y, /, *, C):
    print(a + y)

try:
    soma(a=3, y=2)
except TypeError:
    raise TypeError('positional arguments are not allowed')
