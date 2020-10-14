import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def  f(t):
    return 2*np.exp(0.475*-t)*np.cos(3/2*np.pi*t)
a = np.arange(-4.5,4,0.04)
ax.plot(-a,f(a))

ax.spines['top'].set_visible(False)     
ax.xaxis.set_ticks_position('bottom') 
ax.spines['right'].set_visible(False)   
ax.yaxis.set_ticks_position('left')  
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.annotate('x(t) =Ce^(σ*t)*cos(ω*t+φ),σ>0', xy=(1.33, 3.78), xytext=(0.15, 13.70),arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()