import numpy as np

#Constantes
g = 9.81

#Condiciones iniciales
x0 = 0
y0 = 0
vy0 = 10
vx0 = 6

t = np.arange(0, 10, 1)

#Calculando posicion
x = vx0 * t + x0
y = y0 + vy0 * t - 0.5 * g * t ** 2

resultados = np.array([t,x,y]).transpose()

np.savetxt('test.txt', resultados, delimiter=',', header='t,x,y')

f = open('test2.txt', 'w+')
print('#t,x,y', file=f)
np.savetxt(f, resultados, delimiter=',')
f.close()

with open('test3', 'w+') as f:
    print('#t,x,y', file=f) 
    for i in np.arange(len(t)): 
        print('{},{},{}'.format(t[i],x[i],y[i]),file=f)

import pandas as pd
df = pd.DataFrame([t,x,y])
df = df.transpose()
df.columns = ['t','x','y']
df.set_index('t')
df.to_csv('test4')
