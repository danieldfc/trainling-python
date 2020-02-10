numero = int(input('Informe um número -> '))
lista = []
cont = 0
contador = 0

while numero != 0:
  lista.append(numero)
  numero = int(input('Informe um número -> '))

numero = int(input('\nDigite um número para verificar -> '))
while cont < len(lista):
  if lista[cont] == numero:
    contador += 1
  cont+=1

print(contador)
