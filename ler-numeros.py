num = int(input('Digite uma lista de numeros, digite 0 para parar a lista: '))
quant = 1
soma = num
while num != 0:
    num = int(input('Digite uma lista de numeros, digite 0 para parar a lista: '))
    if num < 0:
        print('NUMERAÇÃO INVALIDA')
    else:
        quant += 1
        soma = soma + num
if quant != 1: 
    media = soma /(quant-1)
    print('A media dos numero digitados é igual {}'.format(media))
else:
    print('Você não leu nenhum numero')