#Constantes
g = 9.81

#Condiciones iniciales
# x0 = 0
# y0 = 0
# vy0 = 10
# vx0 = 6
print('Dame las condiciones iniciales')
x0 = float(input('x0='))
y0 = float(input('y0='))
vx0 = float(input('vx0='))
vy0 = float(input('vy0='))


t=10

#Calculando posicion
x = vx0 * t + x0
y = y0 + vy0 * t - 0.5 * g * t ** 2

print('La posicion de la particula es:')
print('x={}\ny={}'.format(x,y))
