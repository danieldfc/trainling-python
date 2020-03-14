numeros = open('arquivos/numeros.txt')
linhas = numeros.readlines()

soma = 0
texto = ''
for numero in linhas:
    soma += int(numero)

print(soma)
numeros.close()
