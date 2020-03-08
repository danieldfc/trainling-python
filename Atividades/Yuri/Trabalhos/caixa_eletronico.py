# DEFINE A FUNÇÃO DE MENU DO USUÁRIO COM A OPÇÃO DE ESCOLHA


def menu():
    print('\033[0;33m='*30)
    print('{:^30}'.format('CAIXA ELETRÔNICO'))
    print('='*30+'\n')
    print('1 - CARREGAR CAIXA ELETRÔNICO')
    print('2 - SACAR DINHEIRO')
    print('3 - SAIR\n')
    opc = int(input('\033[0;35mOpção -> '))

    return opc


def contador_notas(preco):
    quant100 = preco // 100
    preco %= 100

    quant50 = preco // 50
    preco %= 50

    quant20 = preco // 20
    preco %= 20

    quant10 = preco // 10
    preco %= 10

    quant5 = preco // 5
    preco %= 5

    if quant100 > notas100 or quant50 > notas50 or quant20 > notas20 or quant10 > notas10 or quant5 > notas5:
        return 0

    return [quant100, quant50, quant20, quant10, quant5]


notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
total = 0

opc = menu()

while opc > 0 and opc < 4:
    if opc == 1:
        print(
            '\033[0;33m\n> Informe separadamente a quantidade de notas para (100, 50, 20, 10, 5)')
        print('\nEx.: 1 2 3 4 5\n')
        print('Resultado: 100=1 50=2 20=3 10=4 5=5\n')

        quant100, quant50, quant20, quant10, quant5, = map(
            int, input('\033[0;35m> ').split())

        notas100 += quant100
        notas50 += quant50
        notas20 += quant20
        notas10 += quant10
        notas5 += quant5

        total += (notas100 * 100) + (notas50 * 50) + \
            (notas20 * 20) + (notas10 * 10) + (notas5 * 5)

        if total == 0:
            print(
                '\033[1;32m\n** O caixa foi não foi abaslecido. Total em caixa -> \033[1;31mR$ {},00\033[0;32m **\n'.format(total))
        else:
            print(
                '\033[1;32m\n** O caixa foi abaslecido. Total em caixa -> \033[1;31mR$ {},00\033[0;32m **\n'.format(total))
    elif opc == 2:
        if notas100 == 0 and notas50 == 0 and notas20 == 0 and notas10 == 0 and notas5 == 0:
            print(
                '\033[1;31m\n** O caixa não possui notas disponível, por favor abasteça **\n')
        else:
            print('\033[0;33m\nInforme um valor total inteiro, que quer sacar')
            print('\nEx.: 200\n')
            print('Resultado: 100=2 50=0 20=0 10=0 5=0')
            print('\033[1;32m\nSALDO ATUAL -> R$ {},00\n'.format(total))
            print('\033[0;33mQuantidade de notas armazenadas -> 100={} 50={} 20={} 10={} 5={}\n'.format(
                notas100, notas50, notas20, notas10, notas5))

            preco = int(input('\033[0;35m> R$ '))
            notas = contador_notas(preco)

            if notas == 0:
                print(
                    '\033[1;31m\n** Não foi possível efetuar o saque, verifique a quantidade de notas **\n')
                print('\033[0;33mQuantidade de notas armazenadas -> 100={} 50={} 20={} 10={} 5={}\n'.format(
                    notas100, notas50, notas20, notas10, notas5))

            else:
                notas100 -= notas[0]
                notas50 -= notas[1]
                notas20 -= notas[2]
                notas10 -= notas[3]
                notas5 -= notas[4]

                print(notas100, notas50, notas20, notas10, notas5)
                print(total)

                total = (notas100 * 100) + (notas50 * 50) + \
                    (notas20 * 20) + (notas10 * 10) + (notas5 * 5)
                print(
                    '\033[1;32m\n** Seu saque foi completado. Total em caixa -> \033[1;31mR$ {},00\033[0;32m **\n'.format(total))
                print('\033[0;33mQuantidade de notas armazenadas -> 100={} 50={} 20={} 10={} 5={}\n'.format(
                    notas100, notas50, notas20, notas10, notas5))
    elif opc == 3:
        print('\033[1;32m\n** Obrigado pela preferência, volte sempre! **\n')
        exit()
    opc = menu()
