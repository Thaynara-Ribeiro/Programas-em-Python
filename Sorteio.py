#Faça um programa para auxiliar um professor realizar um sorteio entre quatro alunos para que um deles apague o quadro, informando ao final o nome do aluno sorteado.
import random 
a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')
alunos = [a1,a2, a3, a4]
print('O aluno escolhido para apagar o quadro é {}'.format(random.choice(alunos)))