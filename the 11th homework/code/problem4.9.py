# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

#parameter
dt = 0.001

m = 1.0
x = 1.0
y = 0
vx = 0
vy = 2.25*math.pi
ax = 0
ay = 0

x_array = []
y_array = []

i=0
while i<10000:
	x_array.append(x)
	y_array.append(y)
	
	r = math.sqrt(x**2+y**2)

	ax = 4*(math.pi)**2*m*x/(r**3.05)
	ay = 4*(math.pi)**2*m*y/(r**3.05)
	
	vx -= ax*dt
	vy -= ay*dt
	
	x += vx*dt
	y += vy*dt

	i += 1

plt.plot(x_array,y_array,'.k')
plt.title('$Problem4.9$',fontsize=28)
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.text(1,1,u'Vy=2.25\u03C0',color='black',ha='center',fontsize=20)
plt.show()