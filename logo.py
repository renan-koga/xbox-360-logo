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


P = np.zeros((1+100, 2), dtype=np.float32)
T = np.linspace(0, 2*np.pi, len(P)-1, endpoint=True)
P[1:, 0], P[1:, 1] = 0.5*np.cos(T) - 0.1, 0.95*np.sin(T) + 0.5
polygon = gloo.Program(vertex, fragment, count=len(P))
polygon["position"] = P
polygon["center"] = -0.1, 0.5
polygon["color1"] = 1, 1, 1
polygon["color2"] = 0.62, 0.65, 0.65

angle = 0
positivo = True
rotate = False
zoom = 1

def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glShadeModel(GL_SMOOTH)

def draw():
    global rotate
    global positivo 
    global angle
    global zoom

    pivot_x, pivot_y = 750.0, 750.0
    
    glPushMatrix()

    glTranslatef(pivot_x, pivot_y, 0)
    
    glScalef(zoom, zoom, zoom)

    glRotatef(angle, 0, 0, 1)
    
    if rotate:
        if positivo:
            angle -= 5
        else:
            angle += 5
    
    glTranslatef(-pivot_x, -pivot_y, 0)
    
    #glBegin(GL_TRIANGLE_FAN)
    polygon.draw(GL_TRIANGLE_FAN)
    #glEnd()

    #######################  FIRST X ###########################
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

    ####################### SECOND X ############################
    translate = 374.0
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

#     ################ B ###################
#     r, g, b = 151, 200, 62
#     glBegin(GL_POLYGON)
#     glColor3ub(r, g, b)
#     glVertex2f(419.0, 746.0)
#     glVertex2f(419.0, 819.0)
#     glVertex2f(437.0, 819.0)
#     glVertex2f(437.0, 669.0)
#     glVertex2f(419.0, 669.0)
#     glVertex2f(419.0, 730.0)
#     glVertex2f(398.0, 730.0)
#     glVertex2f(389.0, 746.0)
#     glEnd()

#     ################### TRADEMARK #######################
#     r, g, b = 161, 160, 166
#     glBegin(GL_POLYGON)
#     glColor3ub(r, g, b)
#     glVertex2f(1299.0, 805.0)
#     glVertex2f(1299.0, 808.0)
#     glVertex2f(1311.0, 808.0)
#     glVertex2f(1311.0, 805.0)
#     glEnd()
#     glBegin(GL_POLYGON)
#     glVertex2f(1307.0, 808.0)
#     glVertex2f(1307.0, 819.0)
#     glVertex2f(1304.0, 819.0)
#     glVertex2f(1304.0, 808.0)
#     glEnd()



# # ################### THREE #################
# #     r, g, b = 151, 200, 62
    
# #     # glPolygonMode(GL_BACK, GL_FILL)
    
# #     glColor3ub(r, g, b)
# #     glBegin(GL_LINE_LOOP)
    
# #     points = [
# #         (963.000, 900-164.694),
# #         (985.43, 900-165.64),
# #         (993.67, 900-166.56),
# #         (1001.11, 900-168.82),
# #         (1004.86, 900-170.90),
# #         (1012.49, 900-178.06),
# #         (1015.00, 900-184.15),
# #         (1015.00, 900-197.41),
# #         (1013.38, 900-202.36),
# #         (1007.54, 900-209.53),
# #         (1004.02, 900-212.12),
# #         (995.29, 900-216.14),
# #         (993.84, 900-216.50),
# #         (974.55, 900-216.50),
# #         (972.93, 900-216.22),
# #         (961.40, 900-210.55),
# #         (954.99, 900-204.08),
# #         (949.601, 900-193.000),
# #     ]

# #     data = bezier_curve(np.array(points))
# #     for point in data:
# #         glVertex2f(point[0], point[1])

# #     points = [
# #         (932.00, 900-193.27),
# #         (932.00, 900-193.93),
# #         (933.88, 900-197.82),
# #         (938.73, 900-207.13),
# #         (941.55, 900-211.39),
# #         (949.27, 900-220.40),
# #         (954.52, 900-224.45),
# #         (964.54, 900-228.90),
# #         (968.73, 900-230.14),
# #         (979.30, 900-232.25),
# #         (985.76, 900-232.68),
# #         (1000.15, 900-231.66),
# #         (1007.93, 900-229.59),
# #         (1021.12, 900-222.20),
# #         (1028.21, 900-214.79),
# #         (1034.19, 900-203.10),
# #         (1034.50, 900-201.45),
# #         (1034.50, 900-184.62),
# #         (1034.17, 900-182.83),
# #         (1029.93, 900-174.17),
# #         (1026.55, 900-170.04),
# #         (1019.94, 900-163.95),
# #         (1018.84, 900-163.69),
# #         (1014.59, 900-161.45),
# #         (1012.61, 900-160.63),
# #         (1006.500, 900-158.655)
# #     ]

