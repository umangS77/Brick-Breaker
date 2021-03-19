from time import time,sleep
import random
import functions
import variables 
import config
import os

class Object():

    def __init__(self, element, x, y):
        self._posx = x
        self._posy = y
        self._shape = element
        self._width = len(element[0])
        self._height = len(element)

    def x_coord(self):
        return self._posx

    def y_coord(self):
        return self._posy

    def x_change(self, x):
        self._posx += x
    
    def y_change(self, y):
        self._posy += y

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = self._shape[j][i]

    


class Ball(Object):
    def __init__(self,element,x,y):
        super().__init__(element, x, y)
        self._vx = variables.ORG_BALL_SPEED_X
        self._vy = variables.ORG_BALL_SPEED_Y
        self.status = 0
        self.brick_collision = 1

    def get_status(self):
        return self.status
    
    def set_status(self,s):
        self.status = s

    def get_vx(self):
        return self._vx

    def get_vy(self):
        return self._vy

    def inc_vx(self):
        self._vx += 0.1

    def inc_vy(self):
        self._vy += 0.1

    def dec_vx(self):
        self._vx -= 0.1

    def dec_vy(self):
        self._vy -= 0.1
    
    def rev_vx(self):
        self._vx *= -1

    def rev_vy(self):
        self._vy *= -1

    def powerup_speed(self):
        variables.BALL_SPEED_X *= 2
        variables.BALL_SPEED_Y *= 2  
        self._vx = variables.BALL_SPEED_X
        self._vy = variables.BALL_SPEED_Y

    def reset(self):
        self._vx = variables.ORG_BALL_SPEED_X
        self._vy = variables.ORG_BALL_SPEED_Y
        self.status = 0
        brick_collision = 1
        self._posx = variables.ball_start
        self._posy = variables.ball_base
        variables.BALL_SPEED_X = variables.ORG_BALL_SPEED_X
        variables.BALL_SPEED_Y = variables.ORG_BALL_SPEED_Y

    def reset2(self):
        self._vx = variables.ORG_BALL_SPEED_X
        self._vy = variables.ORG_BALL_SPEED_Y
        self.status = 0
        brick_collision = 1
        self._posx = variables.paddle.x_coord()+3
        self._posy = variables.paddle.y_coord()-1
        variables.BALL_SPEED_X = variables.ORG_BALL_SPEED_X
        variables.BALL_SPEED_Y = variables.ORG_BALL_SPEED_Y
    
    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = self._shape[j][i]
    
    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "O":
                    variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "

    def perform_fireball(self):
        if variables.FIREBALL_FLAG == 1:
            os.system('aplay -q ./sounds/bricks_explode.wav&')
            # file = open("test.txt", "w")
            start_y = int(self._posy)
            start_x = int(self._posx)
            # file.write("start_y = " + str(start_y) + "\nstart_x = " + str(start_x));

            for jj in range(start_y - 5, start_y + 5,1):
                for ii in range(start_x - 5, start_x + 5,1):
                    # file.write(str(jj) + "   "+ str(ii) + "\n")
                    variables.mp.matrix[int(jj)][int(ii)] = " "
                    variables.paddle.inc_score(1)
            # file.close()

    def check_collision(self): 
        
        vx = variables.BALL_SPEED_X
        vy = variables.BALL_SPEED_Y

        i=0
        j=0

        if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "":
            pass
        if int(self._posy) == 22 or int(self._posy) == 23:
            for p in variables.powerups:
                if (p.x_coord() == int(self._posx) or p.x_coord() == int(self._posx)-1) and  variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] != " ":
                    p.change_status_to_1()
                    p.set_vx(variables.ball.get_vx()*1.2)
                    p.y_change(2)
                    p.set_vy(abs(variables.ball.get_vy())*0.3)



        if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "#":
            os.system('aplay -q ./sounds/bricks_explode.wav&')
            start_y = int(j+self._posy - 4)
            start_x = variables.BONUS_COLUMN - 3
            c=9
            if start_x <0:
                c=8
                start_x = 0
            for jj in range(start_y, start_y+6):
                for ii in range(start_x,start_x + c*3):
                    # if variables.mp.matrix[int(jj)][int(ii)] != "R" and variables.mp.matrix[int(jj)][int(ii)] != "0" and variables.mp.matrix[int(jj)][int(ii)] != "C" and variables.mp.matrix[int(jj)][int(ii)] != "K":
                    variables.mp.matrix[int(jj)][int(ii)] = " "
                    variables.paddle.inc_score(1)

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "X" or variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] == "X":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            variables.ball.rev_vy()

        
        # if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] != " " and variables.ball.brick_collision == 0:
        #     variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
        #     variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
        #     variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = " "
        #     variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "
        #     variables.paddle.inc_score(3)

        # elif variables.FIREBALL_FLAG == 1
        #     start_y = int(j+self._posy)
        #     start_x = int(i+self._posx)

        #     for jj in range(start_y - 4, start_y + 4):
        #         for ii in range(start_x - 4, start_x + 4):
        #             variables.mp.matrix[int(jj)][int(ii)] = " "
        #             variables.paddle.inc_score(1)





        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "F":
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = " "
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "
            variables.paddle.inc_score(3)
            os.system('aplay -q ./sounds/bricks_explode.wav&')
            self.perform_fireball()

            if variables.ball.brick_collision == 1:
                if vy < 0 :
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "I":
            
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = " "
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "
            variables.paddle.inc_score(3)
            os.system('aplay -q ./sounds/bricks_explode.wav&')
            self.perform_fireball()

            if variables.ball.brick_collision == 1:
                if vy < 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "


        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "N":
            
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = " "
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "
            variables.paddle.inc_score(3)
            os.system('aplay -q ./sounds/bricks_explode.wav&')
            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "A":
            
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = " "
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "
            variables.paddle.inc_score(3)
            os.system('aplay -q ./sounds/bricks_explode.wav&')
            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "


        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "l":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy < 0 :
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()

                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "F"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "I"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = "A"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "N"
                variables.paddle.inc_score(2)
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "e":
            os.system('aplay -q ./sounds/ball_hit.wav&')

            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy < 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "I"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "F"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = "N"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "A"
                variables.paddle.inc_score(2)
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "v":
            os.system('aplay -q ./sounds/ball_hit.wav&')

            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "N"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "A"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = "I"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "F"
                variables.paddle.inc_score(2)
                #self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "2":
            os.system('aplay -q ./sounds/ball_hit.wav&')            
            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "A"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "N"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = "F"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "I"
                variables.paddle.inc_score(2)
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "
                

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "L":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "l"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "e"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = "2"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "v"
            variables.paddle.inc_score(1)
            if variables.ball.brick_collision == 1:
                if vy < 0 :
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "E":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "e"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "l"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = "v"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "2"
            variables.paddle.inc_score(1)
            if variables.ball.brick_collision == 1:
                if vy < 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                #self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "


        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "V":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "v"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "2"
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = "e"
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "l"
            variables.paddle.inc_score(1)
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                #self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "1":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "2"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "v"
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = "l"
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "e"
            variables.paddle.inc_score(1)
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                #self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "R":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "R"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "0"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "C"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = "K"
            # variables.paddle.inc_score(1)
            if variables.ball.brick_collision == 1:
                if vy < 0 :
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                #self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "0":
            
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "o"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "R"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = "C"
            variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "K"
            # variables.paddle.inc_score(1)
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                if vy < 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = " "


        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "C":
            
            
            # variables.paddle.inc_score(1)
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            if variables.ball.brick_collision == 1:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "C"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "K"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = "0"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "R"
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()
            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)+1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "K":
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "K"
            variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "C"
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = "R"
            variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "0"
            # variables.paddle.inc_score(1)
            if variables.ball.brick_collision == 1:
                if vy > 0:
                    variables.ball.rev_vy()
                else:
                    variables.ball.rev_vx()
                # self.perform_fireball()

            else:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = " "
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = " "

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "Z":
            if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] == " " and variables.mp.matrix[int(j+self._posy-1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "L"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "E"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "V"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx+1)] = "1"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] == " " and variables.mp.matrix[int(j+self._posy+1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "V"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "1"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "L"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx+1)] = "E"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] == " " and variables.mp.matrix[int(j+self._posy-1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "E"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "L"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = "V"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "1"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] == " " and variables.mp.matrix[int(j+self._posy+1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "1"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "V"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = "L"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "E"
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "z":
            if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] == " " and variables.mp.matrix[int(j+self._posy-1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "l"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "e"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "v"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx+1)] = "2"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] == " " and variables.mp.matrix[int(j+self._posy+1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "v"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "2"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "l"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx+1)] = "e"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] == " " and variables.mp.matrix[int(j+self._posy-1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "e"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "l"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = "v"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "2"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] == " " and variables.mp.matrix[int(j+self._posy+1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "2"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "v"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = "l"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "e"
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "y":
            if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] == " " and variables.mp.matrix[int(j+self._posy-1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "F"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "I"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "N"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx+1)] = "A"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] == " " and variables.mp.matrix[int(j+self._posy+1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "N"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] = "A"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "F"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx+1)] = "I"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] == " " and variables.mp.matrix[int(j+self._posy-1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "I"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "F"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)-1] = "N"
                variables.mp.matrix[int(j+self._posy)+1][int(i+self._posx)] = "A"
            elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)+1] == " " and variables.mp.matrix[int(j+self._posy+1)][int(i+self._posx)] == " ":
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = "A"
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)-1] = "N"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)-1] = "F"
                variables.mp.matrix[int(j+self._posy)-1][int(i+self._posx)] = "I"
            os.system('aplay -q ./sounds/ball_hit.wav&')
            self.perform_fireball()

        elif variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == "=":
            variables.ball.rev_vy()
            variables.ufo.dec_lives()

            if variables.ufo._lives <= 0:
                os.system('aplay -q ./sounds/bricks_explode.wav&')
                ufo.change_status_to_0()
                variables.paddle.inc_score(10)
                variables.UFO_FLAG = 0



                
        

