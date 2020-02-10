cont = 1
numero = int(input('Digite um número -> '))
total = 0

while cont <= numero:
  if numero % cont == 0:
    print('\33[33m', end='')
    total += 1
  else:
    print('\33[31m', end='')
  print('{} '.format(cont), end='')
  cont += 1
print('\n\33[mO número {} foi divisível {} vezes'.format(numero, total))

if total == 2:
  print('Então ele é primo.')
else:
  print('Então ele não é primo.')
