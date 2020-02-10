number = int(input('\033[1;33mInforme um número -> '))

orderedList = []

while number != 0:
  for index, value in enumerate(orderedList):
    if number < value:
        orderedList.insert(index, number)
        break
  else:
      orderedList.append(number)
  number = int(input('\033[1;33mInforme um número -> '))

print('\033[1;32m> Lista = \033[0;31m{}'.format(orderedList))
