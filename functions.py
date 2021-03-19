import config
import random
import os
import variables
from colorama import Fore, Back, Style
import objects
from time import time
import numpy as np

ch = ''
ch2 = ''


def print_matrix():
    temp = str(variables.TIME_REM - variables.POWERUP_TIME_SHOOT)
    if (variables.POWERUP_TIME_SHOOT == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1 or variables.SHOOT_FLAG == 0):
        temp = "Not activated"

    temp2 = ''
    if variables.UFO_FLAG == 0:
        temp2 = 'N/A'
    else:
        for i in range(variables.ufo._lives):
            temp2 = temp2 + '|'

    print("\033[2;1H" + Fore.YELLOW +  Style.BRIGHT + 
    ("LEVEL: " + str(variables.LEVEL) + " | LIVES: " + str(variables.paddle.get_lives()) + " | SCORE: " + str(variables.paddle.score())  + " | TIME REMAINING: " +str(variables.TIME_REM) +
    " | Vx: " + str(variables.BALL_SPEED_X) + " | Vy: " + str(variables.BALL_SPEED_Y)  + " | SHOOT_TIME_LEFT: " + temp + " | UFO_HEALTH: " + temp2)  .center(config.columns), end='')
    print(Style.RESET_ALL)
    variables.mp.render()