# #     data = bezier_curve(np.array(points))
# #     for point in data:
# #         glVertex2f(point[0], point[1])

# #     # points = [
# #     #     (1006.500, 900-158.655),
# #     #     (1016.20, 900-156.16),
# #     #     (1034.74, 900-142.17),
# #     #     (1039.20, 900-133.11),
# #     #     (1040.50, 900-126.28),
# #     #     (1040.48, 900-112.43),
# #     #     (1040.14, 900-110.78),
# #     #     (1034.07, 900-97.86),
# #     #     (1029.34, 900-92.27),
# #     #     (1017.70, 900-83.93),
# #     #     (1011.09, 900-80.94),
# #     #     (997.94, 900-77.57),
# #     #     (990.43, 900-76.91),
# #     #     (976.49, 900-77.08),
# #     #     (970.05, 900-77.75),
# #     #     (957.18, 900-81.13),
# #     #     (950.45, 900-84.38),
# #     #     (939.54, 900-93.24),
# #     #     (935.27, 900-98.74),
# #     #     (929.77, 900-109.90),
# #     #     (927.71, 900-114.96),
# #     #     (926.750, 900-120.000)
# #     # ]

# #     # data = bezier_curve(np.array(points))
# #     # for point in data:
# #     #     glVertex2f(point[0], point[1])


# #     # points = [
# #     #     (926.75, 900-120.00),
# #     #     (935.376, 900-120.00),
# #     #     (944.003, 900-120.00)
# #     # ]

# #     # for point in points:
# #     #     glVertex2f(point[0], point[1])

# #     # points = [
# #     #     (944.003, 900-120.000),
# #     #     (950.51, 900-106.23),
# #     #     (957.73, 900-98,93),
# #     #     (968.95, 900-93.76),
# #     #     (971.21, 900-93.50),
# #     #     (997.12, 900-93.51),
# #     #     (999.01, 900-93.74),
# #     #     (1006.96, 900-97.33),
# #     #     (1010.84, 900-100.25),
# #     #     (1016.65, 900-106.71),
# #     #     (1018.74, 900-110.57),
# #     #     (1021.61, 900-120.92),
# #     #     (1020.79, 900-127.58),
# #     #     (1015.50, 900-136.92),
# #     #     (1012.53, 900-140.15),
# #     #     (1000.97, 900-147.87),
# #     #     (995.29, 900-149.18),
# #     #     (963.000, 900-150.243),
# #     # ]

# #     # data = bezier_curve(np.array(points))
# #     # for point in data:
# #     #     glVertex2f(point[0], point[1])


# #     # points = [
# #     #     (963.00, 900-150.243),
# #     #     (963.00, 900-157.469),
# #     #     (963.00, 900-164.694)
# #     # ]

# #     # for point in points:
# #     #     glVertex2f(point[0], point[1])

# #     # points = [
# #     #     (949.601, 900-193.00),
# #     #     (935.96, 900-193.00),
# #     #     (932.00, 900-193.27),
# #     #     (932.00, 900-193.93)
# #     # ]

# #     # data = bezier_curve(np.array(points))
# #     # for point in data:
# #     #     glVertex2f(point[0], point[1])

# #     glEnd()


# ########################## SIX ###########################
#     r, g, b = 255,30,20
#     glColor3ub(r, g, b)
#     glBegin(GL_LINE_LOOP)
   
