import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.set_xlim([-6, 6])   #X轴的区间
ax.set_ylim([-3, 3])     #Y轴区间

def  f(t):
    return np.cos(0.7*np.pi*t-1)
a = np.arange(-7,5,0.05)
ax.plot(a,f(a))

ax.spines['top'].set_visible(False)     
ax.xaxis.set_ticks_position('bottom') 
ax.spines['right'].set_visible(False)   
ax.yaxis.set_ticks_position('left')  
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.annotate('x(t) =Acos(ω*t+φ)', xy=(0.73, 1), xytext=(1.52, 2.21),arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()