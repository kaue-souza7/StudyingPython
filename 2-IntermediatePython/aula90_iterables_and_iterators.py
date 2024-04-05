import sys

# Generator expression, Iterables and Iterators in Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter e _next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

generator = (n for n in range(100))
lista = [n for n in range(1000000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))
# for n in generator:
#     if n <= 500:
#         print(n)

for n in generator:
    if n < 50:
        print(n)
        
    

# print('parou aqui', sys.getsizeof(generator))