def retirar_vogais(texto):
  resultado = ''

  for i in range(len(texto)):
    if texto[i] not in 'aeiou':
      resultado += texto[i]

  return resultado

print(retirar_vogais('estudar'))
