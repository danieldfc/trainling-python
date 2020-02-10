# questão 1
valorProduto=0
media=0
maiorValor=0
destaqueProduto = ""
destaqueAnoProduto=0
quantValiosos = 0
numero = int(input("quantos produtos vc vai verificar --> "))

for i in range(numero):
  nomeProduto = input("Nome do produto --> ")
  valorProduto = float(input("Valor do produto --> "))
  anoProduto = int(input("Ano do produto --> "))
  if anoProduto < 1827:
    quantValiosos+=1
  if(valorProduto > maiorValor):
    maiorValor = valorProduto
    destaqueNomeProduto = nomeProduto
    destaqueAnoProduto = anoProduto
  media += valorProduto
media /= numero
print("QuantValioso: {}\nMedia: {}\nDestaqueProduto: {}\nDestaqueAnoProduto: {}".format(
    quantValiosos,
    media,
    destaqueNomeProduto,
    destaqueAnoProduto
  )
)