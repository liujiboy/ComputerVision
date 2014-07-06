#!/usr/bin/env python
from numpy import *
from matplotlib.pylab import *
execfile('load_vggdata.py')
# make 3D points homogeneous and project
X = vstack( (points3D,ones(points3D.shape[1])) )
x = P[0].project(X)
# plotting the points in view 1
figure()
subplot(121)
imshow(im1)
plot(points2D[0][0],points2D[0][1],'*')
axis('off')
#figure()
subplot(122)
imshow(im1)
plot(x[0],x[1],'r.')
axis('off')
show()

