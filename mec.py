livros = int(input('Informe o numero de livros: '))
alunos = int(input('Informe o numero de alunos: '))
conceito = alunos / livros
if conceito < 9:
    print('{}'.format('A'))
elif   8 < conceito < 13:
    print('{}'.format('B'))
elif   12 < conceito < 19:
    print('{}'.format('C'))
else: 
    print('{}'.format('D'))