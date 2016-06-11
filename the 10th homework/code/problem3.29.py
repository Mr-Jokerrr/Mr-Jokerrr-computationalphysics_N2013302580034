# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

#parameter
r = 165
sigma = 10.0
b = 8.0/3.0
dt = 0.0001
x = 1.0
dx = dy = dz = t = y = z = 0
x_array = []
y_array = []
z_array = []
t_array = []

while t<30:
	x_array.append(x)
	y_array.append(y)
	z_array.append(z)
	t_array.append(t)
	
	dx = sigma*(y-x)*dt
	dy = (-x*z + r*x - y)*dt
	dz = (x*y - b*z)*dt
	
	x += dx
	y += dy
	z += dz
	t += dt

plt.plot(t_array,z_array,'.k')
plt.title('$Problem3.26$',fontsize=28)
plt.xlabel('t',fontsize=20)
plt.ylabel('z',fontsize=20)
plt.text(20,300,'r=165',color='black',ha='center',fontsize=20)
plt.show()
