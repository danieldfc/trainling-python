cont1 = 1
cont2 = 1

while cont1 <= 9:
  print('-'*12)
  while cont2 <= 10:
    print('{} x {:2} = {}'.format(cont1, cont2, cont1*cont2))
    cont2+=1
  cont2=1
  cont1+=1