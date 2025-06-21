#Escreva um programa que é solicite três segmentos de retas para verificar se é possivel formar um triângulo. Sendo possivel essa formação, informe qual o tipo do triângulo formado: Equilátero: Todos os lados iguais, Isóceles: Dois lados iguais, Escaleno: Todos os lados são diferentes.
print('{:=^40}'.format('Analisando Triângulos'))
r1 = int(input('Informe o 1° Segmento de Reta: '))
r2 = int(input('Informe o 2° Segmento de Reta: '))
r3 = int(input('Digite o 3° Segmento de Reta: '))
if r1 < (r2+r3) or r2 < (r1+r3) or r3 < (r1+r2):
    print('As retas informadas FORMAM TRIÂNGULO')
    if r1 == r2 == r3:
        print('O triângulo Formado é EQUILÁTERO')
    elif r1 != r2 != r3:
        print('O triângulo Formando é ESCALENO')
    else:
        print('O triângulo Formando é ISÓSCELES')
else:
    print('As retas informadas NÃO FORMAM TRIÂNGULO')