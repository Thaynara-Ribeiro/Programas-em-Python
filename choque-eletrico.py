level = int(input())
if level > 0 and level < 21:
    potencia = 20 + (level ** 3)
    print('Potencia de : {} W'.format(potencia))
elif level > 20 and level < 41:
    potencia2 = 8000 + (level - 10)**2
    print('Potencia de : {} W'.format(potencia2))
elif level > 40 and level < 61:
    potencia3 = 9000 + (5*level)
    print('Potencia de : {} W'.format(potencia3))
elif level > 60 and level < 81:
    potencia4 = (9300 + 2*level)
    print('Potencia de : {} W'.format(potencia4))
elif level > 80 and level < 101: 
    potencia5 = 9500 + level
    print('Potencia de : {} W'.format(potencia5))