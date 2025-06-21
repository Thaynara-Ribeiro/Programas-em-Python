#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
#Ele foi alugado. Calcule o preço a pagar, sabendo que o aluguel do carro por dia é 60R$ é 0,15R$ por KM rodado.
print('{:=^40}'.format('Calculando Aluguel'))
d = int(input('Digite quantos dias o veiculo foi alugado: '))
km = float(input('Digite quantos KMs foram percorridos com o veiculo: '))
print('Sabendo que o veiculo foi alugado por {} dias, o valor apenas do aluguel é {}R$'.format(d, d*60))
print('Sabendo também que foram percorridos {}KM, o valor total acrescendo o valor cobrado por cada KM é {}'.format(km, (d*60)+(km*0.15)))
