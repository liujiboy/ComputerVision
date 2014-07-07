#!/usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
dx=0
dy=0
dz=0
rx=0
ry=0
rz=0
def draw():
    global dx,dy,dz
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #print dx,dy,dz
    gluLookAt(0+dx,0,1+dz,0,0+dx,-10+dz,0,1,0)
    glRotatef(rx,1,0,0)
    glRotatef(ry,0,1,0)
    glRotatef(rz,0,0,1)
    glTranslatef(-cx,-cy,-cz)
    #glScalef(dz,dz,dz)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POINTS)
    for p in points:
        glVertex3f(p[0],p[1],p[2])
    glEnd()
    glutSwapBuffers()
def reshape(w,h):
    glViewport (0, 0, w, h);   
    glMatrixMode (GL_PROJECTION);  
    glLoadIdentity ();  
    gluPerspective(60.0, w/h, 0.001, 100000.0); 
def keypressed(key,x,y):
    global dx,dy,dz,rx,ry,rz
    if key=='w':
        dz=dz-0.01
    if key=='s':
        dz=dz+0.01
    if key=='a':
        dx=dx-0.01
    if key=='d':
        dx=dx+0.01
    if key=='1':
        rx=rx+1
    if key=='2':
        rx=rx-1
    if key=='3':
        ry=ry+1
    if key=='4':
        ry=ry-1
    if key=='5':
        rz=rz+1
    if key=='6':
        rz=rz-1
    if ord(key)==27:
        import sys
        sys.exit(0)
#opengl main
points=loadtxt("3dpoints.txt")
m=max(abs(points[:3,:]).flatten())
points=(points[:3,:]/m).T
cx=mean(points[:,0])
cy=mean(points[:,1])
cz=mean(points[:,2])
print cx,cy,cz
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800,600)
glutCreateWindow("OpenGL demo")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutReshapeFunc(reshape)
glutKeyboardFunc(keypressed)
glutMainLoop()

