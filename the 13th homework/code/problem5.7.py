# -- coding utf-8 --
import math
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm  
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
import numpy as np 

#	set parameter
dl = 0.02
border_l = 2
distance_x = 0.5
distance_y = 0.3
length = 1
N = int(border_l/dl)
V = [[0.0] * (N+1) for row in range(N+1)]
V_old = [[0.0] * (N+1) for row in range(N+1)]

i = x = y = 0
L = 5000
alpha = 2/(1+math.pi/L)
x_array=[]
y_array=[]
z_array=[]

#	set initial value
y1 = int((1-distance_y)/dl)
y2 = int((1+distance_y)/dl+1)
x_min = int((1-distance_x)/dl)
x_max = int((1+distance_x)/dl)
x = x_min
while x<=x_max:
	V[x][y1]=1.00
	V[x][y2]=-1.00
	x += 1

	
'''
	main program
	
'''
while i < L:
	x = x_min-1
	V_old = V
	while x>0:
		V[x][y1] = 1.0/4.0*(V[x-1][y1]+V[x+1][y1]+V[x][y1-1]+V[x][y1+1])
		V[x][y2] = 1.0/4.0*(V[x-1][y2]+V[x+1][y2]+V[x][y2-1]+V[x][y2+1])
		x -= 1
	x = x_max+1
	while x<N:
		V[x][y1] = 1.0/4.0*(V[x-1][y1]+V[x+1][y1]+V[x][y1-1]+V[x][y1+1])
		V[x][y2] = 1.0/4.0*(V[x-1][y2]+V[x+1][y2]+V[x][y2-1]+V[x][y2+1])
		x += 1
	x=1
	y=y1-1
	while x<N:
		while y>0:
			V[x][y] = 1.0/4.0*(V[x-1][y]+V[x+1][y]+V[x][y-1]+V[x][y+1])
			y -= 1
		y = y1-1
		x += 1
	x=1
	y=y1+1
	while x<N:
		while y<=int(N/2):
			V[x][y] = 1.0/4.0*(V[x-1][y]+V[x+1][y]+V[x][y-1]+V[x][y+1])
			y += 1
		y = y1+1
		x += 1
		
	x=1
	y=y2+1
	while x<N:
		while y<N:
			V[x][y] = 1.0/4.0*(V[x-1][y]+V[x+1][y]+V[x][y-1]+V[x][y+1])
			y += 1
		y = y2+1
		x += 1
		
	x=1
	y=y2-1
	while x<N:
		while y>int(N/2):
			V[x][y] = 1.0/4.0*(V[x-1][y]+V[x+1][y]+V[x][y-1]+V[x][y+1])
			y -= 1
		y = y2-1
		x += 1
	x = y = 1
	while x<N:
		while y<N:
			V[x][y] = alpha*(V[x][y]-V_old[x][y])+V_old[x][y]
			y += 1
		y = 1
		x += 1
	i += 1

#	show the figure
fig = plt.figure()  
ax = fig.gca(projection='3d') 

x_array=np.arange(0,N+1,1)
y_array=np.arange(0,N+1,1)
x_array, y_array = np.meshgrid(x_array, y_array)
surf = ax.plot_surface(x_array, y_array, V, rstride=1, cstride=1, cmap=cm.jet,  
		linewidth=0, antialiased=False) 
			
ax.set_zlim(-1.01, 1.01)  

ax.zaxis.set_major_locator(LinearLocator(10))  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  

fig.colorbar(surf, shrink=0.5, aspect=5)  

plt.show() 