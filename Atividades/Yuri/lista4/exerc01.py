numero = int(input('Informe um número -> '))
cont = 0
lista = []

while cont <= numero:
  if cont % 2 != 0:
    lista.append(cont)
  cont+=1
print(lista) 