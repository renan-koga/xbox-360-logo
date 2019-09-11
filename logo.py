import sys,struct

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import * 
import numpy as np
from glumpy import app, gl, gloo   

vertex = """
attribute vec2 position;
varying vec2 v_position;
void main() {
    v_position = position;
    gl_Position = vec4(position.xy, 0.0, 1.6);
}
"""

fragment = """
uniform vec2 center;
uniform vec3 color1, color2;
varying vec2 v_position;
void main() {
    float a = length(v_position-center);
    gl_FragColor.rgb = mix(color1, color2, a);
    gl_FragColor.a = 1.0;
}
"""


P = np.zeros((1+100,2), dtype=np.float32)
T = np.linspace(0,2*np.pi, len(P)-1, endpoint = True)
P[1:,0], P[1:,1] = 0.5*np.cos(T) - 0.1 , 0.95*np.sin(T) + 0.5
polygon = gloo.Program(vertex, fragment, count=len(P))
polygon["position"] = P 
polygon["center"] = -0.1, 0.5
polygon["color1"] = 1,1,1
polygon["color2"] = 0.62,0.65,0.65

def init():
   glClearColor(1.0, 1.0, 1.0, 0.0)
   glShadeModel(GL_SMOOTH)

def first_X():
    r,g,b = 151,200,62
    glBegin(GL_POLYGON)
    glColor3ub(r,g,b)
    glVertex2f(338.0, 743.0)
    glVertex2f(390.0, 669.0)
    glVertex2f(368.0, 669.0)
    glVertex2f(326.0, 729.0)
    glVertex2f(284.0, 669.0)
    glVertex2f(262.0, 669.0)
    glVertex2f(315.0, 743.0)   
    glVertex2f(262.0, 819.0)
    glVertex2f(284.0, 819.0)
    glVertex2f(326.0, 757.0)
    glVertex2f(368.0, 819.0)
    glVertex2f(390.0, 819.0)
    glEnd()



def second_X(translate):
    r,g,b = 151,200,62
    glBegin(GL_POLYGON)
    glColor3ub(r,g,b)
    glVertex2f(338.0 + translate, 743.0 )
    glVertex2f(390.0 + translate, 669.0 )
    glVertex2f(368.0 + translate, 669.0 )
    glVertex2f(326.0 + translate, 729.0 )
    glVertex2f(284.0 + translate, 669.0 )
    glVertex2f(262.0 + translate, 669.0 )
    glVertex2f(315.0 + translate, 743.0 )   
    glVertex2f(262.0 + translate, 819.0 )
    glVertex2f(284.0 + translate, 819.0 )
    glVertex2f(326.0 + translate, 757.0 )
    glVertex2f(368.0 + translate, 819.0 )
    glVertex2f(390.0 + translate, 819.0 )
    glEnd()

def begin_B():
    r,g,b = 151,200,62
    glBegin(GL_POLYGON)
    glColor3ub(r,g,b)
    glVertex2f(419.0, 746.0)
    glVertex2f(419.0, 819.0)
    glVertex2f(437.0, 819.0)
    glVertex2f(437.0, 669.0)
    glVertex2f(419.0, 669.0)
    glVertex2f(419.0, 730.0)
    glVertex2f(398.0, 730.0)
    glVertex2f(389.0, 746.0)
    glEnd()

def trademark():
    r,g,b = 161,160,166
    glBegin(GL_POLYGON)
    glColor3ub(r,g,b)
    glVertex2f(1299.0, 805.0)
    glVertex2f(1299.0, 808.0)
    glVertex2f(1311.0, 808.0)
    glVertex2f(1311.0, 805.0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(1307.0, 808.0)
    glVertex2f(1307.0, 819.0)
    glVertex2f(1304.0, 819.0)
    glVertex2f(1304.0, 808.0)
    glEnd()

def display():
   glClear(GL_COLOR_BUFFER_BIT)
   first_X()
   second_X(374.0)
   begin_B()
   polygon.draw(GL_TRIANGLE_FAN)
   trademark()
   glFlush()




def reshape(w, h):
   glViewport(0, 0, w, h)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   if(w <= h):
      gluOrtho2D(0.0, 1600.0, 0.0, 900.0 * h/w)
   else:
      gluOrtho2D(0.0, 1600.0, 900.0, 0.0 )
   glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
   if key == chr(27):
      sys.exit(0)


   
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1600,900)
glutInitWindowPosition(0, 0)
glutCreateWindow(b'xboxzin')
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutMainLoop()