you = 1
total = 0
accept = True

while accept:
  number_peoples = int(input('Número de pessoas, sem contar com você -> '))
  total_peoples = you + number_peoples

  total += total_peoples * 14
  
  accept_break = str.lower(input('Você deseja continuar? S/N -> '))
  if accept_break != 's':
    accept = False
print(total)
