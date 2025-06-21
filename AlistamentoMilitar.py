#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar/ Se é a hora de se alistar/ Se já passou da hora do alistamento. Seu programa deve informar o prazo que falta para o alistamento ou o tempo que já passou para o alistamento. 
from datetime import date
print('{:=^40}'.format('Alistamento Militar'))
ano = int(input('Digite seu Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 18:
    print('Você ainda não está elegível ao Alistamento, ainda faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Você está na hora certa para o Alistamento, você tem exatamente {} anos'.format(idade))
else: 
    print('Você já passou da hora para o Alistamento, você está atraso {} anos'.format(idade-18))
