from random import randrange


def create_lista_letras_palavra(palavra):
    lista_letras_palavra = []

    for i in range(0, len(palavra) - 1):
        lista_letras_palavra.append(palavra[i])

    return lista_letras_palavra


def verify_letra_palavra(palavra, letra):
    for i in range(len(palavra)):
        if letra in palavra[i]:
            return True

    return False


def verify_amount_character(palavra, letra):
    cont = 0
    lista_indices = []

    for i in range(len(palavra)):
        if letra in palavra[i]:
            lista_indices.append(i)
            cont += 1

    return cont, lista_indices


def check_letter_already_entered(lista_letras_informadas, letra):
    cont = 0
    for i in range(len(lista_letras_informadas)):
        if letra in lista_letras_informadas[i]:
            cont += 1
        if cont > 1:
            return True
    return False


initial_life = 1
total_life = 6
amount_palavras = -1


def menu():
    global initial_life, total_life, amount_palavras
    print()
    print('\033[1;33m='*30)
    print(f'{"FORCA":^30}\n')
    print(f'VIDA = {initial_life}')
    print(f'CHANCES = {total_life}')
    print('='*30+'\n')


arquivo = open('arquivos/palavras_forca.txt', 'r')
palavras = arquivo.readlines()

lista_letras_palavras = []
lista_letras = []

for i in range(len(palavras)):
    lista_letras_palavras.append(palavras[i])
    amount_palavras += 1
for j in range(0, len(lista_letras_palavras)):
    lista_letras.append(create_lista_letras_palavra(palavras[j]))

if amount_palavras >= 0:
    menu()
    continuar = True

    while initial_life <= total_life:
        cont_palavra = randrange(0, amount_palavras)

        if continuar:
            cont_letra = 0
            palavra_incompleta = '_' * len(lista_letras[cont_palavra])
            palavra_completa = ''

            lista_letras_informadas = []
            while cont_letra < len(lista_letras[cont_palavra]):
                if initial_life > 6:
                    break
                else:
                    if palavra_completa != '':
                        print(
                            f'\033[1;33mPALAVRA SECRETA -> {palavra_completa}\n')
                    else:
                        print(
                            f'\033[1;33mPALAVRA SECRETA -> {palavra_incompleta}\n')
                    letra = str.lower(
                        input('\033[1;35m> INFORME UMA LETRA -> '))
                    lista_letras_informadas.append(letra)

                    if check_letter_already_entered(lista_letras_informadas, letra) == False:
                        if len(letra) == 1:
                            if verify_letra_palavra(lista_letras[cont_palavra], letra) == False:
                                initial_life += 1
                            else:
                                cont_character, indices = verify_amount_character(
                                    lista_letras[cont_palavra], letra)
                                for indice in indices:
                                    if palavra_completa == '':
                                        palavra_completa = palavra_incompleta[:indice] + \
                                            letra + \
                                            palavra_incompleta[indice+1:]
                                    else:
                                        palavra_completa = palavra_completa[:indice] + \
                                            letra + palavra_completa[indice+1:]
                                cont_letra += cont_character
                            if initial_life <= 6:
                                print(
                                    f'\033[1;36m\nVIDA = {initial_life}\nCHANCES = {total_life}\n')
                                if cont_letra == len(lista_letras[cont_palavra]):
                                    print(
                                        f'\033[1;33mPALAVRA SECRETA -> {palavra_completa}\n')
                        else:
                            print(
                                f'\033[1;36m\nVIDA = {initial_life}\nCHANCES = {total_life}')
                            print(
                                '\033[1;31m\n** Coloque apenas uma letra **\n')
                    else:
                        print(
                            '\033[1;31m\n** LETRA JÁ INFORMADA, TENTE OUTRA **\n')
                if cont_letra == len(lista_letras[cont_palavra]):
                    print('\033[1;32m** CONGRATULATIONS! **\n')
                    option = str.lower(
                        input('\033[1;31m> DESEJA CONTINUAR? S/n -> '))
                    if option != 's':
                        continuar = False
                    else:
                        lista_letras_informadas = []
                        cont_letra = 0
                        cont_palavra = randrange(0, amount_palavras)
                        palavra_incompleta = '_' * \
                            len(lista_letras[cont_palavra])
                        palavra_completa = ''
                        menu()

            if initial_life > 6:
                print('\033[1;36m\n** Suas chances acabaram **\n')
                option = str.lower(
                    input('\033[1;31m> Deseja recomeçar o jogo? S/n -> '))
                if option != 's':
                    continuar = False
                else:
                    lista_letras_informadas = []
                    cont_letra = 0
                    initial_life = 1
                    cont_palavra = randrange(0, amount_palavras)
                    palavra_incompleta = '_'*len(lista_letras[cont_palavra])
                    palavra_completa = ''
                    menu()
        else:
            break

    print('\033[1;33m\n** OBRIGADO PELA PREFERÊNCIA, VOLTE SEMPRE **\n')
else:
    print(
        '\033[1;33m\n** POR FAVOR, VERIFIQUE, SE HÁ PALAVRAS NO ARQUIVO, VOLTE MAIS TARDE! **\n')
