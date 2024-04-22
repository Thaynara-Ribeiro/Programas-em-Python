from datetime import date #Importação da biblioteca
ano = date.today().year # comando utilizado para obter o ano atual
count = 0
count2 = 0
for i in range (1,8):
  nome = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
  idade = ano - nome
  if idade > 21: #Estrutura de decisão usada no processo de contagem
    count+= 1 #Encrementando o codigo
  else:
    count2+=1 #Encrementando o codigo
print('''Nas datas apresentadas temos {} pessoas maiores de 21 anos,
também possuimos {} pessoas menores de idade.'''.format(count, count2))