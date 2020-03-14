# DEFINE A FUNÇÃO DE MENU DO USUÁRIO COM A OPÇÃO DE ESCOLHA


def menu():
    print('\033[0;33m='*30)
    print(f'{"DEV BANK":^30}'.format(''))
    print('='*30+'\n')
    print('1 - LOAD ELECTRONIC BOX')
    print('2 - CASH MONEY')
    print('3 - GO OUT\n')
    opt = int(input('\033[0;35mOption -> '))

    return opt


def counter_banknotes(price):
    amount100 = 0
    amount50 = 0
    amount20 = 0
    amount10 = 0
    amount5 = 0

    ballot = 100

    if price <= 0:
        return 0
    else:
        while True:
            if price >= ballot:
                if ballot == 100:
                    if amount100 < banknotes100:
                        price -= ballot
                        amount100 += 1
                    else:
                        ballot = 50
                elif ballot == 50:
                    if amount50 < banknotes50:
                        price -= ballot
                        amount50 += 1
                    else:
                        ballot = 20
                elif ballot == 20:
                    if amount20 < banknotes20:
                        price -= ballot
                        amount20 += 1
                    else:
                        ballot = 10
                elif ballot == 10:
                    if amount10 < banknotes10:
                        price -= ballot
                        amount10 += 1
                    else:
                        ballot = 5
                elif ballot == 5:
                    if amount5 < banknotes5:
                        price -= ballot
                        amount5 += 1
            else:
                if ballot == 100:
                    ballot = 50
                elif ballot == 50:
                    ballot = 20
                elif ballot == 20:
                    ballot = 10
                elif ballot == 10:
                    ballot = 5
                if price == 0:
                    break

        return [amount100, amount50, amount20, amount10, amount5]


def load_banknotes(amount100, amount50, amount20, amount10, amount5):
    global banknotes100, banknotes50, banknotes20, banknotes10, banknotes5, total

    banknotes100 += amount100
    banknotes50 += amount50
    banknotes20 += amount20
    banknotes10 += amount10
    banknotes5 += amount5

    total = (banknotes100 * 100) + (banknotes50 * 50) + \
        (banknotes20 * 20) + (banknotes10 * 10) + (banknotes5 * 5)

    return total


def withdraw(banknotes):
    global banknotes100, banknotes50, banknotes20, banknotes10, banknotes5, total

    print(f'\033[1;33m\n** The withdrawn notes were: 100={banknotes[0]}, 50={banknotes[1]}, 20={banknotes[2]},',
          f'10={banknotes[3]}, 5={banknotes[4]} **')

    banknotes100 -= banknotes[0]
    banknotes50 -= banknotes[1]
    banknotes20 -= banknotes[2]
    banknotes10 -= banknotes[3]
    banknotes5 -= banknotes[4]

    total = (banknotes100 * 100) + (banknotes50 * 50) + \
        (banknotes20 * 20) + (banknotes10 * 10) + (banknotes5 * 5)

    return total


banknotes100 = 0
banknotes50 = 0
banknotes20 = 0
banknotes10 = 0
banknotes5 = 0
total = 0

opt = menu()

while opt > 0 and opt < 4:
    if opt == 1:
        print(
            '\033[0;33m\n> Enter the number of notes separately for (100, 50, 20, 10, 5)')
        print('\nEx.: 1 2 3 4 5\n')
        print('Result: 100=1 50=2 20=3 10=4 5=5\n')

        amount100, amount50, amount20, amount10, amount5 = map(
            int, input('\033[0;35m> ').split())

        total = load_banknotes(
            amount100, amount50, amount20, amount10, amount5)

        if total == 0:
            print(
                f'\033[1;32m\n** The cashier was not replenished. Total in cash -> \033[1;31mR$ {total},00\033[0;32m **\n')
        else:
            print(
                f'\033[1;32m\n** The cashier was replenished. Total in cash -> \033[1;31mR$ {total},00\033[0;32m **\n')
    elif opt == 2:
        if banknotes100 == 0 and banknotes50 == 0 and banknotes20 == 0 and banknotes10 == 0 and banknotes5 == 0:
            print(
                '\033[1;31m\n** The cashier has no notes available, please refill **\n')
        else:
            print('\033[0;33m\n> Enter a total amount that you want to withdraw')
            print('\nEx.: 200\n')
            print('Result: 100=2 50=0 20=0 10=0 5=0')
            print(f'\033[1;32m\n Current balance -> R$ {total},00\n')
            print(
                f'\033[0;33mAmount of banknotes stored -> 100={banknotes100} 50={banknotes50} 20={banknotes20} 10={banknotes10} 5={banknotes5}\n')

            price = int(input('\033[0;35m> R$ '))
            banknotes = counter_banknotes(price)

            if banknotes == 0:
                print(
                    '\033[1;31m\n** Unable to withdraw, check the amount of banknotes **\n')
                print(
                    f'\033[0;33mAmount of banknotes stored -> 100={banknotes100} 50={banknotes50} 20={banknotes20} 10={banknotes10} 5={banknotes5}\n')

            else:
                total = withdraw(banknotes)

                print(
                    f'\033[1;32m\n** Your loot has been completed. Total in cash -> \033[1;31mR$ {total},00\033[0;32m **\n')
                print(
                    f'\033[0;33mAmount of banknotes stored -> 100={banknotes100} 50={banknotes50} 20={banknotes20} 10={banknotes10} 5={banknotes5}\n')
    elif opt == 3:
        print('\033[1;32m\n** Thanks for your preference, always come back! **\n')
        exit()
    opt = menu()

print('\033[1;31m\n** Invalid option, restart and try again! **\n')
