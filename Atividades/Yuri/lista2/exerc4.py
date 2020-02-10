number1, number2, number3 = map(int, input('Digite os números separadamente: ').split())

if number1 > number2 and number1 > number3:
  if number2 > number3:
    print(number1, number2, number3)
  else:
    print(number1, number3, number2)
if number2 > number1 and number2 > number3:
  if number1 > number3:
    print(number2, number1, number3)
  else:
    print(number2, number3, number1)
if number3 > number1 and number3 > number2:
  if number1 > number2:
    print(number3, number1, number2)
  else:
    print(number3, number2, number1)
