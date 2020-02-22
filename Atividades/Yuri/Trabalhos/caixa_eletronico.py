import sys

def menu():
  print('='*30)
  print('{:^30}'.format('CAIXA ELETRÔNICO'))
  print('='*30+'\n')
  print('1 - CARREGAR CAIXA ELETÔNICO')
  print('2 - SACAR DINHEIRO')
  print('3 - SAIR\n')
  opc = int(input('Opção -> '))

  return opc

def checksQuantityOfBanknotes(money):
  totalCedulasCem = 0
  totalCedulasCinquenta = 0
  totalCedulasVinte = 0
  totalCedulasCinco = 0

  ced = 100

  while True:
    if money >= ced:
      money -= ced
      if ced == 100:
        totalCedulasCem += 1
      elif ced == 50:
        totalCedulasCinquenta += 1
      elif ced == 20:
        totalCedulasVinte += 1
      elif ced == 5:
        totalCedulasCinco += 1
    else:
      if ced == 100:
        ced = 50
      elif ced == 50:
        ced = 20
      elif ced == 20:
        ced = 5
      if money == 0:
        break

  return totalCedulasCem, totalCedulasCinquenta, totalCedulasVinte, totalCedulasCinco

opc = menu()

amountCem = 0
amountCinquenta = 0
amountVinte = 0
amountCinco = 0

while opc > 0 and opc < 4:
  if opc == 1:
    quantCem, quantCinquenta, quantVinte, quantCinco = map(int, input('Digite a quantidade de notas separadamente, os tipos são: (100, 50, 20, 5) -> ').split())
    amountCem += quantCem
    amountCinquenta += quantCinquenta
    amountVinte += quantVinte
    amountCinco += quantCinco
    print('O caixa eletrônico armazenou as notas!')
  elif opc == 2:
    if amountCem == 0 and amountCinquenta == 0 and amountVinte == 0 and amountCinco == 0:
      print('Não possui recursos para fazer o saque!\n')
    else:
      money = int(input('Informe qual o valor que você quer sacar -> R$'))
      quantCem, quantCinquenta, quantVinte, quantCinco = checksQuantityOfBanknotes(money)

      if quantCem <= amountCem and quantCinquenta <= amountCinquenta and quantVinte <= amountVinte and quantCinco <= amountCinco:
        amountCem -= quantCem
        amountCinquenta -= quantCinquenta
        amountVinte -= quantVinte
        amountCinco -= quantCinco
        print('Saque feito com sucesso!')
      else:
        print('Não possui recursos para fazer o saque!\n')


  elif opc == 3:
    print('Obrigado pela preferência, volte sempre!')
    sys.exit(0)

  opc = menu()
