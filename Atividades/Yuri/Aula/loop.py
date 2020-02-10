n=int(input('Digite um número: '))
contador1=0
contador2=0

while contador1 < n:
  while contador2 < n:
    print('@', end="")
    contador2+=1
  print('')
  contador2=0
  contador1+=1