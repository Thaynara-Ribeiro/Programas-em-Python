'''Escreva um programa que calcule se o usúario levou multa. Considerando que a velocidade máxima é 80Km
se o mesmo estiver abaixo de 80Km exiba em tela "Não houve multa" acima de 10Km "Levou multa leve"
entre 11 até 20Km exiba "Levou multa grave" acima de 20Km "Levou multa gravíssima."
Utilizando o Metodo 5Qs
Qual os dados de entrada?
Oque fazer com esses dados?
Qual as restrições do programa?
Qual o resultado esperado?
Qual a sequência de passo a passo em Pseudocódigo?
'''
velocidade = int(input('Qual velocidade atingida? '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Não houve Multa.')
elif velocidade > velocidade_maxima and velocidade < velocidade_maxima + 10:
    print('Levou multa Leve.')
elif velocidade > velocidade_maxima + 10 and velocidade < velocidade_maxima + 20:
    print('Levou multa Grave.')
elif velocidade > velocidade_maxima + 20:
    print('Levou multa Gravissima.')
else:
    print('Valor Inválido.')