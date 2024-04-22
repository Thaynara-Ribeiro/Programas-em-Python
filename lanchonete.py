print('{:=^40}'.format('LANCHONETE'))
print(''' 
Cardapio
Hambúrguer................. R$ 3,00
Cheeseburger .............. R$ 2,50
Fritas............................ R$ 2,50
Refrigerante ................. R$ 1,00
Milkshake..................... R$ 3,00''')
hamburguer = int(input('Quantos Hanbúrguers você deseja: '))
cheeseburgers = int(input('Quantos cheeseburgers você deseja: '))
fritas = int(input('Quantas fritas você deseja: '))
refrigerante = int(input('Quantos refrigerantes você deseja: '))
milkshake = int(input('Quantos milkskaes você deseja: '))
resultado = (hamburguer * 3) + (cheeseburgers * 2.50) + (fritas * 2.50) + (refrigerante * 1) + (milkshake * 3)
print('Conta Final {:.2f} R$'.format(resultado))