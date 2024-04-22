pessoas = int(input('Pessoas: '))
local = str(input('Local: ')).upper()
quarto = int(input('Quartos: '))
if local == 'PIPA' and quarto == 2:
    passeio = pessoas * 75
    print('''
{:.2f}
{:.2f}'''.format(passeio + 600, (passeio + 600)/pessoas))
elif local == 'PIPA' and quarto == 3:
    passeio2 = pessoas * 75
    print('''
{:.2f}
{:.2f}'''.format(passeio2 + 900, (passeio2 + 900)/pessoas))
elif local == 'FORTALEZA' and quarto == 3:
    passeio3 = pessoas * 60 
    print('''
{:.2f}
{:.2f}'''.format(passeio3 + 950, (passeio3 + 950)/pessoas))
else:
    passeio4 = pessoas * 60
    print('''
{:.2f}
{:.2f}'''.format(passeio4 + 1120, (passeio4 + 1120)/pessoas))
