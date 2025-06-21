#Faça um programa que ajude um professor sortear a ordem de apresentação de quatro alunos, o programa precisa ler os nomes dos quatro alunos retornando qual a ordem de apresentação.
import random
a1 = str(input('Digite o nome do 1° aluno: '))
a2 = str(input('Digite o nome do 2° aluno: '))
a3 = str(input('Digite o nome do 3° aluno: '))
a4 = str(input('Digite o nome do 4° aluno: '))
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print('A ordem de apresentação: {}'.format(alunos))