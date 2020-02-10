def media(nota1, nota2, nota3: float):
  return (nota1 + nota2 + nota3) / 3

nota1 = float(input('Insira a primeira nota do aluno -> '))
nota2 = float(input('Insira a segunda nota do aluno -> '))
nota3 = float(input('Insira a terceira nota do aluno -> '))

mediaBimestral = round(media(nota1, nota2, nota3), 2)

print('\nMédia = {}\n'.format(mediaBimestral))

if (mediaBimestral > 10):
  print('A sua média está incorreta no bimestre, verifique seus dados.\n')
elif (mediaBimestral <= 10):
  if(mediaBimestral >= 7 and mediaBimestral <= 10):
    print('A sua média está aprovada no bimestre.\n')
  elif (mediaBimestral >= 4 and mediaBimestral < 7):
    print('A sua média está reprovada no bimestre, mas com direito a reposição.\n')
  else:
    print('A sua média está reprovada no bimestre, mas sem direito a reposição.\n')
