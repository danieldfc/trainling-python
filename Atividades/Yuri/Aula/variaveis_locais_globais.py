# Escopo é uma parte do programa que determinados identificadores
# só existe nele mesmo

desconto = 0

def troco(pago, total):
  resultado = total - pago + desconto
  return resultado

print(troco(12, 10))
print(desconto)
