print('{:=^40}'.format('Supermecado Otimista'))
print('''Dias da semana: seg, ter, qua, qui, sex, sab, dom
Opções de compras: ouro, prata ''')
dia = str(input('Qual o dia das suas compras? '))
preço = float(input('Qual o valor das compras? '))
opção = str(input('Qual a opção usada nas compras? '))
produto = str(input('Qual produto foi comprado? '))
if dia == 'seg' and opção == 'ouro':
    print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço/2)) 
elif dia == 'ter' and opção == 'ouro':
        print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço/2))
elif dia == 'qua' and opção == 'ouro':
    print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço/2))
elif 9.99 < preço < 100.1 and dia == 'qui':
    print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço/3))
elif 9.99 < preço < 100.1 and dia == 'sex':
    print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço/3))
elif dia == 'sab' and opção == 'prata':
    print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço*3))
else:
    print('O preco do produto {} no dia {} eh {:.2f}'.format(produto, dia, preço*2))
