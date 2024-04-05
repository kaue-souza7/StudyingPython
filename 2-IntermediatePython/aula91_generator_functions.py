#Introdução às Generator functions em python
# generator = (n for n in range(10000))


def contador_generator(limite):
    n = 0
    while n < limite:
        yield n
        n += 10
# for n in contador_generator(100):
#     print(n)
        
cont = contador_generator(100000000)
print(next(cont))
print(next(cont))