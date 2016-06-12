# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math


#	set parameter
dt = 0.005
GMs = 4*(math.pi**2)
GMj = 0.00095*GMs

x1 = 3
y1 = 0
vx1 = 0
vy1 = 3.628
ax1 = 0
ay1 = 0

x2 = 3.276
y2 = 0
vx2 = 0
vy2 = 3.471
ax2 = 0
ay2 = 0

x3 = 3.700
y3 = 0
vx3 = 0
vy3 = 3.267
ax3 = 0
ay3 = 0

xj = 5.20
yj = 0
vxj = 0
vyj = 2.755
axj = 0
ayj = 0

x1_array = []
y1_array = []
x2_array = []
y2_array = []
x3_array = []
y3_array = []
xj_array = []
yj_array = []

i=0
while i<10000:
	x1_array.append(x1)
	y1_array.append(y1)
	x2_array.append(x2)
	y2_array.append(y2)
	x3_array.append(x3)
	y3_array.append(y3)
	xj_array.append(xj)
	yj_array.append(yj)
	
	r1j = math.sqrt((x1-xj)**2+(y1-yj)**2)
	r2j = math.sqrt((x2-xj)**2+(y2-yj)**2)
	r3j = math.sqrt((x3-xj)**2+(y3-yj)**2)
	
	r1s = math.sqrt(x1**2+y1**2)
	r2s = math.sqrt(x2**2+y2**2)
	r3s = math.sqrt(x3**2+y3**2)
	rjs = math.sqrt(xj**2+yj**2)
	
	ax1 = GMj*(xj-x1)/(r1j**3)-GMs*x1/(r1s**3)
	ay1 = GMj*(yj-y1)/(r1j**3)-GMs*y1/(r1s**3)
	ax2 = GMj*(xj-x2)/(r2j**3)-GMs*x2/(r2s**3)
	ay2 = GMj*(yj-y2)/(r2j**3)-GMs*y2/(r2s**3)
	ax3 = GMj*(xj-x3)/(r1j**3)-GMs*x3/(r3s**3)
	ay3 = GMj*(yj-y3)/(r1j**3)-GMs*y3/(r3s**3)
	axj = -GMj*xj/(rjs**3)-GMs*xj/(rjs**3)
	ayj = -GMj*yj/(rjs**3)-GMs*yj/(rjs**3)

	vx1 += ax1*dt
	vy1 += ay1*dt
	vx2 += ax2*dt
	vy2 += ay2*dt
	vx3 += ax3*dt
	vy3 += ay3*dt
	vxj += axj*dt
	vyj += ayj*dt
	
	x1 += vx1*dt
	y1 += vy1*dt
	x2 += vx2*dt
	y2 += vy2*dt
	x3 += vx3*dt
	y3 += vy3*dt
	xj += vxj*dt
	yj += vyj*dt

	i += 1

plt.plot(x1_array,y1_array,'.k')
plt.plot(x2_array,y2_array,'.b')
plt.plot(x3_array,y3_array,'.r')
plt.plot(xj_array,yj_array,'.g')
plt.title('$Problem4.18$',fontsize=28)
plt.xlabel('x(AU)',fontsize=20)
plt.ylabel('y(AU)',fontsize=20)
#plt.text(1,14,'r=10',color='black',ha='center',fontsize=20)
plt.show()