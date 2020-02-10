contador = 0

while True:
  year = int(input('Qual o ano? '))
  if year > 0:
    if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
      contador += 1
  else:
    print(contador)
    break