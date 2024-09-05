# Faça uma função que receba um dicionário e um número N.
# Apresentar os primeiros N itens e os últimos N itens do dicionário

# data = {
#     'fila1': [],
# }

# data['fila1'].append(1)
# data['fila1'].append(2)
# data['fila1'].append(3)
# data['fila1'].append(4)
# data['fila1'].append(5)
# data['fila1'].append(6)
# data['fila1'].append(7)
# data['fila1'].append(8)
# data['fila1'].append(9)
# data['fila1'].append(10)

# print(data['fila1'])


# def elementos(data,n):
#     for i in range(0, n, 1):
#         var = data[i]
#         print(f"{var}\n")
#     for j in range(len(data)-1, len(data)-n-1, -1):
#         var2 = data[j]
#         print(f"{var2}\n")

# numero = int(input("Digite um número: "))

# elementos(data['fila1'], numero)


#Faça uma função que troca as chaves e os valores de lugar (Exemplo "chave" : "Valor" vira -> "Valor" : "chave")
# # dicionario = {"chave1": "valor1", "chave2": "valor2"}
# # invertido = {valor1: chave1 for chave1, valor1 in dicionario.items()}
# # print (dicionario)
# # print (invertido)

#Criar um programa que analisa as notas de vários alunos. 
# Dado um dicionário onde as chaves são os nomes dos alunos e os valores são listas com suas respectivas notas em diferentes disciplinas, o programa deve calcular e exibir: 
#3a - A média de cada aluno.
#3b - A nota mais alta e mais baixa de cada aluno.
#3c - O aluno com a maior média e o aluno com a menor média.
#3d - Exemplo de entrada: {João:[10,5,8], Maria:[9,9,9], José[8,7,6]}


# dadosAlunos = {
#     "Maria": [30, 70, 20, 30],
#     "Joao": [50, 90, 20, 10],
#     "Enrique": [70,80, 10, 30],
#     "Emanuelly": [80, 90, 100, 70],
#     "Eduardo": [90, 70, 50, 20]
# }

# def mediaNotas(notas):
#     return sum(notas) / len(notas)

# maiorMedia = -1
# aluno_Maior = ""
# aluno_Menor = ""
# menorMedia = 300000
 

# for aluno, notas in dadosAlunos.items():
#     media = mediaNotas(notas)
#     print (f"A média de {aluno} é de: {media:.2f}")
    
#     maior_nota = max(notas)
#     menor_nota = min(notas)
     
#     print(f"A nota mais alta de {aluno} é: {maior_nota}")
#     print(f"A nota mais baixa de {aluno} é: {menor_nota}")

#     if media > maiorMedia:
#         maiorMedia = media
#         aluno_maior_media = aluno
#     if media < menorMedia:
#         menorMedia = media
#         aluno_menor_media = aluno

#     print(f"\nO aluno com a maior média é {aluno_maior_media} com média {maiorMedia:.2f}")
#     print(f"O aluno com a menor média é {aluno_menor_media} com média {menorMedia:.2f}")




