
continuacao = 's'
while continuacao=='s':

    peso = float(input("Digite seu peso:"))
    altura = float(input("Digite sua altura:"))
    imc=peso/(altura*altura)
    print(imc)
    if imc < 18.5:
       print("Seu peso está muito baixo")
       continuacao= input("Deseja calcular mais um IMC? [s]/[n]")
    elif imc > 18.5 and imc <24.9:
        print("Seu peso está normal")
        continuacao= input("Deseja calcular mais um IMC? [s]/[n]")
    elif imc > 25 and imc < 29.9:
        print("Voce esta com sobrepeso")
        continuacao= input("Deseja calcular mais um IMC? [s]/[n]")
    elif imc >30:
        print("Voce esta com Obesidade")   
        continuacao= input("Deseja calcular mais um IMC? [s]/[n]") 
    else:
        print("Entrada invalida")