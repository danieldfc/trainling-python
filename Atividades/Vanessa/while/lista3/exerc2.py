cont = 0
accept = True

while accept:
  age = int(input('Idade da pessoa -> '))
  if age <= 10 or age > 60:
    cont += 1
  accept_break = str.lower(input('Você deseja continuar? S/N -> '))
  if accept_break != 's':
    accept = False
print(cont)