myWeight = float(input('Seu peso: '))
myHeight = float(input('Sua altura: '))

calcImc = myWeight / (myHeight * myHeight)

print('Seu imc é {:.2f}'.format(calcImc))

if calcImc < 15 and calcImc > 0:
  print('Extremamente abaixo do peso')
elif calcImc >= 15 and calcImc < 16:
  print('Gravimente abaixo do peso')
elif calcImc >= 16 and calcImc < 18.5:
  print('Abaixo do peso ideal')
elif calcImc >= 18.5 and calcImc < 25:
  print('Faixa de peso ideal')
elif calcImc >= 25 and calcImc < 30:
  print('Sobrepeso')
elif calcImc >= 30 and calcImc < 35:
  print('Obesidade grau I')
elif calcImc >= 35 and calcImc < 40:
  print('Obesidade grau II (grave)')
elif calcImc >= 40:
  print('Obesidade grau III (mórbida)')
else:
  print('Verifique seus dados')