def create_board():
    x=0
    f=0
    v = random.randint(0,50)
    variables.BONUS_COLUMN = v
    level = variables.LEVEL

    # for j in range(10,variables.mp.height - 5):
    #     for i in range(variables.mp.width):
    #         if(variables.mp.matrix[j][i] != 'O'):
    #             variables.mp.matrix[j][i]=''

    os.system('aplay -q ./sounds/level_up.wav&')
    if level == 1:
        i = 4
        for y in range(19,23, 3):
            for x in range(0,variables.mp.width - 250,3):
                if x >= v and x <v+21 and f == 1:
                    i = 11
                    variables.BONUS_ROW = y
                    brick = objects.Brick(config.brick_bonus,x,y,i)
                    variables.bricks.append(brick)
                    brick.render()
                # elif x >= 90 and x <111 and f == 4:
                #     i = 11
                #     brick = objects.Brick(config.brick_bonus,x,y,i)
                #     variables.bricks.append(brick)
                #     brick.render()
                else:
                    i = random.randint(3,9)
                    if i%2 == 0:
                        brick = objects.Brick(config.brick1,x,y,i)
                    elif i == 3:
                        brick = objects.Brick(config.brick_rainbow,x,y,i)
                    elif i == 5:
                        brick = objects.Brick(config.brick2,x,y,i)
                    elif i == 7:
                        brick = objects.Brick(config.brick3,x,y,i)
                    elif i == 9:
                        brick = objects.Brick(config.brick_fixed,x,y,i)
                    variables.bricks.append(brick)
                    brick.render()
                if f == 1 and i!=9:
                    j = random.randint(0,10)
                    if j%2==0:
                        variables.powerups_index.append(x)
                        variables.powerups_index.append(x+1)
                        if j == 0:
                            powerup = objects.PowerUp(config.powerup_fast,x,y)
                        elif j == 2:
                            powerup = objects.PowerUp(config.powerup_through,x,y)
                        elif j == 4:
                            powerup = objects.PowerUp(config.powerup_expand,x,y)
                        elif j == 6:
                            powerup = objects.PowerUp(config.powerup_shrink,x,y)
                        elif j == 8:
                            powerup = objects.PowerUp(config.powerup_shoot,x,y)
                        elif j == 10:
                            powerup = objects.PowerUp(config.powerup_fireball,x,y)
                    # else:
                    #     powerup = objects.PowerUp(config.no_powerup,x,y)
                        variables.powerups.append(powerup)
            f += 1

    elif level == 2:
        f=0
        for y in range(13,23, 3):
            for x in range(0,variables.mp.width - 250,3):
                if x >= v and x <v+21 and f == 3:
                    i = 11
                    variables.BONUS_ROW = y
                    brick = objects.Brick(config.brick_bonus,x,y,i)
                    variables.bricks.append(brick)
                    brick.render()
                # elif x >= 90 and x <111 and f == 4:
                #     i = 11
                #     brick = objects.Brick(config.brick_bonus,x,y,i)
                #     variables.bricks.append(brick)
                #     brick.render()
                else:
                    i = random.randint(3,9)
                    if i%2 == 0:
                        brick = objects.Brick(config.brick1,x,y,i)
                    elif i == 3:
                        brick = objects.Brick(config.brick_rainbow,x,y,i)
                    elif i == 5:
                        brick = objects.Brick(config.brick2,x,y,i)
                    elif i == 7:
                        brick = objects.Brick(config.brick3,x,y,i)
                    elif i == 9:
                        brick = objects.Brick(config.brick_fixed,x,y,i)
                    variables.bricks.append(brick)
                    brick.render()
                if f == 4 and i!=9:
                    j = random.randint(0,10)
                    if j%2==0:
                        variables.powerups_index.append(x)
                        variables.powerups_index.append(x+1)
                        if j == 0:
                            powerup = objects.PowerUp(config.powerup_fast,x,y)
                        elif j == 2:
                            powerup = objects.PowerUp(config.powerup_through,x,y)
                        elif j == 4:
                            powerup = objects.PowerUp(config.powerup_expand,x,y)
                        elif j == 6:
                            powerup = objects.PowerUp(config.powerup_shrink,x,y)
                        elif j == 8:
                            powerup = objects.PowerUp(config.powerup_shoot,x,y)
                        elif j == 10:
                            powerup = objects.PowerUp(config.powerup_fireball,x,y)
                    # else:
                    #     powerup = objects.PowerUp(config.no_powerup,x,y)
                        variables.powerups.append(powerup)
            f += 1


    elif level == 3:
        f=0

        # y = 5
        # x = variables.paddle.x_coord()
        # variables.ufo = objects.Ufo(config.ufo,x,y)
        # variables.ufo.render()
        variables.UFO_FLAG = 1
        for y in range(10,variables.mp.height - 25, 3):
            for x in range(0,variables.mp.width - 250,3):
                if x >= v and x <v+21 and f == 4:
                    i = 11
                    variables.BONUS_ROW = y
                    brick = objects.Brick(config.brick_bonus,x,y,i)
                    variables.bricks.append(brick)
                    brick.render()
                # elif x >= 90 and x <111 and f == 4:
                #     i = 11
                #     brick = objects.Brick(config.brick_bonus,x,y,i)
                #     variables.bricks.append(brick)
                #     brick.render()
                else:
                    i = random.randint(3,15)
                    if i%2 == 0:
                        brick = objects.Brick(config.brick1,x,y,i)
                    elif i == 3:
                        brick = objects.Brick(config.brick_rainbow,x,y,i)
                    elif i == 5:
                        brick = objects.Brick(config.brick2,x,y,i)
                    elif i == 7:
                        brick = objects.Brick(config.brick3,x,y,i)
                    else:
                        brick = objects.Brick(config.brick_fixed,x,y,i)
                    variables.bricks.append(brick)
                    brick.render()
                if f == 4 and i!=9:
                    j = random.randint(0,10)
                    if j%2==0:
                        variables.powerups_index.append(x)
                        variables.powerups_index.append(x+1)
                        if j == 0:
                            powerup = objects.PowerUp(config.powerup_fast,x,y)
                        elif j == 2:
                            powerup = objects.PowerUp(config.powerup_through,x,y)
                        elif j == 4:
                            powerup = objects.PowerUp(config.powerup_expand,x,y)
                        elif j == 6:
                            powerup = objects.PowerUp(config.powerup_shrink,x,y)
                        elif j == 8:
                            powerup = objects.PowerUp(config.powerup_shoot,x,y)
                        elif j == 10:
                            powerup = objects.PowerUp(config.powerup_fireball,x,y)
                    # else:
                    #     powerup = objects.PowerUp(config.no_powerup,x,y)
                        variables.powerups.append(powerup)
            f += 1
    else:
        os.system('aplay -q ./sounds/game_over.wav&')
        exit_screen("Game over!")


    # for y in range(10,variables.mp.height - 25, 3):
    #     for x in range(0,variables.mp.width - 250,3):
    #         if x >= v and x <v+21 and f == 4:
    #             i = 11
    #             variables.BONUS_ROW = y
    #             brick = objects.Brick(config.brick_bonus,x,y,i)
    #             variables.bricks.append(brick)
    #             brick.render()
    #         # elif x >= 90 and x <111 and f == 4:
    #         #     i = 11
    #         #     brick = objects.Brick(config.brick_bonus,x,y,i)
    #         #     variables.bricks.append(brick)
    #         #     brick.render()
    #         else:
    #             i = random.randint(4,9)
    #             if i%2 == 0:
    #                 brick = objects.Brick(config.brick1,x,y,i)
    #             elif i == 5:
    #                 brick = objects.Brick(config.brick2,x,y,i)
    #             elif i == 7:
    #                 brick = objects.Brick(config.brick3,x,y,i)
    #             elif i == 9:
    #                 brick = objects.Brick(config.brick_fixed,x,y,i)
    #             variables.bricks.append(brick)
    #             brick.render()
    #         if f == 4 and i!=9:
    #             j = random.randint(0,8)
    #             if j%2==0:
    #                 variables.powerups_index.append(x)
    #                 variables.powerups_index.append(x+1)
    #                 if j == 0:
    #                     powerup = objects.PowerUp(config.powerup_shrink,x,y)
    #                 elif j == 2:
    #                     powerup = objects.PowerUp(config.powerup_expand,x,y)
    #                 elif j == 4:
    #                     powerup = objects.PowerUp(config.powerup_through,x,y)
    #                 elif j == 6:
    #                     powerup = objects.PowerUp(config.powerup_fast,x,y)
    #                 elif j == 8:
    #                     powerup = objects.PowerUp(config.powerup_grab,x,y)
    #             # else:
    #             #     powerup = objects.PowerUp(config.no_powerup,x,y)
    #                 variables.powerups.append(powerup)
    #     f += 1

        

