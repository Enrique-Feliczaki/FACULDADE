import random
import os

def jogo_da_adivinhacao():
    numero_secreto = random.randint(1,20)
    tentativas = 0
    while tentativas<10:
        numero = int(input('Digite um numero: '))
        tentativas +=1
        if numero_secreto > numero:
            print('O numero secreto é maior que o numero digitado')
            
        elif numero_secreto < numero:
            print('O numero secreto é menor que o numero digitado')
            
        else:
            print('Parabens voce acertou o numero secreto!!')    
            break
    print(f'Voce utilizou {tentativas} tentativas para acertar o numero secreto')
jogo_da_adivinhacao()