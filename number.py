import sys
import math
import struct
import tripy
import triangle
import numpy as np

# from shapely.geometry import MultiPoint
# from shapely.ops import triangulate

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from glumpy import app, gl, gloo



def circle():
    points = []

    cx = 800
    cy = 335
    radius = 285
    
    previous = (cx+radius, cy)

    for angle in np.arange(0, 360, 0.1):
        x = cx + radius*math.cos(math.radians(angle))
        y = cy + radius*math.sin(math.radians(angle))

        points.append(previous)
        points.append((cx, cy))
        points.append((x, y))
        # points.append((previous, (cx, cy) ,(x, y)))

    return points


def bezier_curve(points):
    data = []
    n = len(points)

    for u in range(100):
        # print("> " + str(u))
        x = get_function(points, u/100, n-1, 0, 'x')
        y = get_function(points, u/100, n-1, 0, 'y')
        # print("> ", (x, y))
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


# def triangulate(vertices):
#     n = len(vertices)
#     segments = (np.repeat(np.arange(n+1),2)[1:-1]) % n
#     print("> ", np.array(segments))
#     T = triangle.triangulate({'vertices': vertices}, "")
#     return T['triangles']

def triangulate(P):
    n = len(P)
    S = np.repeat(np.arange(n+1),2)[1:-1]
    S[-2:] = n-1,0
    T = triangle.triangulate({'vertices': P[:,:2], 'segments': S}, "p")
    return  T["triangles"].ravel()

vertex2 = """
attribute vec2 position;
void main(void) {
    gl_Position = vec4(0.85 * position, 0.0, 1.0);
}
"""

