contador = 0
numeros_pares = 0

while True:
  number = int(input('Qual o número? '))
  if number != 100:
    if number % 2 == 0:
      contador += 1
      numeros_pares += number
  else:
    if contador == 0:
      print('Não foram lidos números pares')
    else:
      media = numeros_pares/contador
      print(media)
    break