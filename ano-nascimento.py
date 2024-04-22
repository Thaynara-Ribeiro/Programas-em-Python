from datetime import date
totmaior=0
totmenor=0
anoatual = date.today().year
for i in range(1, 8):
  data = int(input('Me informe o ano do nascimento da {} pessoa: '.format(i)))
  idade =  anoatual - data
  if idade < 21:
    totmenor+=1
  else:
    totmaior+=1
print('Ao todo tivemos {} pessoas menores de idade.'.format(totmenor))
print('Também tivemos {} pessoas maiores de idade.'.format(totmaior))