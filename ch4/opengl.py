#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
t=0.3
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #set projection matrix begin
    glMatrixMode(GL_PROJECTION)
    m=eye(4)
    m[3,2]=-0.4
    m=m.T
    m.flatten()
    glLoadMatrixf(m)
    #set projection matrix end
    #set modelview matrix begin
    glMatrixMode(GL_MODELVIEW)
    m=eye(4)
    m[0,3]=t
    m=m.T
    glLoadMatrixf(m)
    #set modelview matrix end
    #draw triangle 1 begin
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.0,0.0,-0.5)
    glVertex3f(0.0,0.5,-0.5)
    glVertex3f(0.5,0.5,-0.5)
    glEnd()
    #draw triangle 1 end
    #set another projection matrix begin 
    glMatrixMode(GL_PROJECTION)
    m=eye(4)
    m.flatten()
    glLoadMatrixf(m)
    #set another projection matrix end
    #draw triangle 2 begin
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(-0.2,0.0,-1.0)

    glVertex3f(-0.7,0.5,-1.0)
    glVertex3f(-0.2,0.5,-1.0)

    glEnd()
    glutSwapBuffers()
def keypressed(key,x,y):
    global t
    #import sys
    #sys.exit(0)
    t=t+0.1
#opengl main
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800,600)
glutCreateWindow("OpenGL demo")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutKeyboardFunc(keypressed)
glutMainLoop()

