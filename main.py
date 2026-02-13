#emojis: 🎰 🍀 🎲 🃏 💎 💸 ♦️ ♠️
import time
import random
import os
def jogar():
    emoji = ['🎰', '🍀', '🎲', '🃏', '💎', '💸', '♦️', '♠️']
    def mostrar_animacao():
        print('girando...')
        for i in range(15):
            emojis = [random.choice(emoji), random.choice(emoji), random.choice(emoji)]
            print(f'{emojis[0]} | {emojis[1]} | {emojis[2]}', end = '\r')
            time.sleep(0.1)


    print('🎰 Bem vindo ao Caça-Niquel Python 🎰\n')

    input('Pressione ENTER para girar os rolos...')
    mostrar_animacao()
    resultado = [random.choice(emoji), random.choice(emoji), random.choice(emoji)]
    print(f'{resultado[0]} | {resultado[1]} | {resultado[2]}')

    if resultado[0] == resultado[1] == resultado[2]:
        print('\n🎉 JACKPOT! Você ganhou! 🎉')
    elif resultado[0] == resultado[1] or resultado[0] == resultado[2] or resultado[1] == resultado[2]:
        print('\nQuase lá! Duas combinações iguais.')
    else:
        print('\nNão foi dessa vez. Tente de novo!')
if __name__ == '__main__':
    while True:
        jogar()
        resposta = input('Pressione ENTER para jogar novamente ou digite "q" para sair: ').strip().lower()
        if resposta == 'q':
            print('\nObrigado por jogar! Até a proxima!')
            break
        os.system('cls')
