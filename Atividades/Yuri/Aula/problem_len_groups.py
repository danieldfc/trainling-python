def fatorial(number):
  fatorial = 1
  for i in range(1, number + 1):
    fatorial = i * fatorial

  return fatorial

def combination(turmaTotal, quantPessoa):
  return fatorial(turmaTotal)//(fatorial(quantPessoa)*fatorial((turmaTotal - quantPessoa)))

print(combination(15, 3))
