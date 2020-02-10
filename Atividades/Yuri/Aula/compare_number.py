x, y = map(float, input('Digite os valores separadamente: ').split())

if x == y:
  print('São iguais.')
else:
  if x > y:
    print('x é maior', x)
  else:
    print('y é maior', y)
