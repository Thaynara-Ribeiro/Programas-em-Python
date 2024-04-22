# Escreva um prgrama que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o 
# usuário chute um número até que o valor gerado no início do programa seha chutado corretamente.
# O programa deve informar se o chute foi acima. abaixo ou igual ao valor aleatprio gerado no início do programa

# Método 5Q's para montra o algoritmo
# Analisar criticamente o problema: 
# Quais são os dados de entrada?
# (Uma lista de 1 a 10/ Um chute do usuário)
# O que devo fazer com esses dados?
# (Comparar o chute do usuário ao numero aleatório gerado é exibir na tela se o chute foi maior, meno ou igual) 
# Quais são as restrições?
# (Um valor entre 1 até 10)
# Qual o resultado esperado? 
# (O programa deve informar se o chute foi acima. abaixo ou igual ao valor aleatório gerado no início do programa)
# Passo a passo do Pseudocódigo?
'''
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
    print "O chute foi maior que o valor gerado"
if chute < valor_aleatorio
    print "O chute foi menor que o valor gerado"
if chute = valor_aleatorio
    print "Você Acertou"
'''
'''
Codigo sem loop de repetição
import random
valor_aleatorio = random.randint(1,10)
escolha_cumputador = valor_aleatorio
chute = int(input('Chute um valor entre 1 a 10: '))
if chute > valor_aleatorio:
    print('O chute foi maior que o valor gerado))
elif chute < valor_aleatorio:
    print('O chute foi menor que o valor gerado,))
else:
    print('Você Acertou')
'''
import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor entre 1 a 10: '))
    if chute > valor_aleatorio:
        print('O chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('O chute foi menor que o valor gerado')
        acertou = True
        print('Você Acertou')