#Escreva um programa que leia o ano de nascimento de atleta é mostre sua categoria, de acordo com a idade: Até 9 anos: Mirin, Até 14 anos: Infantil, Até 19 anos: Junior, Até 20 anos Sênior, Acima de 20: Master
from datetime import date
ano = int(input('Digite seu Ano de Nascimento Atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade <= 9:
    print('Sua Categoria: MIRIN')
elif idade <= 14:
    print('Sua Categoria: INFANTIL')
elif idade <= 19:
    print('Sua Categoria: JUNIOR')
elif idade == 20:
    print('Sua Categoria: SÊNIOR')
else: 
    print('Sua Categoria: MASTER')