unidade = str(input())
temperatura = float(input())
if unidade == 'C' and temperatura >= -273::
    C_para_F = (temperatura * 1.8) + 32
    C_para_K = temperatura + 273.15
    print('''
    {:.2f} F
    {:.2f} K'''.format(C_para_F, C_para_K))
elif unidade == 'F' and temperatura >= -459.67:
    F_para_C = (temperatura - 32) / 1.8
    F_para_K = (temperatura + 459.67) / 1.8
    print('''
    {:.2f} C
    {:.2f} K'''.format(F_para_C, F_para_K))
elif unidade == 'K' and temperatura >= 0:
    K_para_C = (temperatura - 273.15)
    K_para_F = (temperatura * 1.8) - 459.67
    print('''
    {:.2f} C
    {:.2f} F'''.format(K_para_C, K_para_F))
else:
    print('Valor de temperatura abaixo do minimo')

