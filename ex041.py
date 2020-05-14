from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nacsimento: '))
idade = atual - nascimento
print('Atleta tem {} anos.'.format(idade))
if idade <= 9:
    print(' Você ainda e um nadador mirim ')
elif idade <= 14:
    print(' Você é um nadador infantil ')
elif idade <= 19:
    print('Você é um nadador junior ')
elif idade <= 25:
    print('Você é um nadador sênior ')
elif idade >=26:
    print('Está na hora de se aposenta ')
