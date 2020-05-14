from math import radians, sin, cos, tan
an = float(input(' Digite o angulo: '))
se = sin(radians(an))
print(' O angulo de {} tem SENO de {:.2f}'.format(an, se))
co = cos(radians(an))
print(' o angulo de {} tem o COSSENO de {:.2f}'.format(an, co))
ta = tan(radians(an)) 
print(' o angulo de {} tem TANGENTE de {:.2f}'.format(an, ta))
