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


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def fx(self, x):
        return self.a*x + self.b


def getEquation(p1, p2):
    a = (p2['y'] - p1['y'])/(p2['x'] - p1['x'])
    b = p1['y'] - a*p1['x']

    return Equation(a, b)


def circle():
    points = []

    cx = 798
    cy = 335
    radius = 285
    
    previous = (cx+radius, cy)

    for angle in np.arange(0, 360, 0.1):
        x = cx + radius*math.cos(math.radians(angle))
        y = cy + radius*math.sin(math.radians(angle))

        points.append((x, y))

    return points


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


P = np.zeros((1+100, 2), dtype=np.float32)
T = np.linspace(0, 2*np.pi, len(P)-1, endpoint=True)
P[1:, 0], P[1:, 1] = 0.5*np.cos(T) - 0.1, 0.95*np.sin(T) + 0.5
polygon = gloo.Program(vertex, fragment, count=301)
# polygon["position"] = P
polygon["center"] = -0.1, 0.5
polygon["color1"] = 1, 1, 1
polygon["color2"] = 0.62, 0.65, 0.65


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glShadeModel(GL_SMOOTH)


def draw_circle():
    r, g, b = 194, 194, 194
    # glPolygonMode(GL_BACK, GL_FILL)
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    points = circle()

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()


def draw_numbers():
    three()
    six()
    zero()


