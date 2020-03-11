def soma(lista1, lista2):
    resultado = []

    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])

    return resultado


def diferenca(lista1, lista2):
    resultado = []

    for i in range(len(lista1)):
        resultado.append(lista1[i] - lista2[i])

    return resultado