def check_level_change():
    if variables.LEVEL_CHANGE_FLAG == 1:
        variables.LEVEL += 1
        initialize_board()
        variables.LEVEL_CHANGE_FLAG = 0
        



def initialize_board():
    # variables.mp.matrix = np.empty((variables.mp.height,variables.mp.width))
    # variables.mp.matrix = np.array([[" " for x in range(variables.mp.width)] for y in range(0,variables.mp.height)])
    variables.mp.__init__()
    create_board()
    # for y in range(10,variables.mp.height - 20, 2):
    #     for x in range(0,variables.mp.width - 250,6):
    #         brick = objects.Brick(config.brick,x,y,random.randint(0,3)+3)
    #         brick.render()
    variables.paddle.render()
    variables.ball.render()
    ch = ''
    ch2 = ''
    print_matrix()
    # variables.LAST_TIME = time()
    # variables.TIME_BEGUN = round(variables.LAST_TIME)


def ball_move(ball):
    
    if ball.get_status() == 1:
        ball.clear()
        # speedx = variables.ball.get_vx()
        # speedy = variables.ball.get_vy()
        speedx = variables.BALL_SPEED_X
        speedy = variables.BALL_SPEED_Y

        if ball.get_vx() > 0 :
            if ball.x_coord() < variables.mp.start_index + config.columns:
                ball.x_change(speedx)
        elif ball.get_vx() < 0:
            ball.x_change(-speedx)

        if ball.get_vy() > 0:
            ball.y_change(-speedy)

        elif ball.get_vy() < 0:
            ball.y_change(speedy)
        ball.check_collision()
        ball.render()

