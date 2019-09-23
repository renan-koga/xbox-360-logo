# -----------------------------------------------------------------------------
# Python, OpenGL & Scientific Visualization
# www.labri.fr/perso/nrougier/python+opengl
# Copyright (c) 2018, Nicolas P. Rougier
# Distributed under the 2-Clause BSD License.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app, gl, gloo
from OpenGL.GL import *
from OpenGL.GLU import *

vertex = """
attribute vec2 position;
varying vec2 v_position;
void main() {
    v_position = position;
    gl_Position = vec4(position.xy, 0.0, 1.0);
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

vertexes = [
    ()
]

def bezier(A, B, C, D, t):
    # s = 1 - t
    # AB = (A[0]*s + B[0]*t, A[1]*s + B[1]*t)
    # BC = (B[0]*s + C[0]*t, B[1]*s + C[1]*t)
    # CD = (C[0]*s + D[0]*t, C[1]*s + D[1]*t)
    # ABC = (AB[0]*s + BC[0]*t, AB[1]*s + BC[1]*t)
    # BCD = (BC[0]*s + CD[0]*t, BC[1]*s + CD[1]*t)

    # return (ABC[0]*s + BCD[0]*t, ABC[1]*s + BCD[1]*t)

    # P = (1−t)^3*P1 + 3(1−t)^2*t*P2 +3(1−t)*t^2*P3 + t^3*P4
    x = (1-t)**3*A[0] + 3*(1-t)**2*t*B[0] + 3*(1-t)*t**2*C[0] + t**3*D[0]
    y = (1-t)**3*A[1] + 3*(1-t)**2*t*B[1] + 3*(1-t)*t**2*C[1] + t**3*D[1]
    return x, y

# def draw_bezier()

def draw_polygon():
    r, g, b = 255,30,20
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(r, g, b)
    glBegin(GL_POLYGON)
    # glVertex2d(100, 100, 0)
    # glVertex2d(200, 200, 0)
    # glVertex2d(300, 300, 0)
    glVertex3f(0.5, 1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, 1.0, 0.0)
    glEnd()


window = app.Window(width=512, height=512, color=(1, 1, 1, 1))

# A = (-0.5, 0.9)
# B = (0.3, 0.9)
# C = (0.3, 0.3)
# D = (-0.5, 0.3)

A = (0, 0)
B = (0.9, 0)
C = (0.25, 1)
D = (-0.2, 0.4)

A1 = (-0.27, 0.4)
B1 = (0.2, 1.15)
C1 = (1, 0.15)
D1 = (0.25, -0.05)

A2 = (0.25, -0.05)
B2 = (1, -0.15)
C2 = (0.2, -1.15)
D2 = (-0.27, -0.4)

A3 = (-0.2, -0.4)
B3 = (0.25, -1)
C3 = (0.9, 0)
D3 = (0, -0.10)

# print(">> ", 2**3*2)

@window.event
def on_draw(dt):
    window.clear()

    r, g, b = 255,30,20
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)
    for t in range(10):
        data = bezier(A, B, C, D, t/10)
        print(data)
        if data[0] > 1 or data[0] < -1 or data[1] > 1 or data[1] < -1:
            print("DUZIN BOBIN") 
        glVertex2f(data[0], data[1])
    
    glVertex2f(data[0] - 0.07, data[1])
    
    for t in range(1000):
        data = bezier(A1, B1, C1, D1, t/1000)
        # print(data)
        if data[0] > 1 or data[0] < -1 or data[1] > 1 or data[1] < -1:
            print("DUZIN BOBIN") 
        glVertex2f(data[0], data[1])
    
    A2 = (data[0], data[1])
    # B2 = (1.0, -0.5)
    # C2 = (0.15, -1.13)
    # D2 = (-0.27, -0.45)

    for t in range(1000):
        data = bezier(A2, B2, C2, D2, t/1000)
        # print(data)
        if data[0] > 1 or data[0] < -1 or data[1] > 1 or data[1] < -1:
            print("DUZIN BOBIN") 
        glVertex2f(data[0], data[1])

    glVertex2f(data[0] + 0.07, data[1])

    for t in range(1000):
        data = bezier(A3, B3, C3, D3, t/1000)
        # print(data)
        if data[0] > 1 or data[0] < -1 or data[1] > 1 or data[1] < -1:
            print("DUZIN BOBIN") 
        glVertex2f(data[0], data[1])

    glVertex2f(0, 0)
    
    # glEnd()

    # r, g, b = 255,30,20
    # glClear(GL_COLOR_BUFFER_BIT)
    # glColor3ub(r, g, b)
    # glBegin(GL_LINE_STRIP)
    # for t in range(100):
    #     data = bezier(A1, B1, C1, D1, t/100)
    #     glVertex2f(data[0], data[1])
    glEnd()
    # draw_polygon()
   
# P = np.zeros((1+64,2), dtype=np.float32)
# T = np.linspace(0,2*np.pi, len(P)-1, endpoint = True)
# P[1:,0], P[1:,1] = 0.95*np.cos(T), 0.95*np.sin(T)
# polygon = gloo.Program(vertex, fragment, count=len(P))
# polygon["position"] = P
# polygon["center"] = 0.10, 0.10
# polygon["color1"] = 1,1,1
# polygon["color2"] = 0.62,0.65,0.65
app.run()