import math, random

pi = math.acos(-1)

def gc():
    return random.randint(0, 255)

def get_color():
    return (gc(), gc(), gc())

def get_speed():
    speed = random.uniform(1, 4)
    return int(10*speed) / 10.0

def norm(x):
    return math.sqrt(x[0]*x[0] + x[1]*x[1])

def dot(x, y):
    return x[0]*y[0] + x[1]*y[1]

def get_angle(A_x, A_y, B_x, B_y):
    A = (B_x - A_x, B_y - A_y)
    B = (B_x - A_x, 0)
    assert A_x != B_x
    return math.acos(dot(A, B)/(norm(A)*norm(B)))*90