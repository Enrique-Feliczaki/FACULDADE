#Crie um programa que simule diferentes tipos de investimentos: poupança , renda fixa, ações e CDI.
#O usuári deve inserir o valor inicial de cada investimento, taxa de juros e período de investimento, 
# e o programa deve calcular o lucro em relação ao tempo final
continuacao = "s" 
print("Selecione qual tipo de investimento deseja utilizar")
while continuacao == "s":
    opcao = input("[1]-poupanca || [2]-renda_fixa || [3]-Acoes || [4]-CDI")


    if opcao == "1":
        print("Poupanca selecionada!")
        num1 = float(input("Insira  valor inicial a ser investido: "))
        taxa = float(input("Insira a taxa de juros que o investimento em decimal: "))
        periodo_de_investimento = float(input("Insira o periodo de investimento em: "))
        valor_total = num1 * (1+taxa)*periodo_de_investimento
        print(f"O lucro atingido é: {valor_total}")
        continuacao = input("Se deseja fazer mais algum investimento digite [s]")

    elif opcao == "2":
        print("Poupanca selecionada!")
        num1 = float(input("Insira  valor inicial a ser investido: "))
        taxa = float(input("Insira a taxa de juros que o investimento em decimal: "))
        periodo_de_investimento = float(input("Insira o periodo de investimento em: "))
        valor_total = num1 * (1+taxa)*periodo_de_investimento
        print(f"O lucro atingido é: {valor_total}")
        continuacao = input("Se deseja fazer mais algum investimento digite [s]")

    elif opcao == "3":
        print("Poupanca selecionada!")
        num1 = float(input("Insira  valor inicial a ser investido: "))
        taxa = float(input("Insira a taxa de juros que o investimento em decimal: "))
        periodo_de_investimento = float(input("Insira o periodo de investimento em: "))
        valor_total = num1 * (1+taxa)*periodo_de_investimento
        print(f"O lucro atingido é: {valor_total}")
        continuacao = input("Se deseja fazer mais algum investimento digite [s]")
        
    elif opcao == "4":
        print("Poupanca selecionada!")
        num1 = float(input("Insira  valor inicial a ser investido: "))
        taxa = float(input("Insira a taxa de juros que o investimento em decimal: "))
        periodo_de_investimento = float(input("Insira o periodo de investimento em: "))
        valor_total = num1 * (1+taxa)*periodo_de_investimento
        print(f"O lucro atingido é: {valor_total}")
        continuacao = input("Se deseja fazer mais algum investimento digite [s]")

    else:
        print("Opcao invalida")
        continuacao = input("Digite [s] para selecionar alguma forma de investimento")
        
    
    