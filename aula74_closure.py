"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom Dia')
falar_boa_noite = criar_saudacao('Bom NOite')

print(falar_bom_dia('Gael'))
print(falar_boa_noite('Flávia'))

client = ['Carol', 'Arthur', 'Vinicius', 'Kaue', 'Ana', 'Bea', 'João']

for name in client:
#     print(falar_bom_dia(name))

names = ['Carol', 'Arthur', 'Vinicius', 'Kaue', 'Ana', 'Bea', 'João', 'Lara']

def saudacao(saudacao):
    def print(name):
        return f'{saudacao}, {name}'
    return print

saudacao_1 = saudacao('Bom dia')
saudacao_2 = saudacao('Boa Tarde')
saudacao_3 = saudacao('Boa noite')

# print(saudacao_1('Kauê'))
# print(saudacao_2)
# print(saudacao_3('Julia'))

for name in names:
    # print(saudacao_1(name))
    print(saudacao_2(name))
    # print(saudacao_3(name))
    