def powerup_fall(powerup):
    if powerup.get_status() == 1:
        powerup.clear()
        # temp = powerup.get_vy()
        # powerup.y_change_under_gravity()
        # powerup.x_change(powerup.get_vx())
        powerup.inc_vy(0.01)
        powerup.y_change(powerup.get_vy())
        # v = int()
        powerup.x_change(powerup.get_vx())

        check_powerup(powerup)
        if(powerup.y_coord() > variables.paddle_base+1):
            # powerup.clear()
            # variables.mp.matrix[int(powerup.y_coord())][int(powerup.x_coord())]=" "
            powerup.change_status_to_0()
        powerup.render()

def check_powerup(powerup):
    if(int(powerup.y_coord()) == int(variables.paddle_base) and int(powerup.x_coord()) > int(variables.paddle.x_coord()) and int(powerup.x_coord()) < int(variables.paddle.x_coord()) + variables.paddle.get_width()-1):
       perform_powerup(powerup) 

def perform_powerup(powerup):
    os.system('aplay -q ./sounds/powerup.wav&')
    if powerup.get_type() == '?':
        variables.BALL_SPEED_X += 0.1
        variables.BALL_SPEED_Y += 0.1
        variables.POWERUP_TIME_FAST = variables.TIME_REM - variables.POWERUP_DURATION
    elif powerup.get_type() == '>':
        variables.paddle.expand_shape()
        variables.POWERUP_TIME_EXPAND = variables.TIME_REM - variables.POWERUP_DURATION
    elif powerup.get_type() == '<':
        variables.paddle.shrink_shape()
        variables.POWERUP_TIME_SHRINK = variables.TIME_REM - variables.POWERUP_DURATION
    elif powerup.get_type() == '@':
        variables.ball.brick_collision = 0
        variables.POWERUP_TIME_THROUGH = variables.TIME_REM - variables.POWERUP_DURATION
    elif powerup.get_type() == 'G':
        # variables.ball.brick_collision = 0
        variables.FIREBALL_FLAG = 1
        variables.POWERUP_TIME_FIREBALL = variables.TIME_REM - variables.POWERUP_DURATION
    elif powerup.get_type() == '|':
        variables.SHOOT_FLAG = 1
        variables.POWERUP_TIME_SHOOT = variables.TIME_REM - variables.POWERUP_DURATION
        
    powerup.change_status_to_0()

def check_powerup_timeout():
    if variables.POWERUP_TIME_FAST == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1:
        variables.BALL_SPEED_X = variables.ORG_BALL_SPEED_X
        variables.BALL_SPEED_Y = variables.ORG_BALL_SPEED_Y
        variables.POWERUP_TIME_FAST = -1
    
    if variables.POWERUP_TIME_THROUGH == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1:
        variables.ball.brick_collision = 1

    if variables.POWERUP_TIME_SHRINK == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1:
        variables.paddle.reset_shape_to_original()

    if variables.POWERUP_TIME_EXPAND == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1:
        variables.paddle.reset_shape_to_original()

    if variables.POWERUP_TIME_FIREBALL == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1:
        variables.FIREBALL_FLAG = 0

    if variables.POWERUP_TIME_SHOOT == variables.TIME_REM or variables.LEVEL_CHANGE_FLAG == 1:
        variables.SHOOT_FLAG = 0

