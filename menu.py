maior = 0
escolha = 0
print('{:=^40}'.format(' MENU '))
print('''[1] Somar
[2] Subtrair
[3] Maior
[4] Novos numeros
[5] Sair do programa''')
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
while escolha != 5:
  escolha = int(input('Escolha qual opção deseja do menu: '))
  if escolha == 1:
    print('A soma dos numeros {} e {} é {}'.format(v1, v2, (v1+v2)))
  if escolha == 2:
    print('A subtração dos numeros {} e {} é {}'.format(v1, v2, (v1-v2)))
  if escolha == 3 and v1 > v2:
    print('O numero {} é o maior'.format(v1))
  if escolha == 3 and v2 > v1:
    print('O numero {} é o maior'.format(v2))
  if escolha == 3 and v1 == v2:
    print('Ambos os numeros são iguais')
  if escolha == 4:
    print('Digite novos valores')
    v3 = int(input('1° Valor: '))
    v4 = int(input('2° Valor : '))
