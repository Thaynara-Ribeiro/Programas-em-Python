print('{:=^40}'.format('Calculando capacidade de transmissão'))
TVideo = float(input('Digite um valor para o video: '))
TAudio = float(input('Digite um valor para o audio: '))
TDados = float(input('Digite um valor para os dados: '))
capacidade = float(input('Qual a capacidade: '))
QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade
print('{:.2f}'.format(QDmax))