def set_board():
    for i in range(4, variables.mp.height, 3):
            for j in range(variables.mp.width):
                if variables.mp.matrix[i][j] == "L":
                        variables.mp.matrix[i][j+1] = "E"
                        variables.mp.matrix[i+1][j+1] = "1"
                        variables.mp.matrix[i+1][j] = "V"
                        
                elif variables.mp.matrix[i][j] == "E":
                    variables.mp.matrix[i][j-1] = "L"
                    variables.mp.matrix[i+1][j-1] = "V"
                    variables.mp.matrix[i+1][j] = "1"

                elif variables.mp.matrix[i][j] == "V":
                    variables.mp.matrix[i][j+1] = "1"
                    variables.mp.matrix[i-1][j+1] = "E"
                    variables.mp.matrix[i-1][j] = "L"

                elif variables.mp.matrix[i][j] == "1":
                    variables.mp.matrix[i][j-1] = "V"
                    variables.mp.matrix[i-1][j-1] = "L"
                    variables.mp.matrix[i-1][j] = "E"  

                elif variables.mp.matrix[i][j] == "l":
                    variables.mp.matrix[i][j+1] = "e"
                    variables.mp.matrix[i+1][j+1] = "2"
                    variables.mp.matrix[i+1][j] = "v"
                    
                elif variables.mp.matrix[i][j] == "e":
                    variables.mp.matrix[i][j-1] = "l"
                    variables.mp.matrix[i+1][j-1] = "v"
                    variables.mp.matrix[i+1][j] = "2"

                elif variables.mp.matrix[i][j] == "v":
                    variables.mp.matrix[i][j+1] = "2"
                    variables.mp.matrix[i-1][j+1] = "e"
                    variables.mp.matrix[i-1][j] = "l"

                elif variables.mp.matrix[i][j] == "2":
                    variables.mp.matrix[i][j-1] = "v"
                    variables.mp.matrix[i-1][j-1] = "l"
                    variables.mp.matrix[i-1][j] = "e"

                elif variables.mp.matrix[i][j] == "F":
                    variables.mp.matrix[i][j+1] = "I"
                    variables.mp.matrix[i+1][j+1] = "A"
                    variables.mp.matrix[i+1][j] = "N"
                    
                elif variables.mp.matrix[i][j] == "I":
                    variables.mp.matrix[i][j-1] = "F"
                    variables.mp.matrix[i+1][j-1] = "N"
                    variables.mp.matrix[i+1][j] = "A"

                elif variables.mp.matrix[i][j] == "N":
                    variables.mp.matrix[i][j+1] = "A"
                    variables.mp.matrix[i-1][j+1] = "I"
                    variables.mp.matrix[i-1][j] = "F"

                elif variables.mp.matrix[i][j] == "A":
                    variables.mp.matrix[i][j-1] = "N"
                    variables.mp.matrix[i-1][j-1] = "F"
                    variables.mp.matrix[i-1][j] = "I"

                elif variables.mp.matrix[i][j] == "R":
                    variables.mp.matrix[i][j+1] = "0"
                    variables.mp.matrix[i+1][j+1] = "K"
                    variables.mp.matrix[i+1][j] = "C"
                    
                elif variables.mp.matrix[i][j] == "0":
                    variables.mp.matrix[i][j-1] = "R"
                    variables.mp.matrix[i+1][j-1] = "C"
                    variables.mp.matrix[i+1][j] = "K"

                elif variables.mp.matrix[i][j] == "C":
                    variables.mp.matrix[i][j+1] = "K"
                    variables.mp.matrix[i-1][j+1] = "0"
                    variables.mp.matrix[i-1][j] = "R"

                elif variables.mp.matrix[i][j] == "K":
                    variables.mp.matrix[i][j-1] = "C"
                    variables.mp.matrix[i-1][j-1] = "R"
                    variables.mp.matrix[i-1][j] = "0"   
   




