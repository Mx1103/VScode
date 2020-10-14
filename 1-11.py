import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def  f(t):
    return 2*np.exp(0.475*-t)
a = np.arange(-4.5,4,0.04)
ax.plot(a,f(a))
ax.plot(-a,f(a))
ax.spines['top'].set_visible(False)     
ax.xaxis.set_ticks_position('bottom') 
ax.spines['right'].set_visible(False)   
ax.yaxis.set_ticks_position('left')  
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.annotate('x(t) =Ce^(s*t),σ>0', xy=(1.48, 3.89), xytext=(3.05, 3.1),arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('x(t) =Ce^(-s*t),σ<0', xy=(-1.48, 3.89), xytext=(-5.3, 2.01),arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()