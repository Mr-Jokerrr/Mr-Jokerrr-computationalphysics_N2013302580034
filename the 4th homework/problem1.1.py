# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(v0,n):
	g = 9.8
	t = np.arange(0.0,5.0,5.0/n)
	plt.plot(t,v0-g*t,'bo',t,v0-g*t,'k')
	plt.title('$Problem1.1$',fontsize=28)
	plt.xlabel('$t$',fontsize=20)
	plt.ylabel('$V(t)$',fontsize=20)
	plt.show()
	
f(30,10)
