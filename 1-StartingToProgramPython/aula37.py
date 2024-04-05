"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um codigo nao tem fim
"""

contador = 0

while contador < 100:
    contador += 1
    
    if contador > 30 and contador <= 39:
        continue
    print(contador)
    

    if contador == 40:
        break

    
    

print('Acabou')