num = int(input('Digite um numero ' ))
print('''Escolha uam das bases para conversão 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Digite uma opção: ' ))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2: 
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3: 
    print('{} convertido para HEXADECIMAL e igual a {} '.format(num, hex(num)[2:]))
else:
    print ('Valor invalido. Tente novamete ')
