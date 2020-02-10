accept = True
numeros = 0

while accept:
  numero = int(input('Qual o número? -> '))
  if numero % 3 == 0:
    numeros += numero
  accept_break = str.lower(input('Você deseja continuar? S/N -> '))
  if accept_break != 's':
    accept = False
print(numeros)