class Paddle(Object):
    def __init__(self,element,x,y,lives):
        super().__init__(element, x, y)
        self.__lives = config.lives
        self.__score = 0

    def get_lives(self):
        return self.__lives

    def score(self):
        return self.__score

    def increase_width(self):
        self._width += 2

    def dec_lives(self):
        self.__lives -= 1
    
    def inc_score(self, x):
        self.__score += x

    def get_width(self):
        return self._width
    
    

    def reset(self):
        self._posx = variables.paddle_start
        self._posy = variables.paddle_base
        element = config.paddle
        self._shape = element
        self._width = len(element[0])
        self._height = len(element)

        variables.POWERUP_TIME_FAST = -1
        variables.POWERUP_TIME_THROUGH = -1
        variables.POWERUP_TIME_SHRINK = -1
        variables.POWERUP_TIME_EXPAND = -1
        variables.POWERUP_TIME_FIREBALL = -1
        variables.FIREBALL_FLAG = 0

        for p in variables.powerups:
            p.change_status_to_0()
        variables.ball.brick_collision = 1;

        for j in range(21,50):
            for i in range(0,150):
                if(variables.mp.matrix[j][i] == "@" or variables.mp.matrix[j][i] == "?" or variables.mp.matrix[j][i] == "<" or variables.mp.matrix[j][i] == ">" or variables.mp.matrix[j][i] == "G"):
                    variables.mp.matrix[j][i]=" "

    # def reset2(self):
    #     self._posx = variables.paddle_start
    #     self._posy = variables.paddle_base


    def expand_shape(self):
        new_shape = ""
        new_shape = config.paddle_expand
        self._shape = new_shape
        self._width = len(new_shape[0])
        self._height = len(new_shape)

    def shrink_shape(self):
        new_shape = ""
        new_shape = config.paddle_shrink
        self._shape = new_shape
        self._width = len(new_shape[0])
        self._height = len(new_shape)

    def reset_shape_to_original(self):
        new_shape = ""
        new_shape = config.paddle
        self._shape = new_shape
        self._width = len(new_shape[0])
        self._height = len(new_shape)
        

        

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                # variables.mp.color[j+self._posy][i+self._posx] = 5
                variables.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]
        


