velocidade = float(input('Qual a velocidade atual do carro ? '))
if (velocidade > 80.0):
    print('MULTADO ! você execedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar a multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com seguranca !')
