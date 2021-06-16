from math import atan2, cos, pi, radians, sqrt, sin
from fractions import Fraction
import turtle
from time import sleep


""" 
    Entrada:
        T - número de instâncias
        a - ângulo (0<=a<=365) (int)
        i - 0<=i<=10 - distância (racional)
        n - 0<=n<=10**9 (int)

    Saída:
        (x, y) - coordenada final em metros (floats)
"""

T = 4
Entrada = (90, 10, 1), (90, 10, 2), (90, 10, 3), (30, 1.5, 121)
Saída = (10.00, 0.00), (10.00, 10.00), (0.00, 10.00), (1.50, 0.00)


def para_cartesiano(r, a):
    x = r * cos(a)
    y = r * sin(a)
    return x, y


def para_polar(x, y):
    r = sqrt(x**2 + y**2)
    a = atan2(y, x)
    return r, a


def obtem_coordenadas(a: int, i: Fraction, n: int) -> tuple[float, float]:
    r = 0
    x = 0
    y = 0
    a_ = 0

    for _ in range(n):
        a_ += a/180
        x, y = para_cartesiano(r, a_)
        x += i
        r, a_ = para_polar(x, y)

    print(x, y)
    return x, y

obtem_coordenadas(*Entrada[2])

# def plano_cartesiano(escala=1):
#     minha_pen = turtle.Turtle()
#     minha_pen.shape("arrow")
#     minha_pen.shapesize(0.5)
#     minha_pen.color("red")

#     minha_pen.penup()
#     minha_pen.goto(0,-10 * escala)
#     minha_pen.pendown()
#     minha_pen.goto(0,10 * escala)

#     minha_pen.penup()
#     minha_pen.goto(-10 * escala,0)
#     minha_pen.pendown()
#     minha_pen.goto(10 * escala,0)


# def move(a: int, i: Fraction, n: int, escala=1, delay=0):
#     minha_pen = turtle.Turtle()
#     minha_pen.pen(pencolor='black')
#     minha_pen.color('green')
#     minha_pen.shape('arrow')
#     minha_pen.shapesize(0.5)
#     minha_pen.home()

#     for _ in range(n):
#         minha_pen.left(a)
#         minha_pen.forward(i*escala)
    
#     x, y = list(minha_pen.position())
#     x /= escala
#     y /= escala
#     print('x: ', Fraction(round(x, 2)))
#     print('y: ', Fraction(round(y, 2)))


# def desenha(a: int, i: Fraction, n: int, escala=1, delay=0):
#     move(a, i, n, escala, delay)


# escala = 50
# delay = 0

# turtle.delay(delay)
# plano_cartesiano(escala)
# desenha(*Entrada[3], escala, delay)

# # obtem_coordenadas(*Entrada[0])
# # obtem_coordenadas(*Entrada[1])
# # obtem_coordenadas(*Entrada[2])