vertex = """
attribute vec2 position;
varying vec2 v_position;
void main() {
    v_position = position;
    gl_Position = vec4(position.xy, 0.0, 1.55);
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


# triangulo = [(30, 30), (40, 40), (50, 50)]
# meuTri = gloo.Program(vertex2, fragment, count=3)
# meuTri["position"] = triangulo

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


def draw_circle():
    r, g, b = 151, 200, 62
    # glPolygonMode(GL_BACK, GL_FILL)
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_FAN)

    points = circle()

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()

def draw_middle_x():
    r, g, b = 151, 200, 62
    # glPolygonMode(GL_BACK, GL_FILL)
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    points = [
        (799.428, 900-617.615),
        (780.12, 900-593.52),
        (759.37, 900-570.47),
        (748.88, 900-558.29),
        (720.61, 900-524.82),
        (706.09, 900-508.70),
        (698.61, 900-499.75),
        (693.28, 900-492.89),
        (678.51, 900-473.04),
        (631.63, 900-404.09),
        (606.75, 900-356.50),
        (605.41, 900-353.94),
        (605.01, 900-354.13)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (608.47, 900-381.61),
        (620.95, 900-445.35),
        (639.30, 900-497.65),
        (677.07, 900-573.13),
        (686.12, 900-588.78),
        (711.91, 900-627.79),
        (729.65, 900-650.79),
        (740.95, 900-663.42),
        (743.25, 900-666.36),
        (745.88, 900-669.48),
        (747.00, 900-670.81),
        (747.00, 900-672.99)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (747.00, 900-670.81),
        (747.00, 900-672.99),
        (737.12, 900-682.54),
        (713.25, 900-706.28),
        (676.04, 900-741.18),
        (646.44, 900-766.38),
        (621.88, 900-782.53)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (619.23, 900-784.56),
        (620.24, 900-785.57),
        (647.91, 900-781.75),
        (686.77, 900-773.80),
        (707.30, 900-767.35),
        (751.03, 900-748.48),
        (764.02, 900-741.39),
        (799.428, 900-717.917),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (799.428, 900-717.917),
        (851.66, 900-755.07),
        (901.25, 900-775.13),
        (978.35, 900-786.08),
        (973.68, 900-785.67),
        (975.25, 900-784.07)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])

    
    points = [
        (970.12, 900-780.27),
        (953.95, 900-767.59),
        (910.77, 900-728.68),
        (882.40, 900-700.61),
        (871.89, 900-690.42),
        (856.72, 900-675.95),
        (852.00, 900-672.13),
        (852.00, 900-670.21)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (852.00, 900-670.677),
        (853.122, 900-669.000),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    points = [
        (853.122, 900-669.000),
        (877.14, 900-641.43),
        (898.33, 900-609.92),
        (942.06, 900-533.82),
        (968.93, 900-464.39),
        (984.46, 900-387.95),
        (988.82, 900-354.93),
        (986.84, 900-355.09),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])

    
    points = [
        (983.35, 900-361.69),
        (972.79, 900-383.72),
        (957.94, 900-408.89),
        (933.15, 900-451.56),
        (910.23, 900-484.42),
        (878.94, 900-523.13),
        (864.77, 900-538.74),
        (856.91, 900-548.44),
        (821.07, 900-590.53),
        (813.89, 900-598.48),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])


    glEnd()

def draw_numbers():
    r, g, b = 151, 200, 62
    # glPolygonMode(GL_BACK, GL_FILL)
    glColor3ub(r, g, b)
    glBegin(GL_LINES)

    vertexes = []

    points = [
        (932.00, 900-193.27),
        (932.00, 900-193.93),
        (933.88, 900-197.82),
        (938.73, 900-207.13),
        (941.55, 900-211.39),
        (949.27, 900-220.40),
        (954.52, 900-224.45),
        (964.54, 900-228.90),
        (968.73, 900-230.14),
        (979.30, 900-232.25),
        (985.76, 900-232.68),
        (1000.15, 900-231.66),
        (1007.93, 900-229.59),
        (1021.12, 900-222.20),
        (1028.21, 900-214.79),
        (1034.19, 900-203.10),
        (1034.50, 900-201.45),
        (1034.50, 900-184.62),
        (1034.17, 900-182.83),
        (1029.93, 900-174.17),
        (1026.55, 900-170.04),
        (1019.94, 900-163.95),
        (1018.84, 900-163.69),
        (1014.59, 900-161.45),
        (1012.61, 900-160.63),
        (1006.500, 900-158.655)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    points = [
        # (1006.500, 900-158.655),
        (1016.20, 900-156.16),
        (1034.74, 900-142.17),
        (1039.20, 900-133.11),
        (1040.50, 900-126.28),
        (1040.48, 900-112.43),
        (1040.14, 900-110.78),
        (1034.07, 900-97.86),
        (1029.34, 900-92.27),
        (1017.70, 900-83.93),
        (1011.09, 900-80.94),
        (997.94, 900-77.57),
        (990.43, 900-76.91),
        (976.49, 900-77.08),
        (970.05, 900-77.75),
        (957.18, 900-81.13),
        (950.45, 900-84.38),
        (939.54, 900-93.24),
        (935.27, 900-98.74),
        (929.77, 900-109.90),
        (927.71, 900-114.96),
        (926.750, 900-120.000)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    points = [
        # (926.75, 900-120.00),
        (935.376, 900-120.00),
        (944.003, 900-120.00)
    ]

    for point in points:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    points = [
        # (944.003, 900-120.000),
        (950.51, 900-106.23),
        (957.73, 900-98,93),
        (968.95, 900-93.76),
        (971.21, 900-93.50),
        (997.12, 900-93.51),
        (999.01, 900-93.74),
        (1006.96, 900-97.33),
        (1010.84, 900-100.25),
        (1016.65, 900-106.71),
        (1018.74, 900-110.57),
        (1021.61, 900-120.92),
        (1020.79, 900-127.58),
        (1015.50, 900-136.92),
        (1012.53, 900-140.15),
        (1000.97, 900-147.87),
        (995.29, 900-149.18),
        (963.000, 900-150.243),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    points = [
        # (963.00, 900-150.243),
        (963.00, 900-157.469),
        (963.00, 900-164.694)
    ]

    for point in points:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    points = [
        # (963.000, 900-164.694),
        (985.43, 900-165.64),
        (993.67, 900-166.56),
        (1001.11, 900-168.82),
        (1004.86, 900-170.90),
        (1012.49, 900-178.06),
        (1015.00, 900-184.15),
        (1015.00, 900-197.41),
        (1013.38, 900-202.36),
        (1007.54, 900-209.53),
        (1004.02, 900-212.12),
        (995.29, 900-216.14),
        (993.84, 900-216.50),
        (974.55, 900-216.50),
        (972.93, 900-216.22),
        (961.40, 900-210.55),
        (954.99, 900-204.08),
        (949.601, 900-193.000)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    points = [
        # (949.601, 900-193.00),
        (935.96, 900-193.00),
        (932.00, 900-193.27),
        # (932.00, 900-193.93)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        # glVertex2f(point[0], point[1])
        vertexes.append(point)


    glEnd()


    # points = MultiPoint(vertexes)
    # triangles = triangulate(points, edges=True)

    # print(np.array(vertexes))
    V = triangulate(np.array(vertexes))

    print(V)


    # arr = np.asarray(triangles)
    # for triangle in triangles:
    #     arr = np.append(arr, triangle.wkt)
        # print("> ", np.append(arr, triangle.wkt))

    # triangles = tripy.earclip(vertexes)

    # print(">>> ", triangles)

    r, g, b = 0,0,0
    glColor3ub(r, g, b)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    # polygon.draw(GL_TRIANGLES, V)
    # glPolygonMode(GL_BACK, GL_FILL)
    glBegin(GL_TRIANGLE_STRIP)

    for point in V:
        print("> ", point)
        # glVertex2d(point[0], point[1])

    glEnd()
    
    # r, g, b = 151, 200, 62
    # glColor3ub(r, g, b)
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # polygon.draw(GL_TRIANGLES, I)


def bezier(A, B, C, D, t):
    x = (1-t)**3*A[0] + 3*(1-t)**2*t*B[0] + 3*(1-t)*t**2*C[0] + t**3*D[0]
    y = (1-t)**3*A[1] + 3*(1-t)**2*t*B[1] + 3*(1-t)*t**2*C[1] + t**3*D[1]

    return x, y

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # polygon.draw(GL_TRIANGLE_FAN)
    # draw_circle()
    draw_numbers()  
    # draw_middle_x()
    # meuTri.draw(GL_TRIANGLE_STRIP)
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
