''' Escreva um programa que analise o número de atrasos de um aluno, exibindo na tela
As possiveis, mensagens: 1 ATRASO "Pode, passar mas seja mais cuidadoso com o horário"
2 ATRASOS "Segundo atraso, ocorrendo novamente você será Supenso."
3 ATRASOS "Você, está suspenso" '''

atraso = int(input('Quantos atrasos? '))
if atraso == 1:
    print("Pode, passar mas seja mais cuidadoso com o horário")
elif atraso == 2:
    print("Segundo atraso, ocorrendo novamente você será Supenso.")
elif atraso == 3:
    print("Você, está suspenso")
else:
    print('Valor Inválido')