import numpy as np
import math

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from glumpy import app, gl, gloo

# points = [
#     (1, -1),
#     (-2, 2),
#     (1, 5),
#     (4, 2),
#     (7, 5)
# ]

def bezier_curve(points):
    data = []
    n = len(points)
    
    for u in range(10):
        # print("> " + str(u))
        x = get_function(points, u/10, n-1, 0, 'x')
        y = get_function(points, u/10, n-1, 0, 'y')
        print("> ", (x, y))
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
    # print("BINOMIAL: ", binomial(n, i)*(u**i)*(1-u)**(n-i))
    return binomial(n, i)*(u**i)*(1-u)**(n-i)


def binomial(n, i):
    # print("BINOMIAL ", math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))
    return math.factorial(n)/(math.factorial(i)*math.factorial(n-i))


def bezier(A, B, C, D, t):
    x = (1-t)**3*A[0] + 3*(1-t)**2*t*B[0] + 3*(1-t)*t**2*C[0] + t**3*D[0]
    y = (1-t)**3*A[1] + 3*(1-t)**2*t*B[1] + 3*(1-t)*t**2*C[1] + t**3*D[1]

    return x, y

A = (1, -1)
B = (-2, 2)
C = (1, 5)
D = (4, 2)

points = [
    (1, -1),
    (-2, 2),
    (1, 5),
    (4, 2)
]
arr = np.array(points)

bezier_curve(points)

# for t in range(10):
#     data = bezier(A, B, C, D, t/10)
#     print("> ", data)

# print(arr)
# print(bezier_curve(arr))