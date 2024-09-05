print("Calculadora")
print("Selecione qual operacao deseja ser utilizada")
continuar = 's'
while continuar=='s':
    opcao=int(input("1-Adicao | 2-Subtracao | 3-Multiplicacao | 4-Divisao: "))
    if opcao==1:
        num1=int(input("Digite o primeiro numero: "))
        num2=int(input("Digite o segundo numero: "))
        soma=num1+num2
        print(f"A soma do primeiro e do segundo numero e {soma}")
        continuar=input("Gostaria de continuar?[s][n]")
    elif opcao==2:
        num1=int(input("Digite o primeiro numero: "))
        num2=int(input("Digite o segundo numero: "))
        subtracao=num1-num2
        print(f"A subtracao do primeiro e do segundo numero e {subtracao}")
        continuar=input("Gostaria de continuar?[s][n]")
    elif opcao==3:
        num1=int(input("Digite o primeiro numero: "))
        num2=int(input("Digite o segundo numero: "))
        multiplicacao=num1*num2
        print(f"A multiplicacao do primeiro e do segundo numero e {multiplicacao}")
        continuar=input("Gostaria de continuar?[s][n]") 
    elif opcao==4:
        num1=int(input("Digite o primeiro numero: "))
        num2=int(input("Digite o segundo numero: "))
        divisao=num1/num2
        print(f"A divisao do primeiro e do segundo numero e {divisao}")    
        continuar=input("Gostaria de continuar?[s][n]")
    else:
        print("Numero inválido")    

