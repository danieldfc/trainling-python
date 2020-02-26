saque = int(input('Digite o valor do saque: '))

if saque < 2 or saque == 3:
    print('Valor inválido!')

cem = int(saque/100)
saque = saque % 100
    
cinquenta = int(saque/50)
saque = saque % 50

vinte = int(saque/20)
saque = saque % 20

dez = int(saque/10)
saque = saque % 10

cinco = int(saque/5)
saque = saque % 5

dois = int(saque/2)
saque = saque % 2

print('{} Nota(s) R$ 100,00.' .format(cem))
print('{} Notas(s) R$ 50,00.' .format(cinquenta))
print('{} Notas(s) R$ 20,00.' .format(vinte))
print('{} Notas(s) R$ 10,00.' .format(dez))
print('{} Notas(s) R$ 5,00.' .format(cinco))
print('{} Notas(s) R$ 2,00.' .format(dois))