nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
conta = (nota1 + nota2) / 2
if conta >=0:
    print(' Sua media foi de {}'.format(conta))
elif conta < 5:
    print(' Você perdeu, por favor estude mais ')
elif conta > 5:
    print('Parabens você passou')