def clear_brick(x, y, ball):
    # pass
    ind_i = [0,1,-1]
    ind_j = [0,1,-1]

    if(variables.mp.matrix[int(y)][int(x)]=="|"):
        if ball.get_vx() > 0:
            if variables.mp.matrix[int(y)][int(x)-1] == '_' or variables.mp.matrix[int(y)][int(x)-1] == '\u203e':
                for i in range(3):
                    variables.mp.matrix[int(y)][int(x)-i]=" "
                    variables.mp.matrix[int(y)-1][int(x)-i]=" "
                    variables.mp.matrix[int(y)+1][int(x)-i]=" "
            else:
                for i in range(3):
                    variables.mp.matrix[int(y)][int(x)+i]=" "
                    variables.mp.matrix[int(y)-1][int(x)+i]=" "
                    variables.mp.matrix[int(y)+1][int(x)+i]=" "

        elif ball.get_vx() < 0:
            if variables.mp.matrix[int(y)][int(x)-1] == '_' or variables.mp.matrix[int(y)][int(x)-1] == '\u203e':
                for i in range(3):
                    variables.mp.matrix[int(y)][int(x)-i]=" "
                    variables.mp.matrix[int(y)-1][int(x)-i]=" "
                    variables.mp.matrix[int(y)+1][int(x)-i]=" "
            else:
                for i in range(3):
                    variables.mp.matrix[int(y)][int(x)+i]=" "
                    variables.mp.matrix[int(y)-1][int(x)+i]=" "
                    variables.mp.matrix[int(y)+1][int(x)+i]=" "

        ball.rev_vx()

            

    elif variables.mp.matrix[int(y)][int(x)]=="_":
        ball.rev_vy()
        for i in range(2):
            variables.mp.matrix[int(y)-i][int(x)-1]=" "
            variables.mp.matrix[int(y)-i][int(x)+1]=" "
            variables.mp.matrix[int(y)-i][int(x)]=" "

    elif variables.mp.matrix[int(y)][int(x)]=="\u203e":
        ball.rev_vy()
        for i in range(2):
            variables.mp.matrix[int(y)+i][int(x)-1]=" "
            variables.mp.matrix[int(y)+i][int(x)+1]=" "
            variables.mp.matrix[int(y)+i][int(x)]=" "


def check_ball_side():
    if variables.ball.x_coord()<=0:
        variables.ball.rev_vx()
        os.system('aplay -q ./sounds/ball_hit.wav&')

    elif variables.ball.x_coord()>=variables.mp.start_index + config.columns:
        variables.ball.rev_vx()
        os.system('aplay -q ./sounds/ball_hit.wav&')



def check_ball_base():
    if (variables.ball.y_coord() >= variables.paddle.y_coord()) and variables.ball.x_coord() > variables.paddle.x_coord() and (variables.ball.x_coord() < variables.paddle.x_coord() + variables.paddle.get_width()-1):
        # variables.paddle.clear()
        # quit()
        variables.ball.clear()
        variables.ball.reset2()
        # variables.paddle.reset2()
    elif variables.ball.y_coord() > variables.paddle_base + 1:
        variables.paddle.clear()
        variables.ball.clear()
        variables.paddle.dec_lives()
        os.system('aplay -q ./sounds/lost_life.wav&')
        variables.BALL_SPEED_X = variables.ORG_BALL_SPEED_X
        variables.BALL_SPEED_Y = variables.ORG_BALL_SPEED_Y
        if variables.paddle.get_lives() <= 0:
            os.system('aplay -q ./sounds/game_over.wav&')
            exit_screen("Lives over!!")
        else:
            variables.ball.reset()
            variables.paddle.reset()
            variables.SHOOT_FLAG = 0
            os.system('aplay -q ./sounds/lost_life.wav&')
            variables.BALL_SPEED_X = variables.ORG_BALL_SPEED_X
            variables.BALL_SPEED_Y = variables.ORG_BALL_SPEED_Y


def check_ball_paddle_collision():
    if (variables.ball.y_coord()  == variables.paddle.y_coord() or variables.ball.y_coord()  == variables.paddle.y_coord() - 1) and variables.ball.x_coord() >= variables.paddle.x_coord() and variables.ball.x_coord() < variables.paddle.x_coord() + variables.paddle.get_width():
        variables.ball.rev_vy()
        # brick_fall()
        if variables.ball.get_status() == 1:
            os.system('aplay -q ./sounds/ball_hit.wav&')
            # if variables.TIME_REM < variables.BRICK_FALL_TIME:
            #     brick_fall()
            if variables.ball.x_coord() < variables.paddle.x_coord() + 2:
                variables.BALL_SPEED_X -= 0.02
            elif variables.ball.x_coord() < variables.paddle.x_coord() + 4:
                variables.BALL_SPEED_X -= 0.01
            elif variables.ball.x_coord() < variables.paddle.x_coord() + 6:
                variables.BALL_SPEED_X += 0.01
            elif variables.ball.x_coord() < variables.paddle.x_coord() + 8:
                variables.BALL_SPEED_X += 0.02
            if variables.TIME_REM < variables.BRICK_FALL_TIME:
                brick_fall()

