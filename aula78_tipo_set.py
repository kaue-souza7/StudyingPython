# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.



# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = () # set vazio
# s1 = {'Luiz', 1, 2, 3} # set com dados
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# li = [1, 2, 3, 3, 3, 3, 3, 1]
# print(li)
# s1 = set(li)
# print(s1)
# l2 = list(s1)
# tp = (4, 5, 6, (7, 8, 9,))
# s1 = {1, 2, 3, tp}
# print(s1)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# print(s1)
# s1.update(('Selma',))
# print(s1)
# s1.discard('Selma')
# print(s1)



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print(s3)
print(s4)
print(s5)
print(s6)