def three():
    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

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

    outside = []
    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])


    points = [
        (963.00, 900-157.469)
    ]

    for point in points:
        outside.append(point)
        glVertex2f(point[0], point[1])


    points = [
        (963.000, 900-164.694),
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

    inside = []

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    inside.reverse()

    points = [
        (935.96, 900-193.00),
        (932.00, 900-193.27)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        glVertex2f(point[0], point[1])

    glEnd()


    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    point1 = outside[-2]
    point2 = outside[-1]
    point3 = inside[-1]
    
    final.append(point1)
    final.append(point2)
    final.append(point3)

    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glVertex2f(963.000, 900-164.694)
    glVertex2f(963.00, 900-157.469)
    glVertex2f(1006.500, 900-158.655)

    glEnd()


    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    outside = []
    inside = []

    points = [
        (1006.500, 900-158.655),
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
    outside.append((1006.500, 900-158.655))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])

    points = [
        (935.376, 900-120.00),
        (944.003, 900-120.00)
    ]

    for point in points:
        glVertex2f(point[0], point[1])


    points = [
        (944.003, 900-120.000),
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
        inside.append(point)
        glVertex2f(point[0], point[1])

    points = [
        (963.00, 900-150.243),
        (963.00, 900-157.469),
        (963.00, 900-164.694)
    ]

    for point in points:
        glVertex2f(point[0], point[1])

    outside.reverse()
    
    glEnd()


    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    point1 = outside[-2]
    point2 = outside[-1]
    point3 = inside[-1]
    
    final.append(point1)
    final.append(point2)
    final.append(point3)

    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glVertex2f(963.000, 900-150.243)
    glVertex2f(963.00, 900-157.469)
    glVertex2f(1006.500, 900-158.655)

    glEnd()


def six():
    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    inside = []
    outside = []
    
    points = [
        (1170.36, 900-193.88),
        (1172.24, 900-195.95),
        (1170.57, 900-198.89),
        (1163.57, 900-212.46),
        (1159.71, 900-217.49),
        (1152.09, 900-223.98),
        (1148.82, 900-226.08),
        (1138.53, 900-230.97),
        (1136.67, 900-231.39),
        (1119.84, 900-232.14),
        (1113.15, 900-231.61),
        (1101.71, 900-228.78),
        (1096.84, 900-226.64),
        (1088.11, 900-220.63),
        (1084.25, 900-216.76),
        (1078.42, 900-208.72),
        (1076.24, 900-205.04),
        (1071.86, 900-196.14),
        (1069.90, 900-191.24),
        (1066.70, 900-180.97),
        (1065.46, 900-175.60),
        (1063.96, 900-165.41),
        (1063.55, 900-160.63),
        (1063.31, 900-150.89),
        (1063.47, 900-145.92),
        (1064.31, 900-136.22)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])


    points = [
        (1080.83, 900-150.00),
        (1080.57, 900-150.00),
        (1080.81, 900-155.06),
        (1081.56, 900-166.14),
        (1082.13, 900-170.73),
        (1083.84, 900-180.09),
        (1085.08, 900-184.72),
        (1088.79, 900-194.81),
        (1091.55, 900-199.83),
        (1098.38, 900-208.18),
        (1102.49, 900-211.41),
        (1112.77, 900-216.16),
        (1114.61, 900-216.50),
        (1130.81, 900-216.48),
        (1133.43, 900-216.06),
        (1143.72, 900-211.43),
        (1150.02, 900-205.08),
        (1155.398, 900-194.000),
        (1155.398, 900-194.000)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])


    glEnd()


    inside.reverse()
    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)


    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()

    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    inside = []
    outside = []

    points = [
        (1063.55, 900-160.63),
        (1063.31, 900-150.89),
        (1063.47, 900-145.92),
        (1064.31, 900-136.22),
        (1067.08, 900-120.90),
        (1069.06, 900-114.73),
        (1074.74, 900-102.75),
        (1078.69, 900-97.17),
        (1086.83, 900-88.99),
        (1090.75, 900-86.07),
        (1099.85, 900-80.93),
        (1105.13, 900-78.93),
        (1114.54, 900-77.39),
        (1118.87, 900-77.06),
        (1128.23, 900-77.25),
        (1133.14, 900-78.02),
        (1141.46, 900-80.61),
        (1144.98, 900-82.19),
        (1151.61, 900-86.17),
        (1154.72, 900-88.55),
        (1161.04, 900-94.50),
        (1163.86, 900-97.82),
        (1169.01, 900-105.63),
        (1171.07, 900-110.23),
        (1173.46, 900-119.36),
        (1174.00, 900-123.79),
        (1174.00, 900-133.28),
        (1173.46, 900-137.73),
        (1171.20, 900-146.30),
        (1169.41, 900-150.40),
        (1164.90, 900-157.54),
        (1162.38, 900-160.64),
        (1155.50, 900-167.50),
        (1151.53, 900-170.46),
        (1142.79, 900-174.91),
        (1137.99, 900-176.32),
        (1127.44, 900-177.64),
        (1122.32, 900-177.52),
        (1113.86, 900-176.09),
        (1110.44, 900-175.14),
        (1102.23, 900-171.91),
        (1097.67, 900-169.20),
        (1090.05, 900-162,82),
        (1086.90, 900-159.27),
        (1082.46, 900-152.36),
        (1080.83, 900-150.00),
        (1080.57, 900-150.00)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])

    
    points = [
        (1085.96, 900-136.48),
        (1089.31, 900-143.74),
        (1092.11, 900-147.47),
        (1098.94, 900-154.30),
        (1103.00, 900-157.34),
        (1112.70, 900-162.04),
        (1114.53, 900-162.43),
        (1129.14, 900-162.50),
        (1131.40, 900-162.08),
        (1144.03, 900-156.15),
        (1149.45, 900-150.87),
        (1156.20, 900-137.17),
        (1156.50, 900-135.68),
        (1156.50, 900-119.84),
        (1156.11, 900-117.66),
        (1152.05, 900-109.00),
        (1149.30, 900-105.30),
        (1143.07, 900-99.25),
        (1139.66, 900-96.82),
        (1133.12, 900-93.82),
        (1128.42, 900-92.82),
        (1119.11, 900-91.96),
        (1114.49, 900-92.09),
        (1106.29, 900-94.38),
        (1101.56, 900-96.87),
        (1093.81, 900-103.36),
        (1090.70, 900-107.24),
        (1085.54, 900-116.84),
        (1085.51, 900-118.52),
        (1085.51, 900-133.64),
        (1085.96, 900-136.48),
        (1089.31, 900-143.74)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    inside.reverse()
    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)


    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()


