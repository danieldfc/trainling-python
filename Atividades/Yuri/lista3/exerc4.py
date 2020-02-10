total = 0
numero = int(input('Digite um número -> '))

while numero != 0:
    total += numero
    numero = int(input('Digite um número -> '))
print('\33[32mTotal = {}'.format(total), end='')
