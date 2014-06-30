#!/usr/bin/env python
from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *
import pickle
from numpy import *
import sys
import Image
def set_projection_from_camera(K):
    """ Set view from a camera calibration matrix. """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    fx = K[0,0]
    fy = K[1,1]
    fovy = 2*arctan(0.5*height/fy)*180/pi
    aspect = (width*fy)/(height*fx)
    # define the near and far clipping planes
    near = 0.1 
    far = 100.0
    # set perspective
    gluPerspective(fovy,aspect,near,far) 
    glViewport(0,0,width,height)
def set_modelview_from_camera(Rt):
    """ Set the model view matrix from camera pose. """
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()
    # rotate teapot 90 deg around x-axis so that z-axis is up
    Rx = array([[1,0,0],[0,0,-1],[0,1,0]])
    # set rotation to best approximation
    R = Rt[:,:3]
    U,S,V = linalg.svd(R)
    R = dot(U,V)
    R[0,:] = -R[0,:] # change sign of x-axis
    # set translation
    t = Rt[:,3]
    # setup 4*4 model view matrix
    M = eye(4)
    M[:3,:3] = dot(R,Rx) 
    M[:3,3] = t
    # transpose and flatten to get column order
    M = M.T
    m = M.flatten()
    # replace model view with the new matrix
    glLoadMatrixf(m)
def load_texture(imname):
    # load background image (should be .bmp) to OpenGL texture
    bg_image = Image.open(imname) 
    bg_data = bg_image.convert("RGBA").tostring("raw","RGBA")
    tex_id=glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,tex_id) 
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,width,height,0,GL_RGBA,GL_UNSIGNED_BYTE,bg_data) 
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST) 
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    return tex_id
def draw_background(texId):
    """ Draw background image using a quad. """
    glDisable(GL_LIGHTING)
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # bind the texture
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D,tex_id) 
    # create quad to fill the whole window
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,1.0); glVertex3f(-1.0,-1.0,-1.0)
    glTexCoord2f(1.0,1.0); glVertex3f( 1.0,-1.0,-1.0) 
    glTexCoord2f(1.0,0.0); glVertex3f( 1.0, 1.0,-1.0) 
    glTexCoord2f(0.0,0.0); glVertex3f(-1.0, 1.0,-1.0) 
    glEnd()
    glDisable(GL_TEXTURE_2D)
def draw_teapot(size):
    """ Draw a red teapot at the origin. """
    glEnable(GL_LIGHTING) 
    glEnable(GL_LIGHT0) 
    glEnable(GL_DEPTH_TEST)
    glClear(GL_DEPTH_BUFFER_BIT)
    # draw red teapot
    glMaterialfv(GL_FRONT,GL_AMBIENT,[0,0,0,0]) 
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[0.5,0.0,0.0,0.0]) 
    glMaterialfv(GL_FRONT,GL_SPECULAR,[0.7,0.6,0.6,0.0]) 
    glMaterialf(GL_FRONT,GL_SHININESS,0.25*128.0) 
    glutSolidTeapot(size)
def init():
    glEnable(GL_DEPTH_TEST)
def resize(w,h):
    glViewport(0,0,w,h)
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_background(tex_id) 
    set_projection_from_camera(K) 
    set_modelview_from_camera(Rt) 
    draw_teapot(0.2)
    glutSwapBuffers()
def keyPressed(*args):
    sys.exit()
# main
width,height = 1000,747
# load camera data
with open('ar_camera.pkl','r') as f: 
    K = pickle.load(f)
    Rt = pickle.load(f)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width,height)
glutInitWindowPosition(0,0)
glutCreateWindow("OpenGL AR demo")
glutIdleFunc(draw)
glutDisplayFunc(draw)
glutReshapeFunc(resize)
glutKeyboardFunc(keyPressed)
tex_id=load_texture('../data/book_perspective.bmp')
glutMainLoop()
