'''# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

#	set parameter
dl = 0.1
border_l = 2
distance_x = 0.5
distance_y = 0.3
length = 1
N = int(border_l/dl)
V1 = [[0.0] * (N+1) for row in range(N+1)]
V2 = [[0.0] * (N+1) for row in range(N+1)]

n = i = x = y = 0
L = 1000

y1 = int((1-distance_y)/dl)
y2 = int((1+distance_y)/dl+1)
x_min = int((1-distance_x)/dl)
x_max = int((1+distance_x)/dl)
x = x_min

while x<=x_max:
	V1[x][y1]=V1[x][y2]=V2[x][y1]=V2[x][y2]=1.00
	x += 1

	
	
x = 5
y = 6
print V1[6][6]
print V1[4][6]
print V1[5][5]
print V1[5][7]
V2[x][y] = 1.0/4.0*(V1[x-1][y]+V1[x+1][y]+V1[x][y-1]+V1[x][y+1])

print V1[x-1][y]
print V1[x+1][y]
print V1[x][y-1]
print V1[x][y+1]
print ""
print V2[x][y]
while i<N+1:
	print V2[i][:]
	i+=1


while x<N:
	while y<N:
		V2[x][y] = 1/4*(V1[x-1][y]+V1[x+1][y]+V1[x][y-1]+V1[x][y+1])
		y += 1
	y = 1
	x += 1


	

i=0
while i<N+1:
	print V1[i][:]
	i+=1
i=0
while i<N+1:
	print V2[i][:]
	i+=1
'''

from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm  
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
import numpy as np  
 
fig = plt.figure()  
ax = fig.gca(projection='3d')  
X = np.arange(-5, 5, 1)  
Y = np.arange(-5, 5, 1)  
X, Y = np.meshgrid(X, Y)  
R = np.sqrt(X**2 + Y**2)  
Z = np.sin(R)
print X
print ""
print Y
print ""
print Z
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,  
        linewidth=0, antialiased=False)  
ax.set_zlim(-1.01, 1.01)  
 
ax.zaxis.set_major_locator(LinearLocator(10))  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  
 
fig.colorbar(surf, shrink=0.5, aspect=5)  
 
plt.show()