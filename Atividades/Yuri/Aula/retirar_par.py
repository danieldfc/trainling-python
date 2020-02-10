lista = [10, 5, 3, 12, 4, 19]
cont = 0
while cont < len(lista):
  if lista[cont] % 2 == 0:
    lista.pop(cont)
  else:
    cont += 1
print(lista)