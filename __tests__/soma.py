def soma(first, second: int):
  return first + second

x = int(input('Qual o primeiro valor? '))
y = int(input('Qual o segundo valor? '))

result = soma(x, y)

print('O resultado de', x, "+", y, 'é', result)
