casa = float(input(" Valor da casa: R$  " ))
salario = float(input( " Valor do salario ? " ))
anos = int(input('Quantos anos de finaciamento ? ' ))
prestacao = (anos * 12)
minimo = salario * 30 / 100
print (' Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print (' A prestação será de {} '.format(prestacao))
if  prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo negado ' )
