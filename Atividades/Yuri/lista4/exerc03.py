numero = int(input('Informe um número -> '))
lista = []
cont = 0

maior = 0
menor = 0

while numero != 0:
  lista.append(numero)
  if cont == 0:
    maior = menor = numero
  else:
    if numero > maior:
      maior = numero
    if numero < menor:
      menor = numero
  cont+=1
  numero = int(input('Informe um número -> '))

print('Maior: {}\nMenor: {}'.format(maior, menor))
print('Lista: {}'.format(lista))