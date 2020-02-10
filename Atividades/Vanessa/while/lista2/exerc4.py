total = 0

while True:
  quant_carros = int(input('Quantidade de carros -> '))
  if quant_carros != 555:
    if quant_carros > 2:
      calc_total = 0
      for i in range(3, quant_carros + 1):
        calc_total += 10
      total += calc_total
      print(calc_total)
    else:
      print(0)
  else:
    print(total)
    break