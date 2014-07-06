#!/usr/bin/env python
import sfm
from numpy import *
from matplotlib.pylab import *
execfile("load_vggdata.py")
# index for points in first two views
ndx = (corr[:,0]>=0) & (corr[:,1]>=0)
# get coordinates and make homogeneous
x1 = points2D[0][:,corr[ndx,0]]
x1 = vstack( (x1,ones(x1.shape[1])) ) 
x2 = points2D[1][:,corr[ndx,1]]
x2 = vstack( (x2,ones(x2.shape[1])) )
Xtrue = points3D[:,ndx]
Xtrue = vstack( (Xtrue,ones(Xtrue.shape[1])) )
# check first 3 points
Xest = sfm.triangulate(x1,x2,P[0].P,P[1].P)
print Xest[:,:3]
print Xtrue[:,:3]
# plotting
from mpl_toolkits.mplot3d import axes3d 
fig = figure()
ax = fig.gca(projection='3d') 
ax.plot(Xest[0],Xest[1],Xest[2],'ko') 
ax.plot(Xtrue[0],Xtrue[1],Xtrue[2],'r.') 
axis('equal')
show()
