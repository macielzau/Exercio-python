from datetime import date
atual = date.today().year
ano = int(input('Qual ano você nacseu ? ' ))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {} '.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE! ')
elif idade < 18:
    print('Falta pouco para se alista')
elif idade > 18:
    print('Você já deveria ter se alistado, poderá paga multa por atraso ')
