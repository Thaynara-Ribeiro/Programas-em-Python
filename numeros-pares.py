# Utilizando estrutura de repetições
numero = 0
contagem = 0
for numero in range (1, 6):
    numero = int(input('Digite um numero para saber se o mesmo é impar ou par: '))
    if ((numero%2) == 0):
        print('O numero é Par')
        contagem = contagem + 1
    else: 
        print('O numero é Impar')
print('Possui {} numeros pares.'.format(contagem))