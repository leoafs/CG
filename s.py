from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

year = 0
day = 0

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)


import time

start_time = time.time()

def display():

    t = time.time() - start_time
    year_period = 120.0                  # 120 seconds for simulating one year 
    year     = (t / year_period)
    day      = 365 * year
    moon_sid = (365 / 27.3) * year

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )

    #SOL
    glColor4f (1.0, 1.0, 0, 1)
    #glRotatef(0.1, 0.0, 1.0, 0.0)     
    glutSolidSphere(1.0, 20, 16)
    glPushMatrix()

    #Planeta1 
    glRotatef(year*360.0, 0.0, 1.0, 0.0)     # earth rotation around the sun 
    glTranslatef(2.0, 0.0, 0.0)              # earth location
              
    glPushMatrix()                           # push earth system               
    glRotatef(day*360.0, 1.0, 0.0, 0.0)      # earth spinn
    glRotatef(90-23.4, 0.0, 1.0, 0.0)        # earth axis
    glColor3f (0, 0, 1)                      # blue
    glutWireSphere(0.3, 10, 8)               
    glutSolidSphere(0.3, 10, 8)             
    glPopMatrix()
    #LUA1
    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) # moon sidereal
    glTranslatef(1.0, 0.0, 0.0)              # distance moon to earth
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor4f (0.4, 0.5, 0.6, 1)                         
    glutWireSphere(0.1, 10, 8)               # moon
    glPopMatrix()

    #LUA2
    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 1.0) # moon sidereal
    glTranslatef(0.0, 1.0, 0.0)              # distance moon to earth
    glRotatef(90, 0.0, 1.0, 0.0)
    glColor4f (0.4, 0.5, 0.6, 1)                         
    glutWireSphere(0.1, 10, 8)               # moon
    glPopMatrix()

    glPopMatrix()      

    #Planeta2
    glPushMatrix()
    glRotatef((-1)*year*360.0, 0.0, 1.0, 0.0)     # earth rotation around the sun 
    glTranslatef(-3.0, 0.0, 0.0)              # earth location
    glRotatef(day*360.0, 0.0, 1.0, 0.0)      # earth spinn
    glRotatef(90-23.4, 90-23.4, 0.0, 0.0)        # earth axis
    glColor3f (1, 0, 0)                      
    glutWireSphere(0.3, 20, 8)               # earth
    #glutSolidSphere(0.3, 12, 8) 
    glPopMatrix()
    
    glutPostRedisplay()
    glutSwapBuffers()
    
def reshape(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(70.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition (100, 100)
glutCreateWindow("Transformation")
init ()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