#     points = [
#         (1170.36, 900-193.88),
#         (1172.24, 900-195.95),
#         (1170.57, 900-198.89),
#         (1163.57, 900-212.46),
#         (1159.71, 900-217.49),
#         (1152.09, 900-223.98),
#         (1148.82, 900-226.08),
#         (1138.53, 900-230.97),
#         (1136.67, 900-231.39),
#         (1119.84, 900-232.14),
#         (1113.15, 900-231.61),
#         (1101.71, 900-228.78),
#         (1096.84, 900-226.64),
#         (1088.11, 900-220.63),
#         (1084.25, 900-216.76),
#         (1078.42, 900-208.72),
#         (1076.24, 900-205.04),
#         (1071.86, 900-196.14),
#         (1069.90, 900-191.24),
#         (1066.70, 900-180.97),
#         (1065.46, 900-175.60),
#         (1063.96, 900-165.41),
#         (1063.55, 900-160.63),
#         (1063.31, 900-150.89),
#         (1063.47, 900-145.92),
#         (1064.31, 900-136.22),
#         (1064.91, 900-131.89),
#         (1067.08, 900-120.90),
#         (1069.06, 900-114.73),
#         (1074.74, 900-102.75),
#         (1078.69, 900-97.17),
#         (1086.83, 900-88.99),
#         (1090.75, 900-86.07),
#         (1099.85, 900-80.93),
#         (1105.13, 900-78.93),
#         (1114.54, 900-77.39),
#         (1118.87, 900-77.06),
#         (1128.23, 900-77.25),
#         (1133.14, 900-78.02),
#         (1141.46, 900-80.61),
#         (1144.98, 900-82.19),
#         (1151.61, 900-86.17),
#         (1154.72, 900-88.55),
#         (1161.04, 900-94.50),
#         (1163.86, 900-97.82),
#         (1169.01, 900-105.63),
#         (1171.07, 900-110.23),
#         (1173.46, 900-119.36),
#         (1174.00, 900-123.79),
#         (1174.00, 900-133.28),
#         (1173.46, 900-137.73),
#         (1171.20, 900-146.30),
#         (1169.41, 900-150.40),
#         (1164.90, 900-157.54),
#         (1162.38, 900-160.64),
#         (1155.50, 900-167.50),
#         (1151.53, 900-170.46),
#         (1142.79, 900-174.91),
#         (1137.99, 900-176.32),
#         (1127.44, 900-177.64),
#         (1122.32, 900-177.52),
#         (1113.86, 900-176.09),
#         (1110.44, 900-175.14),
#         (1102.23, 900-171.91),
#         (1097.67, 900-169.20),
#         (1090.05, 900-162,82),
#         (1086.90, 900-159.27),
#         (1082.46, 900-152.36),
#         (1080.83, 900-150.00),
#         (1080.57, 900-150.00)
#     ]

#     data = bezier_curve(np.array(points))
#     for point in data:
#         glVertex2f(point[0], point[1])

#     points = [
#         (1080.83, 900-150.00),
#         (1080.57, 900-150.00),
#         (1080.81, 900-155.06),
#         (1081.56, 900-166.14),
#         (1082.13, 900-170.73),
#         (1083.84, 900-180.09),
#         (1085.08, 900-184.72),
#         (1088.79, 900-194.81),
#         (1091.55, 900-199.83),
#         (1098.38, 900-208.18),
#         (1102.49, 900-211.41),
#         (1112.77, 900-216.16),
#         (1114.61, 900-216.50),
#         (1130.81, 900-216.48),
#         (1133.43, 900-216.06),
#         (1143.72, 900-211.43),
#         (1150.02, 900-205.08),
#         (1155.398, 900-194.000),
#         (1155.398, 900-194.000)
#     ]

#     data = bezier_curve(np.array(points))
#     for point in data:
#         glVertex2f(point[0], point[1])

    
#     points = [
#         (1155.398, 900-194.000),
#         (1155.398, 900-194.000),
#         (1167.99, 900-194.00)
#     ]

#     data = bezier_curve(np.array(points))
#     for point in data:
#         glVertex2f(point[0], point[1])

#     glEnd()


#     r, g, b = 255,30,20
#     glColor3ub(r, g, b)
#     glBegin(GL_LINE_LOOP)

#     points = [
#         (1114.53, 900-162.43),
#         (1129.14, 900-162.50),
#         (1131.40, 900-162.08),
#         (1144.03, 900-156.15),
#         (1149.45, 900-150.87),
#         (1156.20, 900-137.17),
#         (1156.50, 900-135.68),
#         (1156.50, 900-119.84),
#         (1156.11, 900-117.66),
#         (1152.05, 900-109.00),
#         (1149.30, 900-105.30),
#         (1143.07, 900-99.25),
#         (1139.66, 900-96.82),
#         (1133.12, 900-93.82),
#         (1128.42, 900-92.82),
#         (1119.11, 900-91.96),
#         (1114.49, 900-92.09),
#         (1106.29, 900-94.38),
#         (1101.56, 900-96.87),
#         (1093.81, 900-103.36),
#         (1090.70, 900-107.24),
#         (1085.54, 900-116.84),
#         (1085.51, 900-118.52),
#         (1085.51, 900-133.64),
#         (1085.96, 900-136.48),
#         (1089.31, 900-143.74),
#         (1092.11, 900-147.47),
#         (1098.94, 900-154.30),
#         (1103.00, 900-157.34),
#         (1112.70, 900-162.04)
#     ]

#     data = bezier_curve(np.array(points))
#     for point in data:
#         glVertex2f(point[0], point[1])

#     glEnd()


# ########################### ZERO ########################
#     r, g, b = 255,30,20
#     glColor3ub(r, g, b)
    
#     glBegin(GL_LINE_LOOP)

