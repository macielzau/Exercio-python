ano = int(input('Que ano quer analisar ? '))
if ano % 4==0:
    print('ano {} é BISSEXTO'.format(ano))
else: 
    print (' O ano {} não é BISSEXTO'.format(ano))
