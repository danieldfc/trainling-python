precoGasolina = 2.53
precoEtanol = 2.09
precoDiesel = 1.92

resultLitros = 0

optionUser = int(input('Qual a opção? (1) Gasolina | (2) Etanol | (3) Diesel: '))

valorOption = float(input('Quanto? '))

if (optionUser == 1):
  resultLitros = valorOption / precoGasolina
  print('O preço total de {} foi de: {:.2f}'.format(valorOption, resultLitros))
  print('Não ganho a troca de óleo')
if (optionUser == 2):
  resultLitros = valorOption / precoEtanol
  print('O preço total de {} foi de: {:.2f}'.format(valorOption, resultLitros))
  if resultLitros > 30:
    print('Ganhou troca de óleo')
  else:
    print('Não ganho a troca de óleo')
if (optionUser == 3):
  resultLitros = valorOption / precoDiesel
  print('O preço total de {} foi de: {:.2f}'.format(valorOption, resultLitros))
  print('Não ganho a troca de óleo')
