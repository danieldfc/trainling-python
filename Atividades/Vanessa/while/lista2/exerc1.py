contador = 0

while True:
  letra = str.upper(input('Qual a letra? '))
  if letra != 'X':
    if letra == 'K' or letra == 'Y' or letra == 'W':
      contador+=1
  else:
    print(contador)
    break