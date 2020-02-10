numero = int(input('Informe um número -> '))
lista = []
cont1 = 0
cont2 = 0

while numero != 0:
  lista.append(numero)
  numero = int(input('Informe um número -> '))

while cont1 < len(lista)-1:
  cont2 = cont1 + 1
  while cont2 < len(lista):
    if lista[cont1] == lista[cont2]:
      lista.pop(cont2)
    else:
      cont2+=1
  cont1+=1
print(lista)
