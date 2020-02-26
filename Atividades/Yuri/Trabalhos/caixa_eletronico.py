def menu():
  print('\033[0;33m='*30)
  print('{:^30}'.format('CAIXA ELETRÔNICO'))
  print('='*30+'\n')
  print('1 - CARREGAR CAIXA ELETÔNICO')
  print('2 - SACAR DINHEIRO')
  print('3 - SAIR\n')
  opc = int(input('Opção -> '))

  return opc

def checkTotalNotas(totalCed, ced):
  if ced == 100:
    if totalCed > amountCem:
      return False
  elif ced == 50:
    if totalCed > amountCinquenta:
      return False
  elif ced == 20:
    if totalCed > amountVinte:
      return False
  elif ced == 5:
    if totalCed > amountCinco:
      return False

  return True

def checksQuantityOfBanknotes(money):
  total = money

  totalCedulasCem = 0
  totalCedulasCinquenta = 0
  totalCedulasVinte = 0
  totalCedulasCinco = 0

  ced = 100

  while True:
    if total >= ced:
      total -= ced
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

      if total == 0:
        break

  return totalCedulasCem, totalCedulasCinquenta, totalCedulasVinte, totalCedulasCinco

amountCem = 0
amountCinquenta = 0
amountVinte = 0
amountCinco = 0

opc = menu()

while opc > 0 and opc < 4:
  if opc == 1:
    quantCem, quantCinquenta, quantVinte, quantCinco = map(int,
      input('Digite a quantidade de notas separadamente, os ' +
        'tipos são: (100, 50, 20, 5) -> ').split())
    
    amountCem += quantCem
    amountCinquenta += quantCinquenta
    amountVinte += quantVinte
    amountCinco += quantCinco

    print('\033[0;32m\nO caixa eletrônico armazenou as notas!\n')
  elif opc == 2:
    if amountCem == 0 and amountCinquenta == 0 and amountVinte == 0 and amountCinco == 0:
      print('\033[0;31m\nNão possui recursos para fazer o saque!\n')
    else:
      totalSaque = int(input('Informe qual o valor que você quer sacar -> R$'))
      quantCem, quantCinquenta, quantVinte, quantCinco = checksQuantityOfBanknotes(totalSaque)
      if not checkTotalNotas(quantCem, 100) or not checkTotalNotas(quantCinquenta, 50) or not checkTotalNotas(quantVinte, 20) or not checkTotalNotas(quantCinco, 5):
        print('\033[0;31m\nNão possui recursos para fazer o saque!\n')
      else:
        amountCem -= quantCem
        amountCinquenta -= quantCinquenta
        amountVinte -= quantVinte
        amountCinco -= quantCinco
        
        print('\033[0;32m\nSaque feito com sucesso!\n')
  elif opc == 3:
    print('\033[0;32m\nObrigado pela preferência, volte sempre!\n')
    exit()  
  opc = menu()

print('\033[0;31m\nOpção inválida!\n')
