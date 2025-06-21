#Faça um programa que leia um nome de uma cidade, após leitura informa se ela começa ou não com o nome "SANTO"
c = str(input('Digite o nome de uma cidade: ')).upper()
s = c.split()
print('A cidade {} tem o seu primeiro nome igual SANTO? {}'.format(c, s[0] == 'SANTO'))

#Outra forma de resolver ciente que eu preciso analisar apenas se o primeiro nome é SANTO: 

'''c = str(input('Digite o nome de uma cidade: ')).strip().upper()
print('A cidade {} tem o seu primeiro nome igual SANTO {} '.format(c, c[0:5] == 'SILVA'))
'''


