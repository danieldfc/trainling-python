numero = int(input('Informe um número -> '))
maior = 0
segundo_maior = 0
opcao = True

while opcao:
  if numero > maior:
    segundo_maior = maior
    maior = numero
  elif numero > segundo_maior:
    segundo_maior = numero
  opcaoUser = str.upper(input('Você deseja continuar? S (Sim) / N(não) ->'))
  if opcaoUser != 'S':
    opcao = False
  else:
    numero = int(input('Informe um número -> '))
print(segundo_maior)
