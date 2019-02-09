#Justin Ruiloba
#Lab 1 
#2/7/2019
import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,array_pts):
    if n>0:
        #Dividing all elements in array_pts by 2 to half the size then then subtracting by 400 to shift square left and down to draw bottom right square.
        q1= np.subtract(np.divide(array_pts,2),400)
		#Dividing all elements in array_pts by 2 to half the size then then subtracting by 400 to shift square right and up to draw top right square.
        q2= np.add(np.divide(array_pts,2),400)
		#Divide all elements in array_pts by 2 to half the size.
        q3= np.divide(array_pts,2)
		#Subtracting only the X values of q3 by 400 to shift left.
        q3[:,0]= np.subtract(q3[:,0],400)
		#Adding only the Y values of q3 by 400 to shift up to draw top left square.
        q3[:,1]=np.add(q3[:,1],400)
		#Divide all elements in array_pts by 2 to half the size.
        q4= np.divide(array_pts,2)
		#Adding only the X values of q4 to shift to the right.
        q4[:,0]= np.add(q4[:,0],400)
		#Subtracting only the Y values of q4 to shift down and draw the bottom right square
        q4[:,1]=np.subtract(q4[:,1],400)
        #q4= np.subtract(q3[:,]-400)
       
        #print("q4",array_pts[:,:])
        #print("q4 col 1 =",q3[:,0])
		#plot all squares
		#draws orig_square
        ax.plot(array_pts[:,0],array_pts[:,1],color='k')
        #recursive call and draw each  corner square
        draw_squares(ax,n-1,q1)
        draw_squares(ax,n-1,q2)
        draw_squares(ax,n-1,q3)
        draw_squares(ax,n-1,q4)
#end of draw_squares()    

plt.close("all") 
s = 800
#array_pts= np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#array_pts= np.array([[0,0],[-400,0],[-400,400],[0,400],[0,0]])
array_pts= np.array([[-s,-s],[-s,s],[s,s],[s,-s],[-s,-s]])
array_pts=array_pts/2
fig, ax = plt.subplots()
draw_squares(ax,2,array_pts)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squaresa.png')
#end of a

plt.close("all") 
s = 800
#array_pts= np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#array_pts= np.array([[0,0],[-400,0],[-400,400],[0,400],[0,0]])
array_pts= np.array([[-s,-s],[-s,s],[s,s],[s,-s],[-s,-s]])
array_pts=array_pts/2
fig, ax = plt.subplots()
draw_squares(ax,3,array_pts)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squaresb.png')
#end of b

plt.close("all") 
s = 800
#array_pts= np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
#array_pts= np.array([[0,0],[-400,0],[-400,400],[0,400],[0,0]])
array_pts= np.array([[-s,-s],[-s,s],[s,s],[s,-s],[-s,-s]])
array_pts=array_pts/2
fig, ax = plt.subplots()
draw_squares(ax,4,array_pts)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squaresc.png')
