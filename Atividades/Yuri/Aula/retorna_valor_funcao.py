def repet_numbers(number, quant):
  lista = []
  for i in range(quant):
    lista.append(number)
  return lista

number = int(input('\033[0;33mDigite o número que será repetido -> '))
quant = int(input('\033[0;33mDigite a quantidade de vezes que irá ser repetido -> '))

resultado = repet_numbers(number, quant)

print('\033[0;32m> Lista = {}'.format(resultado))
