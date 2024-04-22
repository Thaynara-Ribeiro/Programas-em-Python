n = int(input())
matriz = list()
for i in range(n):
    matriz.append(list(map(int,input().split())))
lista = list()
# Soma das linhas
for i in range(n):
    soma = 0
    for x in range(n):
        soma+= matriz [i][x]
    lista.append(soma)
# Soma das colunas
for x in range(n):
    soma = 0
    for i in range(n):
        soma+= matriz [i][x]
    lista.append(soma)
# Soma da diagonal 1
soma = 0
for i in range(n):
    soma += matriz [i][i]
lista.append(soma)
# Soma da diagonal 2
soma = 0
i = 0
j = n-1
while i < n:
    soma+= matriz [i][x]
    i+=1
    x-=1
lista.append(soma)

verdadeiro = True
index = 1
while verdadeiro and index < len(lista):
    if lista[index] != lista[0]:
        verdadeiro = False
    index+=1
if verdadeiro:
    print(soma)
else:
    print('-1')