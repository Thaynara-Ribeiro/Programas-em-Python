#soma = 0
#num = int(input('Digite quantos numeros estão presentes na soma: '))
#for n in range(num):
#   num = int(input('Informe o numero: '))
#    soma = soma + num
#print('A soma dos numeros informados é',soma)


# Realizando o mesmo codigo utilizando o comando while 

num = int(input('Digite quantos numeros estão presentes na soma: '))
soma = 0
i = 0
while i != num:
    num = int(input('Informe o numero: '))
    soma = soma + num
    i += 1
print('A soma dos numeros informado é', soma)