import random
def numero_secreto():
    numero_sercreto=random.randint(1, 100)
    certo = False
    tentativas = 0 
    continuar='s'
    while not certo:
        palpites=int(input("Digite sua tentativa: "))
        tentativas+=1
        if palpites==numero_sercreto:
            certo = True
            print("Parabens!! Voce conseguiu acertar o numero secreto")
            continuar=input("Deseja continuar jogando [s]/[n]")    
            
        elif palpites < numero_sercreto:
            print("O numero secreto é maior do que o numero digitado")
        else:
            print("O numero secreto e menor do que o numero digitado")
        
    
        
numero_secreto()