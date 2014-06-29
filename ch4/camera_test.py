#!/usr/bin/env python
from matplotlib.pylab import *
import camera
from numpy import *
# load points
points=loadtxt("../data/house.p3d").T
points=vstack((points,ones(points.shape[1])))
# setup camera
P=hstack((eye(3),array([[0],[0],[-10]])))
cam=camera.Camera(P)
x=cam.project(points)
# plot projection
figure()
subplot(121)
plot(x[0],x[1],'k.')
r=0.05*random.rand(3)
rot=camera.rotation_matrix(r)
# rotate camera and project
subplot(122)
for t in range(20):
    cam.P=dot(cam.P,rot)
    x=cam.project(points)
    plot(x[0],x[1],'k.')
show()

