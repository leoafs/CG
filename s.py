from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


year=0
day=0

paused = False 
start_time = time.time()

def display():

   
    global t,year_period, year, day

    if not paused:
         t = time.time() - start_time
         year_period = 120.0                  # 120 seconds for simulating one year 
         year = (t / year_period)
         day  = 365 * year

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )

    #SOL
    glColor4f (1.0, 1.0, 0, 0)
    #glRotatef(90, 0.0, 0.0, 0.0)     
    glutSolidSphere(1, 20, 20)
    #glutWireSphere(1.0, 20, 20)
    glPushMatrix()

    #Planeta1 
    glRotatef(year*360.0, 0.0, 1.0, 0.0)     # Rotação em torno do sol 
    glTranslatef(3.0, 0.0, 0.0)              # posição do planeta 1 em relação ao sol
    glPushMatrix()                           # push               
    glColor3f (0, 0, 1)                      # Azul
    glutSolidSphere(0.3, 12, 12)
    glPopMatrix()

    
    #LUA1
    glPushMatrix()
    glRotatef(day*45, 0.0, 1.0, 0.0)         # translação da lua 1 em torno do planeta 1
    glTranslatef(0.45, 0.0, 0.0)              # deslocamento da lua 1 em relação ao planeta
    glColor3f (0.4, 0.5, 0.6)                         
    glutSolidSphere(0.08, 10,10)              # LUA 1
    
    glPopMatrix()

    #LUA2
    glPushMatrix()
    glRotatef(day*24, 0.5,0.5, 0.5)          # translação da lua 2 em torno do planeta 2
    glTranslatef(0.0, 0.5, -0.5)            #  deslocamento da lua 2 em relação ao planeta
    glColor3f (0.4, 0.5, 0.6)                       
    glutSolidSphere(0.08, 10, 10)              # LUA 2
    glPopMatrix()

    glPopMatrix()      

    #Planeta2
    glPushMatrix()
    glRotatef((-1)*year*360.0, 0.0, 1.0, 0.0)     # planeta 2 em torno do sol
    glTranslatef(4.0, 0.0, 0.0)              
    #glRotatef(day*45, 0.0, 1.0, 0.0)              
    glRotatef(90, 1, 0, 0)        
    glColor3f (1, 0, 0)                           #Vermelho    
    #glutWireSphere(0.3, 10, 8)               
    glutSolidSphere(0.3, 12, 12)                  #Planeta 2
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
   gluLookAt (0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    
def Y(*args):

    global paused
    if args[0] == b'y':
        paused = not paused
        
    glutPostRedisplay()


    
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(900, 800)
glutInitWindowPosition (100, 100)
glutCreateWindow("Leonardo")
glutIdleFunc(display)
glutKeyboardFunc(Y)
glutDisplayFunc(display)
glutReshapeFunc(reshape)

glutMainLoop()
