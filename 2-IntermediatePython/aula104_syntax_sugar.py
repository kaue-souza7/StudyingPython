# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar Sintático)

def create_function(funcao):
    def interna(*args):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args)
        return resultado
    return interna

@create_function
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('O paramentro deve ser uma string, ou seja você não digitou um número!')

inverte = inverte_string('Kaue')
print(inverte)