#!/usr/bin/env python
import sfm
from numpy import *
from matplotlib.pylab import *
execfile('load_vggdata.py')
# index for points in first two views
ndx = (corr[:,0]>=0) & (corr[:,1]>=0)
# get coordinates and make homogeneous
x1 = points2D[0][:,corr[ndx,0]]
x1 = vstack( (x1,ones(x1.shape[1])) )
x2 = points2D[1][:,corr[ndx,1]]
x2 = vstack( (x2,ones(x2.shape[1])) )
# compute F
F = sfm.compute_fundamental(x1,x2)
# compute the epipole
e = sfm.compute_epipole(F)
# plotting
figure()
imshow(im1)
# plot each line individually, this gives nice colors
for i in range(5):
    sfm.plot_epipolar_line(im1,F,x2[:,i],e,True)
    plot(x1[0,i],x1[1,i],'o')
title("epipole, epipolar_line and x1 on image1")
axis('off')
show()
figure()
imshow(im2)
# plot each point individually, this gives same colors as the lines
for i in range(5):
    plot(x2[0,i],x2[1,i],'o')
title("x2 on image2")
axis('off')
show()
