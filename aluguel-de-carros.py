diaria = int(input())
km = int(input())
calculo = diaria * 90
if km > 100:
    calculo2 = (km - (diaria * 100)) * 12
    print('{:.2f}'.format(calculo+calculo2))
else:
    print('{:.2f}'.format(calculo))