def zero():
    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    inside = []
    outside = []

    points = [
        (1236.01, 900-232.35),
        (1260.56, 900-232.50),
        (1266.32, 900-231.11),
        (1281.18, 900-222.75),
        (1286.22, 900-217.90),
        (1295.32, 900-205.07),
        (1299.21, 900-196.81),
        (1304.62, 900-179.08),
        (1306.27, 900-169.72),
        (1307.16, 900-152.20),
        (1306.77, 900-144.11),
        (1303.84, 900-126.05),
        (1301.08, 900-117.09),
        (1293.82, 900-102.45),
        (1289.61, 900-96.50),
        (1276.89, 900-83.66),
        (1272.16, 900-80.79),
        (1256.43, 900-76.70),
        (1241.30, 900-76.67),
        (1227.08, 900-80.67),
        (1220.00, 900-84.82),
        (1209.26, 900-95.21),
        (1205.20, 900-100.72),
        (1198.49, 900-113.43),
        (1195.81, 900-120.57),
        (1191.93, 900-136.18),
        (1191.60, 900-140.14),
        (1191.66, 900-171.77),
        (1191.92, 900-174.46),
        (1197.51, 900-195.32),
        (1201.50, 900-204.16),
        (1212.16, 900-218.98),
        (1213.16, 900-219.95),
        (1228.05, 900-230.20)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()

    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    points = [
        (1241.20, 900-217.18),
        (1258.17, 900-216.50),
        (1260.22, 900-216.06),
        (1268.64, 900-211.13),
        (1272.37, 900-207.45),
        (1278.74, 900-197.25),
        (1281.37, 900-190.68),
        (1286.13, 900-173.25),
        (1286.32, 900-171.00),
        (1286.35, 900-136.03),
        (1286.07, 900-132.46),
        (1281.93, 900-117.27),
        (1279.23, 900-110.82),
        (1272.72, 900-101.16),
        (1268.97, 900-97.82),
        (1258.13, 900-92.51),
        (1247.41, 900-91.34),
        (1232.98, 900-94.98),
        (1226.78, 900-99.49),
        (1218.58, 900-111.84),
        (1215.87, 900-118.21),
        (1211.99, 900-132.36),
        (1211.66, 900-136.60),
        (1211.54, 900-165.24),
        (1211.80, 900-172.89),
        (1213.68, 900-185.90),
        (1215.42, 900-191.02),
        (1222.40, 900-205.98),
        (1227.52, 900-211.43),
        (1239.61, 900-216.96),
        (1241.20, 900-217.18),
        (1258.17, 900-216.50)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    point1 = inside[-1]
    point1 = inside[0]
    point1 = outside[0]

    final.append(point1)
    final.append(point2)
    final.append(point3)

    r, g, b = 194, 194, 194
    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()


def draw_B():
    r, g, b = 151, 200, 62
    glColor3ub(r, g, b)

    glBegin(GL_POLYGON)

    points = [
        (418.500, 900-231.500),
        (438.000, 900-231.412),
        (438.000, 900-214,164),
        (438.000, 900-192.499),
        (438.000, 900-170.834),
        (417.971, 900-171.070),
        (418.235, 900-201.285),
    ]

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()


    glBegin(GL_POLYGON)

    points = [
        (392.910, 900-162.250),
        (397.789, 900-170.500),
        (407.880, 900-170.785),
        (417.971, 900-171.070),
        (438.000, 900-170.834),
        (438.000, 900-162.250)
    ]

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()


    ####################### B superior externo ############################

    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    outside = []

    points = [
        (438.000, 900-231.412),
        (461.63, 900-231.30),
        (471.86, 900-231.09),
        (484.38, 900-230.61),
        (488.11, 900-230.37),
        (492.80, 900-229.52),
        (498.86, 900-227.34),
        (505.75, 900-223.86),
        (508.12, 900-222.38),
        (512.97, 900-218.45),
        (515.08, 900-215.85),
        (518.62, 900-208.56),
        (519.48, 900-203.46),
        (519.39, 900-191.88),
        (518.27, 900-187.10),
        (514.45, 900-179.31),
        (512.10, 900-176.15),
        (507.35, 900-171.70),
        (505.34, 900-170.16),
        (499.755, 900-166.686)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])


    outside.append((438.000, 900-162.250))

    glEnd()


    ####################### B superior interno ############################


    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    inside = []
    
    points = [
        (438.000, 900-214.164),
        (479.88, 900-213.51),
        (484.14, 900-213.17),
        (493.72, 900-208.91),
        (496.79, 900-205.38),
        (499.05, 900-194.43),
        (498.14, 900-185.97),
        (494.70, 900-179.63),
        (489.94, 900-175.46),
        (482.95, 900-171.75),
        (479.61, 900-171.46),
        (438.000, 900-170.834),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    inside.append(points[-1])
    glVertex2f(438.000, 900-170.834)

    glEnd()


    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()


    ####################### B inferior externo ############################

    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    outside = []

    points = [
        # (438.500, 900-166.686),
        # (451.000, 900-166.686),
        # (478.030, 900-166.686),
        (499.755, 900-166.686),
        (509.35, 900-163.21),
        (512.22, 900-161.92),
        (517.87, 900-158.45),
        (520.49, 900-156.14),
        (525.94, 900-150.07),
        (527.85, 900-147.27),
        (531.33, 900-139.48),
        (532.20, 900-134.11),
        (532.27, 900-122.46),
        (531.84, 900-118.30),
        (529.81, 900-109.65),
        (527.96, 900-105.34),
        (522.69, 900-97.52),
        (519.21, 900-94.04),
        (510.84, 900-88.16),
        (507.27, 900-86.03),
        (498.94, 900-82.85),
        (494.17, 900-81.82),
        (482.91, 900-80.66),
        (477.18, 900-80.38),
        (464.52, 900-80.09),
        (458.17, 900-80.04),
        (450.750, 900-80.035),
        (438.438, 900-80.022)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    ####################### B inferior interno ############################

    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    inside = []

    points = [
        (438.500, 900-153.500),
        (451.000, 900-153.792),
        (457.88, 900-153.95),
        (470.04, 900-153.66),
        (489.77, 900-152.39),
        (493.50, 900-151.77),
        (501.81, 900-147.87),
        (505.02, 900-145.45),
        (510.15, 900-138.31),
        (511.39, 900-133.07),
        (511.39, 900-121.10),
        (510.69, 900-117.14),
        (507.84, 900-110.84),
        (505.93, 900-108.35),
        (500.21, 900-103.31),
        (494.95, 900-101.46),
        (489.38, 900-99.20),
        (485.63, 900-98.52),
        (474.98, 900-97.30),
        (465.59, 900-96.97),
        (447.32, 900-96.97),
        (438.77, 900-97.42),
        (438.19, 900-98.96)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()
    

    outside.reverse()
    inside.reverse()
    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    point1 = inside[-1]
    point2 = (438.000, 900-166.686)
    point3 = outside[-1]

    final.append(point1)
    final.append(point2)
    final.append(point3)

    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()


    ####################### B quadrado inferior esquerdo ############################

    glBegin(GL_POLYGON)

    points = [
        (418.000, 900-98.265),
        (438.452, 900-98.265),
        (438.438, 900-80.022),
        (418.000, 900-80.000),
    ]

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()


    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    glVertex2f(438.452, 900-98.265)
    glVertex2f(outside[1][0], outside[1][1])
    glVertex2f(438.438, 900-80.022)

    glEnd()


    ####################### B reta inferior externa ############################

    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    outside = []

    points = [
        (418.000, 900-98.265),
        (418.000, 900-117.000),
        (418.000, 900-154.000),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    ####################### B reta inferior interna ############################

    glColor3ub(r, g, b)
    glBegin(GL_LINE_STRIP)

    inside = []

    points = [
        (438.78, 900-97.42),
        (438.19, 900-98.96),
        (438.09, 900-111.67),
        (438.233, 900-126.515),
        (438.500, 900-153.500),
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()


    glBegin(GL_POLYGON)

    points = [
        (392.910, 900-162.250),
        (388.030, 900-154.000),
        (403.015, 900-154.000),
        (418.000, 900-154.000),
        (438.500, 900-154.000),
        (438.500, 900-162.250),
    ]

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()


    glBegin(GL_POLYGON)

    points = [
        (417.971, 900-171.070),
        (438.000, 900-170.834),
        inside[-1],
        outside[-1]
    ]

    for point in points:
        glVertex2f(point[0], point[1])

    glEnd()

    
def draw_O():
    ####################### O externo ############################

    r, g, b = 151, 200, 62
    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    outside = []

    points = [
        (616.73, 900-231.59),
        (635.53, 900-230.37),
        (646.40, 900-228.12),
        (661.11, 900-221.62),
        (667.86, 900-217.34),
        (680.68, 900-206.78),
        (686.51, 900-200.31),
        (694.33, 900-187.02),
        (697.23, 900-178.59),
        (700.48, 900-160.04),
        (700.53, 900-149.84),
        (696.43, 900-130.03),
        (691.84, 900-119.82),
        (680.27, 900-103.47),
        (673.83, 900-96.93),
        (658.94, 900-86.09),
        (650.40, 900-81.93),
        (633.77, 900-77.63),
        (613.00, 900-77.34),
        (599.57, 900-80.68),
        (584.77, 900-86.34),
        (568.91, 900-97.64),
        (562.59, 900-103.83),
        (553.11, 900-117.65),
        (549.71, 900-124.57),
        (545.59, 900-139.27),
        (544.67, 900-146.95),
        (544.59, 900-171.13),
        (546.36, 900-179.48),
        (556.94, 900-198.47),
        (563.62, 900-206.33),
        (580.71, 900-220.75),
        (591.61, 900-226.71),
        (608.66, 900-231.14)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        outside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    ####################### O interno ############################


    glColor3ub(r, g, b)
    glBegin(GL_LINE_LOOP)

    inside = []
    
    points = [
        (615.31, 900-213.10),
        (633.91, 900-212.45),
        (643.13, 900-209.69),
        (661.86, 900-198.43),
        (670.60, 900-188.43),
        (678.17, 900-169.11),
        (678.41, 900-167.30),
        (678.48, 900-143.41),
        (678.15, 900-140.54),
        (672.96, 900-125.46),
        (667.06, 900-117.07),
        (653.51, 900-105.45),
        (646.71, 900-101.46),
        (631.70, 900-96.07),
        (615.66, 900-95.40),
        (600.02, 900-99.80),
        (592.65, 900-103.95),
        (580.64, 900-115.02),
        (575.82, 900-121.64),
        (567.35, 900-139.21),
        (565.99, 900-145.39),
        (566.05, 900-167.33),
        (567.14, 900-172.40),
        (575.42, 900-189.84),
        (587.98, 900-202.45),
        (605.96, 900-211.21)
    ]

    data = bezier_curve(np.array(points))
    for point in data:
        inside.append(point)
        glVertex2f(point[0], point[1])

    glEnd()


    outside.append((616.73, 900-231.59))
    outside.append((635.53, 900-230.37))
    inside.append((615.31, 900-213.10))
    inside.append((633.91, 900-212.45))

    final = []

    for i in range(len(inside)-1):
        point1 = outside[i]
        point2 = inside[i]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

        point1 = outside[i]
        point2 = outside[i+1]
        point3 = inside[i+1]

        final.append(point1)
        final.append(point2)
        final.append(point3)

    glColor3ub(r, g, b)
    glBegin(GL_TRIANGLE_STRIP)

    for point in final:
        glVertex2f(point[0], point[1])

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle()
    draw_numbers()
    draw_B()
    draw_O()
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