#     points = [
#         (1236.01, 900-232.35),
#         (1260.56, 900-232.50),
#         (1266.32, 900-231.11),
#         (1281.18, 900-222.75),
#         (1286.22, 900-217.90),
#         (1295.32, 900-205.07),
#         (1299.21, 900-196.81),
#         (1304.62, 900-179.08),
#         (1306.27, 900-169.72),
#         (1307.16, 900-152.20),
#         (1306.77, 900-144.11),
#         (1303.84, 900-126.05),
#         (1301.08, 900-117.09),
#         (1293.82, 900-102.45),
#         (1289.61, 900-96.50),
#         (1276.89, 900-83.66),
#         (1272.16, 900-80.79),
#         (1256.43, 900-76.70),
#         (1241.30, 900-76.67),
#         (1227.08, 900-80.67),
#         (1220.00, 900-84.82),
#         (1209.26, 900-95.21),
#         (1205.20, 900-100.72),
#         (1198.49, 900-113.43),
#         (1195.81, 900-120.57),
#         (1191.93, 900-136.18),
#         (1191.60, 900-140.14),
#         (1191.66, 900-171.77),
#         (1191.92, 900-174.46),
#         (1197.51, 900-195.32),
#         (1201.50, 900-204.16),
#         (1212.16, 900-218.98),
#         (1213.16, 900-219.95),
#         (1228.05, 900-230.20),
#     ]

#     data = bezier_curve(np.array(points))
#     for point in data:
#         glVertex2f(point[0], point[1])

#     glEnd()

#     r, g, b = 255,30,20
#     glColor3ub(r, g, b)
#     glBegin(GL_LINE_LOOP)

#     points = [
#         (1241.20, 900-217.18),
#         (1258.17, 900-216.50),
#         (1260.22, 900-216.06),
#         (1268.64, 900-211.13),
#         (1272.37, 900-207.45),
#         (1278.74, 900-197.25),
#         (1281.37, 900-190.68),
#         (1286.13, 900-173.25),
#         (1286.32, 900-171.00),
#         (1286.35, 900-136.03),
#         (1286.07, 900-132.46),
#         (1281.93, 900-117.27),
#         (1279.23, 900-110.82),
#         (1272.72, 900-101.16),
#         (1268.97, 900-97.82),
#         (1258.13, 900-92.51),
#         (1247.41, 900-91.34),
#         (1232.98, 900-94.98),
#         (1226.78, 900-99.49),
#         (1218.58, 900-111.84),
#         (1215.87, 900-118.21),
#         (1211.99, 900-132.36),
#         (1211.66, 900-136.60),
#         (1211.54, 900-165.24),
#         (1211.80, 900-172.89),
#         (1213.68, 900-185.90),
#         (1215.42, 900-191.02),
#         (1222.40, 900-205.98),
#         (1227.52, 900-211.43),
#         (1239.61, 900-216.96)
#     ]

#     data = bezier_curve(np.array(points))
#     for point in data:
#         glVertex2f(point[0], point[1])
#     glEnd()
    glPopMatrix()



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

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if(w <= h):
        gluOrtho2D(0.0, 1600.0, 0.0, 900.0 * h/w)
    else:
        gluOrtho2D(0.0, 1600.0, 900.0, 0.0)
    glMatrixMode(GL_MODELVIEW)

spin = 0.0

def spinDisplay():
   global spin
   spin = spin + 2.0
   if(spin > 360.0):
      spin = spin - 360.0
   glutPostRedisplay()

def keyboard_rotate(key, x, y):
   
    global angle
    global positivo
    global rotate
    global zoom

    if key == b"q":
        positivo = True
        rotate = True
        glutIdleFunc(spinDisplay)
    elif key == b"w":
        positivo = False
        rotate = True
        glutIdleFunc(spinDisplay)
    

def keyboard_translate(key, x, y):
    
    if key == GLUT_KEY_LEFT:
        glTranslatef(-5,0,0)
    elif key == GLUT_KEY_DOWN:
        glTranslatef(0,5,0)
    elif key == GLUT_KEY_RIGHT:
        glTranslatef(5,0,0)
    elif key == GLUT_KEY_UP:
        glTranslatef(0,-5,0)

    glutPostRedisplay()   


def mouse_reset(button,state,x,y):
    global angle
    global positivo
    global rotate
    global zoom

    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
           glLoadIdentity()
           angle = 0
           rotate = False
           zoom = 1
           glutIdleFunc(None)      
    glutPostRedisplay()   


def mouseWheel_scale(button,dir,x,y):
    global zoom

    if (dir>0):
        zoom = zoom * 2
    else:
        zoom = zoom / 2

    glutPostRedisplay()       

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw()
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1600, 900)
glutInitWindowPosition(0, 0)
glutCreateWindow(b'xboxzin')
init()
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutSpecialFunc(keyboard_translate)  
glutKeyboardFunc(keyboard_rotate)
glutMouseWheelFunc(mouseWheel_scale)
glutMouseFunc(mouse_reset)

glutMainLoop()
