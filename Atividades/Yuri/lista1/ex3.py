km, litro = map(float, input('Digite os valores separadamente: ').split())

consumo = km / litro

print('O seu consumo de {}km/{}l é {:.2f}'.format(km, litro, consumo))