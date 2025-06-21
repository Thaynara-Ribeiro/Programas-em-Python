#Desenvolva um programa que pergunte a distância da viagem em KM. Calcule o preço da passagem, cobrando 0,50 por KM para viagens de até 200KMs rodados é 0,45 para viagens acima de 200KMs.
print('{:=^60}'.format('CAlculando Valor da Viagem'))
d = int(input('Digite a distância da sua viagem: '))
if d <= 200:
    print('O valor da sua viagem ficou em {:.2f}R$'.format(d*0.50))
else: 
    print('O valor da sua viagem ficou em {:.2f}'.format(d*0.45))