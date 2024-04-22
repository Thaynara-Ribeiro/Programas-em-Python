print('{:=^40}'.format('Vamos jogar'))
idade = int(input('Qual a sua idade? '))
print('''Tipos de jogos
azar
mmorpg
moba
casual''')
jogo = str(input('Qual jogo deseja jogar? '))
if  idade < 0 or idade > 130:
    print('Idade invalida.')
elif idade >= 21 and jogo == 'azar':
    print('Pode entrar!')
elif idade < 21 and jogo == 'azar':
    print('Volte daqui há alguns anos.')
elif idade >= 14 and jogo == 'mmorpg':
    print('Pode entrar!')
elif idade < 14 and jogo == 'mmorpg':
    print('Volte daqui há alguns anos.')
elif idade >= 10 and jogo == 'moba':
    print('Pode entrar!')
elif idade < 10 and jogo == 'moba':
    print('Volte daqui há alguns anos.')
elif idade < 130 and jogo == 'casual':
    print('Pode entrar!')
else:
    print('Jogo invalido.')