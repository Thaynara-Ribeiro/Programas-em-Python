from statistics import mean
divisiveis = list()
n = [3,8,1,20,4,13,9,2,2,5]
print('Média: {}'.format(mean(n)))
for i, v in enumerate(n):
    if v % 3 ==0:
        divisiveis.append(v)
print('Divisíveis: {}'.format(v))
