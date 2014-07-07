#!/usr/bin/env python
import PIL.Image as Image
import homography 
import sfm
import sift
from numpy import *
from matplotlib.pylab import *
# calibration
K = array([[2394,0,932],[0,2398,628],[0,0,1]])
print "load images and compute features"
im1 = array(Image.open('../data/alcatraz1.jpg')) 
l1,d1 = sift.read_features_from_file('im1.sift')
im2 = array(Image.open('../data/alcatraz2.jpg'))
l2,d2 = sift.read_features_from_file('im2.sift')
matches = loadtxt("matches.txt")
ndx = matches.nonzero()[0]
x1 = homography.make_homog(l1[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
x2 = homography.make_homog(l2[ndx2,:2].T)
x1n = dot(inv(K),x1)
x2n = dot(inv(K),x2)
P1 = loadtxt("p1.txt") 
P2 = loadtxt("p2.txt")
X =loadtxt("3dpoints.txt")
print "3D plot"
from mpl_toolkits.mplot3d import axes3d
fig = figure()
ax = fig.gca(projection='3d')
ax.plot(-X[0],X[1],X[2],'k.')
axis('off')
# plot the projection of X
import camera
# project 3D points
cam1 = camera.Camera(P1)
cam2 = camera.Camera(P2)
x1p = cam1.project(X)
x2p = cam2.project(X)
# reverse K normalization
x1p = dot(K,x1p)
x2p = dot(K,x2p)
figure()
imshow(im1)
gray()
plot(x1p[0],x1p[1],'o')
plot(x1[0],x1[1],'r.') 
axis('off')
figure()
imshow(im2)
gray() 
plot(x2p[0],x2p[1],'o')
plot(x2[0],x2[1],'r.')
axis('off')
show()
