'''
Crie um programa que recebe do usuário um valor representa a velocidade e com base nessa velocidade
diga se ele tomou multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver
abaixo da velocidade máxima permitida deve exibir "Não houve multa", caso esteja até 10km acima, deve exibir "Multa leve"
caso esteja entre 11 a 20Km acima da velocidade máxima, exibir: "Multa grave", acima de 20Km exibir "Multa Gravíssima"
'''

#Método 5Q's para montra o algoritmo
# Analisar criticamente o problema: 
# Quais são os dados de entrada?
# (velocidade do usuário)
# O que devo fazer com esses dados?
# (Receber velocidade informada pelo usuário, compara-la é informar se o mesmo recebeu alguma multa, caso tenha recebido com a gravidade
# baseado na quantidade que Kms exedidos da velocidade máxima.) 
# Quais são as restrições?
# (O programa não possui restrições)
# Qual o resultado esperado? 
# (Que o programa exiba na tela se o usuário levou multa, se multa foi leve, grave ou gravissima baseada na velocidade permitida)
# Passo a passo do Pseudocódigo?
'''
input velocidade
if velocidade <= 80
    print "Não houve Multa, continue dirigindo com cuidado"
if velocidade > 80 and < 90
     print "Multa Leve"
if velocidade > 91 and < 100
    print "Multa Grave"
if velocidade > 100
    print "Multa Gravíssima"
'''
velocidade = int(input('Digite sua velocidade atual: '))
if velocidade <= 80:
    print('Não houve multa, continue dirigindo com cuidado')
elif velocidade > 80 and velocidade <= 90 :
    print('Multa Leve')
elif velocidade > 91 and velocidade <= 100:
    print('Multa Grave')
else:
    print('Multa Gravíssima')