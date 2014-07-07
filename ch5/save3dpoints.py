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
print "match features"
matches = int32(loadtxt("matches.txt"))
ndx = matches.nonzero()[0]
# make homogeneous and normalize with inv(K)
x1 = homography.make_homog(l1[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
x2 = homography.make_homog(l2[ndx2,:2].T)
x1n = dot(inv(K),x1)
x2n = dot(inv(K),x2)
print "estimate E with RANSAC"
model = sfm.RansacModel()
E,inliers = sfm.F_from_ransac(x1n,x2n,model,50)
print "compute camera matrices (P2 will be list of four solutions)"
P1 = array([[1,0,0,0],[0,1,0,0],[0,0,1,0]]) 
P2 = sfm.compute_P_from_essential(E)
print "pick the solution with points in front of cameras"
ind = 0
maxres = 0
for i in range(4):
    # triangulate inliers and compute depth for each camera
    X = sfm.triangulate(x1n[:,inliers],x2n[:,inliers],P1,P2[i]) 
    d1 = dot(P1,X)[2]
    d2 = dot(P2[i],X)[2]
    if sum(d1>0)+sum(d2>0) > maxres:
        maxres = sum(d1>0)+sum(d2>0) 
        ind = i
        infront = (d1>0) & (d2>0)
    # triangulate inliers and remove points not in front of both cameras
X = sfm.triangulate(x1n[:,inliers],x2n[:,inliers],P1,P2[ind]) 
X = X[:,infront]
savetxt("3dpoints.txt",X)
savetxt("p1.txt",P1)
savetxt("p2.txt",P2[ind])
