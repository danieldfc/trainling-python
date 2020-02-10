continuar = ''

tipoArtista = str.lower(input('Informe o tipo do artista (Banda - Solo) -> '))
valorDiurno = 120
valorNoturno = 200
valorSoloAny = 100
total = 0

while continuar != 'nao':
  horaInicio = int(input('Informe a data de início da gravação -> '))
  duracaoRec = int(input('Informe o tempo de gravação -> '))
  duracaoRecTotal = 0
  
  duracaoRecTotal += duracaoRec
  
  if tipoArtista == 'banda':
    if horaInicio >= 6 and horaInicio < 17:
      total += duracaoRec * valorDiurno
    else:
      total += duracaoRec * valorNoturno
  elif tipoArtista == 'solo':
    total += duracaoRec * valorSoloAny
  continuar = str.lower(input('Deseja continuar? (sim/nao) -> '))
print('> Total=', total)