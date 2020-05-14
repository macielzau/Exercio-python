l = float(input(' Largura da sua parede: '))
a = float(input(' Altura de sua parede: '))
ar = l * a
print(' Sua parede tem dimensão de {} x {} e sua areá é de {}m².'.format(l, a, ar))
tinta = ar / 2
print ('Para pintar essa parede, você precisará de {} de tinta.'.format(tinta))
