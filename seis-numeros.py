soma = 0
cont = 0
for c in range(1,7):
  n = int(input('Digite um numero: '))
  if n%2 ==0:
    soma+=n
    cont=n+1 
  else:
    cont=n-1
print('A soma dos {} valores é igual á {}'.format(cont, soma))