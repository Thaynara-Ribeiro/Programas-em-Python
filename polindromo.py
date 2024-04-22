print('{:=^40}'.format(' Analisando Polindromos '))
f = input('Digite uma frase para indentificar se a mesma é um polindromo: ').strip().upper()
p = f.split()
junto = ''.join(p)
inverso = ''
for i in range(len(junto) -1, -1, -1):
  inverso+=junto[i]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
  print('E um polimendro')
else:
  print('A frase digitada não é um polimedro')