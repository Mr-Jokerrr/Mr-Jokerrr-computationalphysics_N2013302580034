# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8
l = 1.0
ini_x = 0.2
v = 0
a = 0
dt = 0.001
t = np.arange(0,8,dt)
p1 = []

x = ini_x
for i in range(len(t)):
	p1.append(x)
	a = - g/l*math.sin(x)
	v += a*dt
	x += v*dt
	
plt.plot(t,p1,'k')
plt.text(4,0.26,u'nonlinear pendulum',color='black',ha='center',fontsize=16)
plt.title('$Problem3.8$',fontsize=28)
plt.xlabel('$time(s)$',fontsize=20)
plt.ylabel(u'$\u03B8(radians)$',fontsize=20)
plt.show()
