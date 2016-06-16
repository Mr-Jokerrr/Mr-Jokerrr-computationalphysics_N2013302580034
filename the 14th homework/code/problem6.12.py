# -*- coding: utf-8 -*-  
import numpy as np 
import math
from matplotlib import pyplot as plt 
from matplotlib import animation 

#	set patameters
dx = 0.001
c = 300
k = 1000
x0 = 0.3
N = int(1/dx)
x = np.linspace(0,1,N+1)
y = []
y_c = []
y_p = []

#	set initial values
for i in range(N):
	if i<=x0/dx:
		y.append(i*dx/x0)
		y_c.append(i*dx/x0)
		y_p.append(i*dx/x0)
		i+=1
	else:
		y.append(1-1/(1-x0)*(i*dx-x0))
		y_c.append(1-1/(1-x0)*(i*dx-x0))
		y_p.append(1-1/(1-x0)*(i*dx-x0))
		i+=1

y.append(0)
y_c.append(0)
y_p.append(0)

Length=10000
y_array = [[0 for col in range(N+1)] for row in range(Length)] 

#	main program
t=0
while t<Length:
	i=1
	while i < N:
		y[i] = - y_p[i] + y_c[i+1] + y_c[i-1]
		y_array[t][i]=y[i]
		i+=1
	i=1
	while i<N:
		y_p[i]=y_c[i]
		y_c[i]=y[i]
		i+=1
	t+=1

#	show the results
fig = plt.figure() 
ax = plt.axes(xlim=(0, 1), ylim=(-1.2, 1.2)) 
line, = ax.plot([], [], lw=1) 

def init(): 
	yi=[]
	xi = np.linspace(0,1,N+1)
	for i in range(N):
		if i<=x0/dx:
			yi.append(i*dx/x0)
			i+=1
		else:
			yi.append(1-1/(1-x0)*(i*dx-x0))
			i+=1
	yi.append(0)
	line.set_data(xi, yi) 
	return line, 

def animate(i): 
	x = np.linspace(0,1,N+1)
	y = i
	line.set_data(x, y) 
	return line, 

anim = animation.FuncAnimation(fig, animate, y_array, init_func=init, 
                 interval=1, blit=True) 

plt.show()