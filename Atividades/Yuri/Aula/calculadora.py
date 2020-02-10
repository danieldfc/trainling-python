fim = True

while fim:
  print('----- Calculadora -----\n')
  print('+ - Adição')
  print('- - Subtração')
  print('* - Multiplicação')
  print('/ - Divisão')
  print('\nDigite separadamente: (operando) (operador) (operando)')

  numberOne, opcao, numberTwo = map(str, input("-> ").split())

  numberOne = float(numberOne)
  numberTwo = float(numberTwo)

  if opcao == '+':
    calc_soma = numberOne + numberTwo
    print('A adição entre {} e {} é igual a: {}'.format(numberOne, numberTwo, calc_soma))
    repetir = str.upper(input('Você deseja repetir? S/N -> '))
    if repetir != 'S':
      fim = False
      print('Até mais tarde!')
  elif opcao == '-':
    calc_subtracao = numberOne - numberTwo
    print('A subtração entre {} e {} é igual a: {}'.format(numberOne, numberTwo, calc_subtracao))
    repetir = str.upper(input('Você deseja repetir? S/N -> '))
    if repetir != 'S':
      fim = False
      print('Até mais tarde!')
  elif opcao == '*':
    calc_multiplicacao = numberOne * numberTwo
    print('A multiplição entre {} e {} é igual a: {}'.format(numberOne, numberTwo, calc_multiplicacao))
    repetir = str.upper(input('Você deseja repetir? S/N -> '))
    if repetir != 'S':
      fim = False
      print('Até mais tarde!')
  elif opcao == '/':
    calc_divisao = numberOne / numberTwo
    print('A divisão entre {} e {} é igual a: {}'.format(numberOne, numberTwo, calc_divisao))
    repetir = str.upper(input('Você deseja repetir? S/N -> '))
    if repetir != 'S':
      fim = False
      print('Até mais tarde!')
  else:
    print('\nOpção inválida :(\n')