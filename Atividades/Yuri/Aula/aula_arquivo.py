produtos = open('arquivos/listadecompras.txt', 'r')
# texto = produtos.read() ler todo conteudo
# texto = produtos.read(5) ler caracteres
# texto = produtos.readlines() ler e coloca dentro de uma lista as linhas
# texto = produtos.readline() ler a linha e pula para a proxima
linha = produtos.readline()

while linha != '':
    print(linha)
    linha = produtos.readline()

produtos.close()
