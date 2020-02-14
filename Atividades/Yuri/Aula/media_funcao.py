def falta_para_passar(nota1, nota2):
  need_media = 21 - (nota1 + nota2)
  print('O aluno precisa tirar nota mínima "{:.2f}" para passar por média.'.format(need_media))

nota1, nota2 = map(float, input('Digite as notas do aluno separadamente -> ').split())

falta_para_passar(nota1, nota2)
