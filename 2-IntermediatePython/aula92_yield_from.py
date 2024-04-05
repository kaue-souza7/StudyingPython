# yield from 
def generator1():
    print('COMEÇOU generator1')
    yield 1
    yield 2
    yield 3
    print('TERMINOU generator1')


def generator2(gen):
    print('COMEÇOU generator2')
    yield from gen
    yield 3
    yield 2
    yield 1
    print('TERMINOU generator2')
    


gen = generator2(generator1())

print('ASSIM')
for n in gen:
    print(n)

gen = generator2(generator1())

print()
print()
print()
print('OU')
print()
print()
print()

print('ASSIM')
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


