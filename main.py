import variables 
import functions
from variables import paddle, ball, ufo
import inputs
import random
import config
import objects
from time import time, sleep
import signal


functions.initialize_board()
variables.LAST_TIME = time()
variables.TIME_BEGUN = round(variables.LAST_TIME)


while True:
    variables.TIME_REM = variables.TIME_TOTAL - round(time()) + variables.TIME_BEGUN
    variables.powerups_index = []
    if variables.TIME_REM == 0:
        message = "Time is over!!"
        functions.exit_screen(message)
        break
    
    paddle.clear()
    ball.clear()
    if variables.UFO_FLAG == 1:
        ufo.clear()
    inputs.movedin()
    paddle.render()
    ball.render()


    if variables.UFO_FLAG == 1:
        ufo.render()

    functions.check_level_change()
    functions.check_ball_base()
    functions.check_ball_side()
    functions.check_ball_paddle_collision()

    # if ball.get_status() == 1:
    functions.ball_move(ball)
    functions.drop_bomb()
    for p in variables.powerups:
        if p.get_status() == 1 and p._type != ' ':
            p.render()
            functions.powerup_fall(p)

    for b in variables.bullets:
        if b.get_status() == 1 and p._type != ' ':
            b.render()
            functions.bullet_move(b)
        else:
            b.clear()


    for b in variables.bombs:
        if b.get_status() == 1 and p._type != ' ':
            b.clear()
            b.y_change(0.1)
            if b.check_collision() != 1 and b.get_status() == 1:
                b.render()


    functions.check_powerup_timeout()
    functions.print_matrix()
    
