from time import sleep
soma = 0 
maioridade = 0
nomehomem = ''
count = 0
for i in range (1,5):
    print('======= {}° Pessoa ======='.format(i))
    nome = input('Qual o seu nome: ').strip()
    idade = int(input('Qual a sua idade: '))
    sexo = input('Qual o seu sexo [M/F]: ')
    soma += idade
    if i == 1 and sexo in 'Mm':
        maioridade = idade
        nomehomem = nome
    if sexo in 'Mn' and idade > maioridade:
            maioridade = idade
            nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        count+= 1
media = soma / i 
sleep(1)   
print('''
ANALISANDO...''')  
sleep(1)
print('''
 A media das idades lidas digitadas e igual á {} 
 O homem mais velho {} possui {} anos
 São {} mulher menores de 20 anos'''.format(media, nomehomem, maioridade, count))