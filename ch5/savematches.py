#!/usr/bin/env python
import PIL.Image as Image
import homography 
import sfm
import sift
from numpy import *
from matplotlib.pylab import *
# calibration
print "load images and compute features"
im1 = array(Image.open('../data/alcatraz1.jpg')) 
sift.process_image('../data/alcatraz1.jpg','im1.sift')
l1,d1 = sift.read_features_from_file('im1.sift')
im2 = array(Image.open('../data/alcatraz2.jpg'))
sift.process_image('../data/alcatraz2.jpg','im2.sift')
l2,d2 = sift.read_features_from_file('im2.sift')
print "match features"
matches = sift.match_twosided(d1,d2)
savetxt("matches.txt",matches)
