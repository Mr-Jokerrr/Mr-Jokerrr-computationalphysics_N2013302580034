# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

#parameter
dt = 0.002

m1 = 100.0
x1 = 1
y1 = 0
vx1 = 0
vy1 = 10.0
ax1 = 0
ay1 = 0

m2 = 500.0
x2 = -1
y2 = 0
vx2 = 0
vy2 = -2.0
ax2 = 0
ay2 = 0

x1_array = []
y1_array = []
x2_array = []
y2_array = []

i=0
k=1
while i<1000:
	x1_array.append(x1)
	y1_array.append(y1)
	x2_array.append(x2)
	y2_array.append(y2)
	
	r = math.sqrt((x2-x1)**2+(y2-y1)**2)

	ax1 = m2*(x2-x1)/(r**3)
	ay1 = m2*(y2-y1)/(r**3)
	ax2 = m1*(x1-x2)/(r**3)
	ay2 = m1*(y1-y2)/(r**3)

	vx1 += ax1*dt
	vy1 += ay1*dt
	vx2 += ax2*dt
	vy2 += ay2*dt
	
	x1 += vx1*dt
	y1 += vy1*dt
	x2 += vx2*dt
	y2 += vy2*dt

	i += 1

plt.plot(x1_array,y1_array,'.k')
plt.plot(x2_array,y2_array,'.b')
plt.title('$Problem4.7$',fontsize=28)
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
#plt.text(1,14,'r=10',color='black',ha='center',fontsize=20)
plt.show()