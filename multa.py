velocidade = int(input('Digite sua velocidade atual: '))
velocidade_maxima = 80
if velocidade <= 80:
    print('Não houve multa, continue dirigindo com cuidado')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima +10 :
    print('Multa Leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Multa Grave')
else:
    print('Multa Gravíssima')