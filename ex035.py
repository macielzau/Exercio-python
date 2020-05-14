print('-='*100)
print('Analisador de triagulos')
print('-='*100)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print (' Os seguimentos acima pode formar TRIAGULO !')
else: 
    print(' Os seguimentos acima não podem formar TRIANGULO !')
    
