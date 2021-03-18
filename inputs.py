from variables import paddle, ball
import variables
import functions
import config
import os
import sys
import termios
import tty
import signal
import atexit
from select import select

class KBHit(object):
    def __init__(self):
        if os.name == 'nt':
            pass
        else:
            self.filed = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.filed)
            self.old_term = termios.tcgetattr(self.filed)

            self.new_term[3] = (self.new_term[3] & ~
                                termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.filed, termios.TCSAFLUSH, self.new_term)
            atexit.register(self.set_normal_term)
            self.temp = 1

    def kbhit(self):
        draw, dwarf, deaf = select([sys.stdin], [], [], 0)
        self.temp = dwarf
        self.temp = deaf
        return draw != []

    def getinput(self):
        if self.kbhit():
            return self.getch()
        else:
            return ""

    def getch(self):
        self.temp = 1
        return sys.stdin.read(1)

    def set_normal_term(self):
        self.temp = 0
        termios.tcsetattr(self.filed, termios.TCSAFLUSH, self.old_term)


kb = KBHit()


def movedin():
    char = kb.getinput()

    if char == 'w':
        if ball.get_status() == 0:
            variables.BALL_SPEED_X = variables.ORG_BALL_SPEED_X
            variables.BALL_SPEED_Y = variables.ORG_BALL_SPEED_Y
            ball.set_status(1)

    if char == 'q':
        message = "You quit the game !!"
        functions.exit_screen(message)
        quit()

    if char == 'd':
        left_limit = variables.mp.start_index + config.columns - paddle.get_width() - 2
        right_limit = 1090
        if paddle.x_coord() <= left_limit and paddle.x_coord() <= right_limit:
            paddle.x_change(1)
            if ball.get_status() == 0:
                ball.x_change(1)

    if char == 'a':
        if paddle.x_coord() > variables.mp.start_index :
            paddle.x_change(-1)
            if ball.get_status() == 0:
                ball.x_change(-1)

    if char == 'p':
        variables.LEVEL_CHANGE_FLAG = 1
        functions.check_powerup_timeout()
        for p in variables.powerups:
            p.clear()
            p.change_status_to_0()
        variables.ball.reset()
        variables.paddle.reset()


    if char == 'x' and variables.SHOOT_FLAG == 1:
        os.system('aplay -q ./sounds/shoot.wav&')
        functions.shoot_bullets()

    

    

