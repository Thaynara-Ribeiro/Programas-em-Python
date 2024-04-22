n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if n1 > media and n2 > media:
    print('2')
elif n2 > media and n3 > media:
    print('2')
elif n1 > media and n3 > media:
    print('2')
elif n1 > media:
    print('1')
elif n2 > media:
    print('1')
elif n3 > media:
    print('1')
else: 
    print('0') 