def exit_screen(message):
    os.system('tput reset')
    variables.powerups_index = []
    print(Fore.RED + Style.BRIGHT + "BRICK - BREAKER".center(config.columns))
    print(Fore.YELLOW + Style.BRIGHT + ("SCORE: " + str(variables.paddle.score())).center(config.columns) + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + ("LIVES LEFT: " + str(variables.paddle.get_lives())).center(config.columns) + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + (message).center(config.columns) + Style.RESET_ALL)
    # print(Style.RESET_ALL)
    # for p in variables.powerups:
    #     print( p._type , " ", p.get_status(), " ", p.y_coord())
    # print(Style.RESET_ALL)
    quit()
    return


def brick_fall():
    j = variables.mp.height - 7
    while(j > 8 and j < variables.mp.height - 6):
        for i in range(variables.mp.width):
            if(variables.mp.matrix[j][i] != "O" or variables.mp.matrix[j][i] != "@" or variables.mp.matrix[j][i] != ">" or variables.mp.matrix[j][i] != "<" or variables.mp.matrix[j][i] != "?" or variables.mp.matrix[j][i] != "G" or variables.mp.matrix[j][i] != "|"):
                variables.mp.matrix[j+1][i] = variables.mp.matrix[j][i]
        j -= 1

    lower_lim = variables.paddle_base - 2
    for i in range(variables.mp.width):
        if (variables.mp.matrix[lower_lim][i] == "C" or variables.mp.matrix[lower_lim][i] == "K" or 
        variables.mp.matrix[lower_lim][i] == "N"  or variables.mp.matrix[lower_lim][i] == "A" or
        variables.mp.matrix[lower_lim][i] == "v" or variables.mp.matrix[lower_lim][i] == "2" or 
        variables.mp.matrix[lower_lim][i] == "V" or variables.mp.matrix[lower_lim][i] == "1" or
        variables.mp.matrix[lower_lim][i] == "#"):
            os.system('aplay -q ./sounds/game_over.wav&')
            exit_screen("Game over!")


def shoot_bullets():
    bullet1 = objects.Bullet(config.bullet, variables.paddle.x_coord(), variables.paddle.y_coord())
    bullet2 = objects.Bullet(config.bullet, variables.paddle.x_coord() + variables.paddle.get_width(), variables.paddle.y_coord())
    variables.bullets.append(bullet1)
    variables.bullets.append(bullet2)
    # file = open("shoot_test.txt", "a")
    # file.write("\nshooting\n")
    # file.write(str(bullet1.x_coord()))
    # file.write(" " + str(bullet1.y_coord()) + "\n")
    # file.write(str(bullet2.x_coord()))
    # file.write(" " + str(bullet2.y_coord()) + "\n")
    # file.close()




def bullet_move(bullet):
    bullet.clear()
    bullet.check_collision()
    if bullet.get_status() == 1:
        bullet.y_change(-0.15)
    bullet.render()
    # file = open("shoot_test.txt", "a")
    # file.write("\nmoving\n")
    # file.write(str(bullet.x_coord()))
    # file.write(" " + str(bullet.y_coord()) + "\n")
    # file.write(str(bullet2.x_coord()))
    # file.write(" " + str(bullet2.y_coord()) + "\n")
    # file.close()


def drop_bomb():
    if variables.UFO_FLAG == 1 and (variables.ufo.x_coord()+1)%3 == 0 and random.randint(0,20) == 2:
        bomb = objects.Bomb(config.bomb,variables.ufo.x_coord()+3,variables.ufo.y_coord())
        variables.bombs.append(bomb)


def bomb_fall(bomb):
    bomb.y_change(0.1)