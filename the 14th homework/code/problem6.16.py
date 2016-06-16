# -*- coding: utf-8 -*-  
import numpy as np 
import math
from matplotlib import pyplot as plt 
from matplotlib import animation 

#	set patameters

'''
#	C2
c = 250
L = 1.9
e = 0.0000075
'''
'''
#	C4
c = 330
L = 0.62
e = 0.000038
'''


#	C7
c = 380
L = 0.09
e = 0.00087


dx = 0.01
k = 1000
x0 = 0.5
dt = dx/4/c
r = c*dt/dx
M = L/dx
N = int(1/dx)

x = np.linspace(0,1,N+3)
y = np.exp(-k*(x-x0)**2)
y_c = np.exp(-k*(x-x0)**2)
y_p = np.exp(-k*(x-x0)**2)

y[1]=y[N+1]=0
y_c[1]=y_c[N+1]=0
y_p[1]=y_p[N+1]=0
y[0]=-y[2]
y[N+2]=-y[N]
y_c[0]=-y_c[2]
y_c[N+2]=-y_c[N]
y_p[0]=-y_p[2]
y_p[N+2]=-y_p[N]

Length=3000
y_array = [[0 for col in range(N+1)] for row in range(Length)] 

#	main program
t=0
while t<Length:
	i=2
	while i < N+1:
		y[i] = (2-2*r**2-6*e*r**2*M**2)*y_c[i]-y_p[i]+r**2*(1+4*e*M**2)*(y_c[i+1]+y_c[i-1])-e*r**2*M**2*(y_c[i+2]+y_c[i-2])
		y_array[t][i-1]=y[i]
		i+=1
	y[0]=-y[2]
	y[N+2]=-y[N]
	i=0
	while i<N+3:
		y_p[i]=y_c[i]
		y_c[i]=y[i]
		i+=1
	t+=1

#	show the results
fig = plt.figure() 
ax = plt.axes(xlim=(0, 1), ylim=(-1.0, 1.0)) 
line, = ax.plot([], [], lw=1) 

def init(): 
	x_temp = np.linspace(0,1,N+1)
	y = np.exp(-k*(x-x0)**2)
	i=1
	y_temp = []
	while i<N+2:
		y_temp.append(y[i])
		i+=1
	line.set_data(x_temp, y_temp) 
	return line, 

def animate(i): 
	x = np.linspace(0,1,N+1)
	y = i
	line.set_data(x, y) 
	return line, 

anim = animation.FuncAnimation(fig, animate, y_array, init_func=init, 
                 interval=10, blit=True) 

plt.show()
