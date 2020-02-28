def verifyCharacter(palavra):
  cont = 0
  
  for i in palavra:
    if i in 'aeiou':
      cont += 1
  return cont

palavra = input('Informe a palavra a ser verificada -> ')
print('Essa palavra possui {} vogais.'.format(verifyCharacter(palavra)))
