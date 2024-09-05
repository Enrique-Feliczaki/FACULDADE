def formula(num, armazenagem):
    if num == 1 or num == 2:
        return 1
    
    if armazenagem[num] != 0:
        return armazenagem[num]
    
    armazenagem[num] = formula(num-1, armazenagem) + formula(num-2, armazenagem)
    return armazenagem[num]

numero_sequencia = 10
armazenagem = [0] * (numero_sequencia + 1)
lista = []

for interador in range(1, numero_sequencia + 1):
    resultado = formula(interador, armazenagem)
    lista.append(resultado)

print(lista)
