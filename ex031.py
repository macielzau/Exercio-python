distacia = float(input('Qual é a distancia de sua viagem? '))
print('Você está prestes a comecar uma viagem de {}Km,'.format(distacia))
if distacia <= 200:
    preco = distacia * 0.50
else:
    preco = distacia * 0.45
print(' O preço da passagem será {:.2f}'.format(preco))
