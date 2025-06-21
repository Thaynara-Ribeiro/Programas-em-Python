#Faça um programa que leia um angulo qualquer, informando seu seno, cosseno é tangente
import math
a = int(input('Digite um ângulo qualquer: '))
print('O seno do Ângulo {} é {:.2f}° \nO cosseno do Ângulo {} é {:.2f}°'.format(a, math.sin(a), a,  math.cos(a)))
print('A tangente Ângulo {} é {:.2f}°'.format(a, math.tan(a)))
