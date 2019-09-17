import sys
import math
import struct

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


P = np.zeros((1+100, 2), dtype=np.float32)
T = np.linspace(0, 2*np.pi, len(P)-1, endpoint=True)
P[1:, 0], P[1:, 1] = 0.5*np.cos(T) - 0.1, 0.95*np.sin(T) + 0.5
polygon = gloo.Program(vertex, fragment, count=len(P))
polygon["position"] = P
polygon["center"] = -0.1, 0.5
polygon["color1"] = 1, 1, 1
polygon["color2"] = 0.62, 0.65, 0.65


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glShadeModel(GL_SMOOTH)


def first_X():
    r, g, b = 151, 200, 62
    glBegin(GL_POLYGON)
    glColor3ub(r, g, b)
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
    r, g, b = 151, 200, 62
    glBegin(GL_POLYGON)
    glColor3ub(r, g, b)
    glVertex2f(338.0 + translate, 743.0)
    glVertex2f(390.0 + translate, 669.0)
    glVertex2f(368.0 + translate, 669.0)
    glVertex2f(326.0 + translate, 729.0)
    glVertex2f(284.0 + translate, 669.0)
    glVertex2f(262.0 + translate, 669.0)
    glVertex2f(315.0 + translate, 743.0)
    glVertex2f(262.0 + translate, 819.0)
    glVertex2f(284.0 + translate, 819.0)
    glVertex2f(326.0 + translate, 757.0)
    glVertex2f(368.0 + translate, 819.0)
    glVertex2f(390.0 + translate, 819.0)
    glEnd()


def begin_B():
    r, g, b = 151, 200, 62
    glBegin(GL_POLYGON)
    glColor3ub(r, g, b)
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
    r, g, b = 161, 160, 166
    glBegin(GL_POLYGON)
    glColor3ub(r, g, b)
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


def draw_numbers():
    points = [
        (937.86, 900-196.19),
        (937.86, 900-196.86),
        (939.75, 900-200.75),
        (952.86, 900-225.91),
        (968.82, 900-235.38),
        (1004.71, 900-235.29),
        (1012.05, 900-233.61),
        (1027.07, 900-225.04),
        (1034.12, 900-218.00),
        (1040.12, 900-205.87),
        (1040.46, 900-204.36),
        (1040.46, 900-187.40),
        (1040.07, 900-185.58),
        (1034.37, 900-174.06),
        (1025.82, 900-165.51),
        (1015.59, 900-162.27),
        (1012.36, 900-161.58)
    ]

    r, g, b = 255,30,20
    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (1012.36, 900-161.58),
        (1014.01, 900-160.94),
        (1020.83, 900-160.94),
        (1032.69, 900-153.89),
        (1044.28, 900-141.23),
        (1046.41, 900-135.21),
        (1046.41, 900-115.39),
        (1046.16, 900-113.71),
        (1037.22, 900-94.80),
        (1025.56, 900-86.12),
        (998.89, 900-79.13),
        (981.40, 900-79.26),
        (955.37, 900-86.12),
        (944.62, 900-94.54),
        (935.69, 900-112.80),
        (933.74, 900-117.22),
        (933.23, 900-119.68),
        (932.61, 900-122.93)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (932.61, 900-122.93),
        (941.24, 900-122.93),
        (949.86, 900-122.93)
    ]

    for point in points:
        glVertex2f(point[0], point[1])


    points = [
        (949.86, 900-122.93),
        (956.54, 900-109.17),
        (963.66, 900-101.79),
        (974.93, 900-96.61),
        (977.26, 900-96.35),
        (1003.16, 900-96.22),
        (1004.97, 900-96.61),
        (1012.87, 900-100.24),
        (1016.89, 900-103.22),
        (1030.74, 900-118.76),
        (1028.67, 900-136.63),
        (1006.91, 900-150.75),
        (1001.22, 900-152.17),
        (968.86, 900-153.17)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])

    
    points = [
        (968.86, 900-153.17),
        (968.86, 900-160.40),
        (968.86, 900-167.63)
    ]

    for point in points:
        glVertex2f(point[0], point[1])


    points = [
        (968.86, 900-167.63),
        (991.37, 900-168.62),
        (999.66, 900-169.52),
        (1014.43, 900-173.80),
        (1021.03, 900-182.47),
        (1021.03, 900-204.75),
        (1015.85, 900-212.13),
        (1001.22, 900-219.13),
        (998.89, 900-219.38),
        (980.37, 900-219.38),
        (978.81, 900-219.13),
        (967.29, 900-213.43),
        (960.81, 900-206.95),
        (955.46, 900-195.93)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (955.46, 900-195.93),
        (941.90, 900-195.81),
        (937.86, 900-196.53)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    glEnd()


def bezier_curve(points):
    data = []
    n = len(points)

    for u in range(100):
        x = get_function(points, u/100, n-1, 0, 'x')
        y = get_function(points, u/100, n-1, 0, 'y')
        data.append((x, y))

    return np.reshape(data, (len(data), 2))


def get_function(points, u, n, i, param):
    if i > n:
        return 0
    else: 
        if param == 'x':
            return get_basis(u, n, i)*points[i][0] + get_function(points, u, n, i+1, param)
        elif param == 'y':
            return get_basis(u, n, i)*points[i][1] + get_function(points, u, n, i+1, param)


def get_basis(u, n, i):
    return binomial(n, i)*(u**i)*(1-u)**(n-i)


def binomial(n, i):
    return math.factorial(n)/(math.factorial(i)*math.factorial(n-i))


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    first_X()
    second_X(374.0)
    begin_B()
    draw_numbers()
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
        gluOrtho2D(0.0, 1600.0, 900.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    if key == chr(27):
        sys.exit(0)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1600, 900)
glutInitWindowPosition(0, 0)
glutCreateWindow(b'xboxzin')
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutMainLoop()
