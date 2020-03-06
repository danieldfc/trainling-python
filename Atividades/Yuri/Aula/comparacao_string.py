nomes = ['erick', 'saulo', 'amanda', 'lucas', 'roberta']

def ordenar(lista):
  for j in range(len(lista) - 1):
    for i in range(len(lista) - 1 - j):
      if nomes[i] > nomes[i+1]:
        aux = nomes[i+1]
        nomes[i+1] = nomes[i]
        nomes[i] = aux
  return lista

print(ordenar(nomes))
# def ordenar(nome_x, nome_y, nome_z):
  
#   if nome_x < nome_y and nome_x < nome_z:
#     if nome_y < nome_z:
#       print(nome_x, nome_y, nome_z)
#     else:
#       print(nome_x, nome_z, nome_y)
#   elif nome_y < nome_x and nome_y < nome_z:
#     if nome_x < nome_z:
#       print(nome_y, nome_x, nome_z)
#     else:
#       print(nome_y, nome_z, nome_x)
#   else:
#     if nome_x < nome_y:
#       print(nome_z, nome_x, nome_y)
#     else:
#       print(nome_z, nome_y, nome_x)

# ordenar('daniel', 'amanda', 'ighor')