class Brick(Object):
    def __init__(self,element,x,y,strength):
        super().__init__(element,x,y)
        self.__strength = strength


    # 1 = strength = 2
    # 2 = strength = 3
    def get_strength(self):
        return self.__strength

    
    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                variables.mp.matrix[j+self._posy][i+self._posx] = ((self._shape[j][i]))
                # if self.__strength == 4:
                #     variables.mp.color[j+self._posy][i+self._posx] = 4
                # elif self.__strength == 3:
                #     variables.mp.color[j+self._posy][i+self._posx] = 3
                # else:
                #     variables.mp.color[j+self._posy][i+self._posx] = 5


                    

class PowerUp(Object):
    def __init__(self,element,x,y):
        super().__init__(element,x,y)
        self._type = element[0][0]
        self._status = 0
        self._time_end = 0
        self._vx = 0
        self._vy = 0

    def get_status(self):
        return self._status

    def set_time_end(self):
        self._time_end = variables.TIME_REM - 20

    def get_type(self):
        return self._type

    def change_status_to_0(self):
        self._status = 0

    def change_status_to_1(self):
        self._status = 1

    def set_vx(self, v):
        self._vx = v

    def set_vy(self, v):
        self._vy = v

    def get_vx(self):
        return self._vx

    def get_vy(self):
        return self._vy

    def inc_vy(self,v):
        self._vy += v

    def y_change_under_gravity(self):
        self._vy -= 0.1
        self._posy -= self._vy



    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                # if variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] == self._type:
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = " "
                # self.change_status_to_0()

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                variables.mp.matrix[int(j+self._posy)][int(i+self._posx)] = self._shape[j][i]


