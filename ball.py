from pico2d import *
import game_world
import game_framework
import random
import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        sx =self.x - server.boy.x+get_canvas_width() //2
        sy =self.y - server.boy.y+get_canvas_height() //2
        self.image.draw(sx,sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        sx = self.x - server.boy.x +get_canvas_width() //2
        sy = self.y - server.boy.y +get_canvas_height() //2
        return sx - 10, sy - 10, sx + 10, sy + 10

    def handle_collision(self, group, other):
        pass
