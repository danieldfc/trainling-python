for i in range(1, 11):
  for j in range(1, 11):
    if j == 1:
      print('{:^13}'.format(i))

    multiplicadores = '{} x {}'.format(i,j)
    total = '{}'.format(i*j)
    print('{:<7} = {:>3}'.format(multiplicadores, total))