# file.close()


class Bullet(Object):
    def __init__(self,element,x,y):
        super().__init__(element,x,y-2)
        self._type = element[0][0]
        self._status = 1

    def get_status(self):
        return self._status

    def change_status_to_0(self):
        self._status = 0

    def change_status_to_1(self):
        self._status = 1


    def check_collision(self):
        i = int(self._posy)
        j = int(self._posx)

        if(self.y_coord()<5):
            self._status = 0
            self.clear()

        if((variables.mp.matrix[i-1][j] != " " and variables.mp.matrix[i-1][j] != "X" and variables.mp.matrix[i-1][j] != "O")):
            variables.mp.matrix[i-1][j+1] = " "
            variables.mp.matrix[i-1][j-1] = " "
            variables.mp.matrix[i-1][j] = " "
            variables.mp.matrix[i-2][j] = " "
            variables.mp.matrix[i-2][j-1] = " "
            variables.mp.matrix[i-2][j+1] = " "
            variables.mp.matrix[i][j] = " "
            variables.paddle.inc_score(5)
            self._status = 0
            self.clear()


class Ufo(Object):
    def __init__(self,element,x,y):
        super().__init__(element,x,y)
        self._type = element[0][0]
        self._status = 1
        # variables.UFO_FLAG = 1
        self._lives = 5


    def dec_lives(self):
        self._lives -= 1


    def change_status_to_0(self):
        self._status = 0

    def change_status_to_1(self):
        self._status = 1



class Bomb(Object):
    def __init__(self,element,x,y):
        super().__init__(element,x,y)
        self._type = element[0][0]
        self._status = 1

    def change_status_to_0(self):
        self._status = 0

    def change_status_to_1(self):
        self._status = 1

    def get_status(self):
        return self._status


    def check_collision(self):
        if self._status == 1 and self.y_coord() >= variables.paddle.y_coord() - 1 and self.x_coord() >= variables.paddle.x_coord() and self.x_coord() < variables.paddle.x_coord() + variables.paddle.get_width():
            variables.paddle.dec_lives()
            os.system('aplay -q ./sounds/lost_life.wav&')
            self._status = 0
            if variables.paddle.get_lives() <= 0:
                os.system('aplay -q ./sounds/game_over.wav&')
                functions.exit_screen("Lives over!!")
            return 1

        elif self.y_coord() >= variables.paddle.y_coord():
            self._status = 0

        return 0
 