from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

elements = list(q)  

print("Elementos na fila:", elements)

data = {
    'fila1': [],
}

data['fila1'].append(1)
data['fila1'].append(2)
data['fila1'].append(3)
data['fila1'].append(4)
data['fila1'].append(5)
data['fila1'].append(6)
data['fila1'].append(7)
data['fila1'].append(8)
data['fila1'].append(9)
data['fila1'].append(10)

print(data.items())

#print(data['fila1'][:3] and data['fila1'][-3:])
#print(data['fila1'][-3:])

nome={
    'nomes' : []
}

nome['nomes'].append('joao')
nome['nomes'].append('pedro')
nome['nomes'].append('felipe')
nome['nomes'].append('jose')
nome['nomes'].append('maria')

print(nome)

ALT={
    'joao' : 5557354,
    'pedro' : 2172194,
    'felipe' : 1298454,
}

print(ALT)

