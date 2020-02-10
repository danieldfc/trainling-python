month, year = map(int, input('Digite um mês e o ano: ').split())

if month > 0 and month <= 12:
  if month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
  else:
    if month == 2:
      if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        print(29)
      else:
        print(28)
    else:
      print(31)
else:
  print('Não existe no nosso calendário')

#1  - janeiro   - 31
#2  - fevereiro - 28 | 29
#3  - março     - 31
#4  - abril     - 30
#5  - maio      - 31
#6  - junho     - 30
#7  - julho     - 31

#8  - agosto    - 31
#9  - setembro  - 30
#10 - outubro   - 31
#11 - novembro  - 30
#12 - dezembro  - 31