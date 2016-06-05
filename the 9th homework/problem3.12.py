# -- coding utf-8 --
import numpy as np
import matplotlib.pyplot as plt
import math

#parameter
g = 9.8
l = 9.8
q = 0.5
omega_d = 2.0/3.0
dt = 0.04
fd = 1.2
theta = 0.2
omega = 0
t = 0
k = 0
o_array = []
t_array = []
i=0

def reduce_theta(x):
	if x > math.pi:
		return reduce_theta(x - 2*math.pi)
	elif x < -math.pi:
		return reduce_theta(x + 2*math.pi)
	else:
		return x

while i<500000:
	if abs(t-(2*k*math.pi+math.pi/4)/omega_d)<0.02:
		o_array.append(omega)
		t_array.append(theta)
		k += 1
	
	omega = omega + (-g/l*math.sin(theta)-q*omega + fd*math.sin(omega_d*t))*dt
	theta += omega*dt
	theta = reduce_theta(theta)
	t += dt
	i += 1
	
plt.plot(t_array,o_array,'.k')
plt.text(2.5,1.2,u'$\u03C9$ versus $\u03B8$   Fd=1.2',color='black',ha='center',fontsize=20)
plt.text(2.5,1,u'$\u03c0$/4 out-of-phase',color='black',ha='center',fontsize=20)
plt.title('$Problem3.12$',fontsize=28)
plt.xlabel(u'$\u03C9(omega)$',fontsize=20)
plt.ylabel(u'$\u03B8(theta)$',fontsize=20)
plt.show()
