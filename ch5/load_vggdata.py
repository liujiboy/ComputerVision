import camera
from numpy import *
import PIL.Image as Image
# load some images
im1 = array(Image.open('../data/Merton_College_I/001.jpg'))
im2 = array(Image.open('../data/Merton_College_I/002.jpg'))
# load 2D points for each view to a list
points2D = [loadtxt('../data/Merton_College_I/00'+str(i+1)+'.corners').T for i in range(3)]
# load 3D points
points3D = loadtxt('../data/Merton_College_I/p3d').T
# load correspondences
corr = genfromtxt('../data/Merton_College_I/nview-corners',dtype='int',missing='*')
# load cameras to a list of Camera objects
P = [camera.Camera(loadtxt('../data/Merton_College_I/00'+str(i+1)+'.P')) for i in range(3)]
