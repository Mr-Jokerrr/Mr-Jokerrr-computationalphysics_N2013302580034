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
V1 = [[0.0] * (N+1) for row in range(N+1)]
V2 = [[0.0] * (N+1) for row in range(N+1)]

n = i = x = y = 0
L = 50
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
	V1[x][y1]=V2[x][y1]=1.00
	V1[x][y2]=V2[x][y2]=-1.00
	x += 1

	
'''
	main program
	
'''
while i < L:
	if n==0:
		x = y = 1
		while x<N:
			while y<N:
				V1[x][y] = 1.0/4.0*(V2[x-1][y]+V2[x+1][y]+V2[x][y-1]+V2[x][y+1])
				y += 1
			y = 1
			x += 1
		#	set V1(+-0.3,y)=1
		x = x_min
		while x<=x_max:
			V1[x][y1]=1.00
			V1[x][y2]=-1.00
			x += 1
		n = 1
		
	else:
		x = y = 1
		while x<N:
			while y<N:
				V2[x][y] = 1.0/4.0*(V1[x-1][y]+V1[x+1][y]+V1[x][y-1]+V1[x][y+1])
				y += 1
			y = 1
			x += 1
			
		#	set V2(+-0.3,y)=1
		x = x_min
		while x<=x_max:
			V2[x][y1]=1.00
			V2[x][y2]=-1.00
			x += 1
		n = 0
	i += 1

#	show the figure
fig = plt.figure()  
ax = fig.gca(projection='3d') 

x_array=np.arange(0,N+1,1)
y_array=np.arange(0,N+1,1)
x_array, y_array = np.meshgrid(x_array, y_array)
if n==0:
	surf = ax.plot_surface(x_array, y_array, V2, rstride=1, cstride=1, cmap=cm.jet,  
			linewidth=0, antialiased=False) 
else:	
	surf = ax.plot_surface(x_array, y_array, V1, rstride=1, cstride=1, cmap=cm.jet,  
			linewidth=0, antialiased=False) 	
			
ax.set_zlim(-1.01, 1.01)  

ax.zaxis.set_major_locator(LinearLocator(10))  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  

fig.colorbar(surf, shrink=0.5, aspect=5)  

plt.show() 
