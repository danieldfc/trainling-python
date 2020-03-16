from random import randrange


def create_list_letters_word(word):
    list_letters_word = []

    for i in range(0, len(word) - 1):
        list_letters_word.append(word[i])

    return list_letters_word


def verify_letter_word(word, letter):
    for i in range(len(word)):
        if letter in word[i]:
            return True

    return False


def verify_amount_character(word, letter):
    cont = 0
    list_indexes = []

    for i in range(len(word)):
        if letter in word[i]:
            list_indexes.append(i)
            cont += 1

    return cont, list_indexes


def check_letter_already_entered(list_letters_informed, letter):
    cont = 0
    for i in range(len(list_letters_informed)):
        if letter in list_letters_informed[i]:
            cont += 1
        if cont > 1:
            return True
    return False


life = 1
canches = 6
amount_words = -1


def menu():
    global life, canches, amount_words
    print()
    print('\033[1;33m='*30)
    print(f'{"FORCE":^30}\n')
    print(f'LIFE = {life}')
    print(f'CHANCES = {canches}')
    print('='*30+'\n')


arquivo = open('arquivos/palavras_forca.txt', 'r')
words = arquivo.readlines()

list_letters_words = []
list_letters = []

for i in range(len(words)):
    list_letters_words.append(words[i])
    amount_words += 1
for j in range(0, len(list_letters_words)):
    list_letters.append(create_list_letters_word(words[j]))

if amount_words >= 0:
    menu()
    continuar = True

    while life <= canches:
        cont_word = randrange(0, amount_words)

        if continuar:
            cont_letter = 0
            word_incomplete = '_' * len(list_letters[cont_word])
            word_complete = ''

            list_letters_informed = []
            while cont_letter < len(list_letters[cont_word]):
                if life > 6:
                    break
                else:
                    if word_complete != '':
                        print(
                            f'\033[1;33mWORD SECRET -> {word_complete}\n')
                    else:
                        print(
                            f'\033[1;33mWORD SECRET -> {word_incomplete}\n')
                    letter = str.lower(
                        input('\033[1;35m> REPORT A LETTER -> '))
                    list_letters_informed.append(letter)

                    if check_letter_already_entered(list_letters_informed, letter) == False:
                        if len(letter) == 1:
                            if verify_letter_word(list_letters[cont_word], letter) == False:
                                life += 1
                                canches -= 1
                            else:
                                cont_character, indexes = verify_amount_character(
                                    list_letters[cont_word], letter)
                                for indice in indexes:
                                    if word_complete == '':
                                        word_complete = word_incomplete[:indice] + \
                                            letter + \
                                            word_incomplete[indice+1:]
                                    else:
                                        word_complete = word_complete[:indice] + \
                                            letter + word_complete[indice+1:]
                                cont_letter += cont_character
                            if life <= 6:
                                print(
                                    f'\033[1;36m\nLIFE = {life}\nCHANCES = {canches}\n')
                                if cont_letter == len(list_letters[cont_word]):
                                    print(
                                        f'\033[1;33mWORD SECRET -> {word_complete}\n')
                        else:
                            print(
                                f'\033[1;36m\LIFE = {life}\nCHANCES = {canches}')
                            print(
                                '\033[1;31m\n** PLEASE ENTER ONLY ONE LETTER **\n')
                    else:
                        print(
                            '\033[1;31m\n** LETTER ALREADY INFORMED, TRY ANOTHER **\n')
                if cont_letter == len(list_letters[cont_word]):
                    print('\033[1;32m** CONGRATULATIONS! **\n')
                    option = str.lower(
                        input('\033[1;31m> DO YOU WISH TO CONTINUE? Y/n -> '))
                    if option != 'y':
                        continuar = False
                    else:
                        list_letters_informed = []
                        cont_letter = 0
                        cont_word = randrange(0, amount_words)
                        word_incomplete = '_' * \
                            len(list_letters[cont_word])
                        word_complete = ''
                        menu()

            if canches == 0:
                print('\033[1;36m\n** YOUR CHANCES ARE OVER **\n')
                option = str.lower(
                    input('\033[1;31m> WANT TO RESTART THE GAME? Y/n -> '))
                if option != 'y':
                    continuar = False
                else:
                    list_letters_informed = []
                    cont_letter = 0
                    life = 1
                    canches = 6
                    cont_word = randrange(0, amount_words)
                    word_incomplete = '_'*len(list_letters[cont_word])
                    word_complete = ''
                    menu()
        else:
            break

    print('\033[1;33m\n** THANK YOU FOR PREFERENCE, ALWAYS COME BACK! **\n')
else:
    print(
        '\033[1;33m\n** PLEASE CHECK, IF THERE ARE WORDS IN THE FILE, COME BACK LATER! **\n')
