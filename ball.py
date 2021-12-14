import random
from utility import get_color, get_speed, norm

class Ball:
    def __init__(self, X, Y):
        self.v_x, self.v_y = 1, 1
        self.c_x = random.randint(0, X)
        self.c_y = random.randint(0, Y)
        self.color = get_color()
        self.X = X
        self.Y = Y
        self.speed = get_speed()
    
    def update_position(self):
        to_x, to_y = self.c_x + self.v_x, self.c_y + self.v_y
        if min(to_x, to_y) >= 0 and to_x < self.X and to_y < self.Y:
            self.c_x, self.c_y = to_x, to_y
    
    def update_vector(self, x, y):
        dir_x = (x - self.c_x)
        dir_y = (y - self.c_y)
        len_vector = norm((dir_x, dir_y))
        self.v_x = self.speed * dir_x / len_vector
        self.v_y = self.speed * dir_y / len_vector

    def update_revert(self):
        self.c_x -= self.v_x * 30
        self.c_x = max(0, self.c_x)
        self.c_x = min(self.X - 1, self.c_x)

        self.c_y -= self.v_y * 15
        self.c_y = max(0, self.c_y)
        self.c_y = min(self.Y - 1, self.c_y)

    def set_position(self):
        self.c_x = random.randint(0, self.X)
        self.c_y = random.randint(0, self.Y)

    def get(self):
        return [self.c_x, self.c_y, self.v_x, self.v_y]

    def get_c(self):
        return [self.c_x, self.c_y]

    def get_v(self):
        return [self.v_x, self.v_y]
    
    def get_color(self):
        return self.color