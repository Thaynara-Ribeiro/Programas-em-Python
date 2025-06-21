#Faça um programa que leia um número inteiro qualquer é mostre sua Tabuada
print('{:=^30}'.format('TABUADA'))
n = int(input('Digite um número (Tabuada): '))
tabuada = 0
for i in range(1, 11):
    tabuada = n * i
    print('{} X {} = {}'.format(n, i, tabuada))