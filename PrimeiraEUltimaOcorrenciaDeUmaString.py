#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A", Em qual posição ela aparece a primeira vez, Em qual posição ela aparece a ultima vez.
print('{:=^40}'.format('Analisando um Nome'))
n = str(input('Digite seu nome: ')).upper().strip()
print('A letra A aparere {} vezes no nome {}'.format(n.count('A'), n))
print('A primeira aparição da letra A no nome {} ocorre na posição {}'.format(n, n.find('A')+1))
print('A ultima aparição da letra A no nome {} ocorre na posição {}'.format(n , n.rfind('A')+1))