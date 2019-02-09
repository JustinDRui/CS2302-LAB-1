#Justin Ruiloba
#Lab 1
#2/8/19
import numpy as np
import matplotlib.pyplot as plt
import math

def draw_squares(ax,n,p):
    if n>0:
        #print("\nN =",n)
        #print("p",p[:,0])
        ax.plot(p[:,0],p[:,1],color='k')

        #make copy of p into left
        #shrink x & move over the size of itself
        #move it down the size of itself
        left=np.divide(p,1)
        left[:,0]=np.divide(p[:,0],2)
        left[:,0]=left[:,0]-orig_size
        left[:,1]=left[:,1]-orig_size

        #make copy of p into right
        #shrink x & move over the size of itself
        #move it down the size of itself
        right=np.divide(p,1)
        right[:,0]=np.divide(p[:,0],2)
        right[:,0]=right[:,0]+orig_size
        right[:,1]=right[:,1]-orig_size
        #call left and right
        draw_squares(ax,n-1,left)
        draw_squares(ax,n-1,right)


orig_size = 1000

p = np.array([[-orig_size,0],[0,orig_size],[orig_size,0]])
fig, ax = plt.subplots()
draw_squares(ax,3,p)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('trianglesa.png')
#end of a 

p = np.array([[-orig_size,0],[0,orig_size],[orig_size,0]])
fig, ax = plt.subplots()
draw_squares(ax,4,p)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('trianglesb.png')
#end of b

p = np.array([[-orig_size,0],[0,orig_size],[orig_size,0]])
fig, ax = plt.subplots()
draw_squares(ax,6,p)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('trianglesc.png')