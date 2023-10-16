import pygame
import game_map

v = .1

w_code = [26, 82]
a_code = [4, 80]
s_code = [22, 81]
d_code = [7, 79]

class Player:
    def __init__(self):
        self.x = game_map.block_size
        self.y = game_map.block_size
        self.w_pressed = 0
        self.a_pressed = 0
        self.s_pressed = 0
        self.d_pressed = 0
        self.vx = 0
        self.vy = 0

    def handle(self, event, key):
        if event == pygame.KEYDOWN:
            if key in a_code:
                self.a_pressed = 1
            elif key in d_code:
                self.d_pressed = 1
            elif key in w_code:
                self.w_pressed = 1
            elif key in s_code:
                self.s_pressed = 1
        elif event == pygame.KEYUP:
            if key in a_code:
                self.a_pressed = 0
            elif key in d_code:
                self.d_pressed = 0
            elif key in w_code:
                self.w_pressed = 0
            elif key in s_code:
                self.s_pressed = 0
        self.vx = (self.d_pressed - self.a_pressed) * v
        self.vy = (self.s_pressed - self.w_pressed) * v

    def update(self, time):
        self.x += self.vx * time
        self.x, _, self.vx, _ = game_map.check_collision(self.x, self.y, self.vx, self.vy)
        self.y += self.vy * time
        _, self.y, _, self.vy = game_map.check_collision(self.x, self.y, self.vx, self.vy)
