# -*- coding: utf-8 -*-  
import numpy as np 
import math
from matplotlib import pyplot as plt 
from matplotlib import animation 

#	set patameters
dx = 0.002
c = 300
k = 1000
x0 = 0.3
N = int(1/dx)

x = np.linspace(0,1,N+1)
y = np.exp(-k*(x-x0)**2)
y_c = np.exp(-k*(x-x0)**2)
y_p = np.exp(-k*(x-x0)**2)
y[0]=y[N]=0
y_c[0]=y_c[N]=0
y_p[0]=y_p[N]=0

Length=1000
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
	x = np.linspace(0,1,N+1)
	y = np.exp(-k*(x-x0)**2)
	y[0]=y[N]=0
	line.set_data(x, y) 
	return line, 

def animate(i): 
	x = np.linspace(0,1,N+1)
	y = i
	line.set_data(x, y) 
	return line, 

anim = animation.FuncAnimation(fig, animate, y_array, init_func=init, 
                 interval=10, blit=True) 

plt.show()
