import random

while True:
    try:
        jogador = int(input('Adivinha um numero de 0 a 5:'))
        cpu = random.randint(0,5)

        if jogador == cpu:
            break

        else:
            print('Errou: Tente de novo')

    except ValueError:
        print('Dados invalidos: precisam ser numeros.')

print('Parabens!')
print('FIM DE JOGO')