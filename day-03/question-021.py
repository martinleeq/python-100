"""
问题21: 模拟机器人行动,并计算与原点的距离
在控制台输入机器人行进的方向以及距离, 在其行动结束后,计算机器人与原点的位置
控制台的输入形如:
UP 2
DOWN 4
LEFT 2
RIGHT 2
"""

import math

class Robot(object):

    def __init__(self) -> None:
        self.x0 = self.x1 = 0
        self.y0 = self.y1 = 0
        self.dist = 0

    def move(self, directive):
        ops = str(directive).split()
        if ops[0].upper() == 'UP':
            self.y1 -= int(ops[1])
        elif ops[0].upper() == 'DOWN':
            self.y1 += int(ops[1])
        elif ops[0].upper() == 'LEFT':
            self.x1 -= int(ops[1])
        elif ops[0].upper() == 'RIGHT':
            self.x1 += int(ops[1])

        self.dist = round(math.sqrt((self.x1 - self.x0) ** 2 + (self.y1 - self.y0) ** 2))

    def get_distance(self):
        return self.dist


robot = Robot()
while True:
    raw = input()
    if not raw:
        break
    else:
        robot.move(raw)

print(robot.get_distance())
