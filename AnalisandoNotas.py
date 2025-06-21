#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida. (Media Abaixo de 5.0: Reprovado, Media entre 5.0/6.9: Recuperação, Media 7.0 ou superior: Aprovado)
print('{:=^40}'.format('Analisando Notas'))
n1 = float(input('Digite sua 1º Média: '))
n2 = float(input('Digite sua 2º Média: '))
if (n1+n2) / 2 < 5.0:
    print('Você está REPROVADO')
elif (n1+n2) / 2 >= 7.0:
    print('Você está APROVADO')
else:
    print('Você está em RECUPERAÇÃO')
