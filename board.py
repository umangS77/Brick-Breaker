import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import variables
import os
import sys
import termios, tty, time

class Map(object):

    height = int(config.rows) 
    width = int(config.columns*8)

    def __init__(self):
        self.matrix = np.array([[" " for x in range(self.width)] for y in range(self.height)])
        for x in range(self.width):
            self.matrix[3][x] = "X"
        for i in range(self.width):
            self.matrix[self.height - 1][i] = "X"
        self.start_index = 0

    def render(self):
        lev_flag = 0
        # rainbow = random.randint(10)
        for i in range(3,self.height):
            board = []
            for j in range(0, config.columns):
                if i == variables.paddle_base + 1:
                    self.matrix[i][j] = " "
                if i == 3 or i == self.height - 1:
                    board.append(Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                # elif i == self.height - 1:
                #     board.append(Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                elif self.matrix[i][j] == " " or self.matrix[i][j] == "O":
                    board.append(self.matrix[i][j])

                elif self.matrix[i][j] == "Z":
                    self.matrix[i][j] = "z"
                    board.append(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                
                elif self.matrix[i][j] == "z":
                    self.matrix[i][j] = "y"
                    board.append(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                elif self.matrix[i][j] == "y":
                    self.matrix[i][j] = "Z"
                    board.append(Fore.LIGHTGREEN_EX + Back.LIGHTGREEN_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))








                
                elif self.matrix[i][j] == "L":
                    self.matrix[i][j+1] = "E"
                    self.matrix[i+1][j+1] = "1"
                    self.matrix[i+1][j] = "V"
                    lev_flag = 1
                    board.append(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                        
                elif self.matrix[i][j] == "E":
                    self.matrix[i][j-1] = "L"
                    self.matrix[i+1][j-1] = "V"
                    self.matrix[i+1][j] = "1"
                    lev_flag = 1
                    board.append(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                elif self.matrix[i][j] == "V" or self.matrix[i][j] == "1":
                    lev_flag = 1
                    board.append(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                #     self.matrix[i][j+1] = "1"
                #     self.matrix[i-1][j+1] = "E"
                #     self.matrix[i-1][j] = "L"

                # elif self.matrix[i][j] == "1":
                #     board.append(Fore.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j-1] = "V"
                #     self.matrix[i-1][j-1] = "L"
                #     self.matrix[i-1][j] = "E"  

                elif self.matrix[i][j] == "l":
                    self.matrix[i][j+1] = "e"
                    self.matrix[i+1][j+1] = "2"
                    self.matrix[i+1][j] = "v"
                    lev_flag = 1
                    board.append(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                elif self.matrix[i][j] == "e":
                    self.matrix[i][j-1] = "l"
                    self.matrix[i+1][j-1] = "v"
                    self.matrix[i+1][j] = "2"
                    lev_flag = 1
                    board.append(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                elif self.matrix[i][j] == "v" or self.matrix[i][j] == "2":
                    lev_flag = 1
                    board.append(Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j+1] = "2"
                #     self.matrix[i-1][j+1] = "e"
                #     self.matrix[i-1][j] = "l"

                # elif self.matrix[i][j] == "2":
                #     board.append(Fore.LIGHTYELLOW_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j-1] = "v"
                #     self.matrix[i-1][j-1] = "l"
                #     self.matrix[i-1][j] = "e"

                elif self.matrix[i][j] == "F":
                    self.matrix[i][j+1] = "I"
                    self.matrix[i+1][j+1] = "A"
                    self.matrix[i+1][j] = "N"
                    lev_flag = 1
                    board.append(Fore.LIGHTGREEN_EX + Back.LIGHTGREEN_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                elif self.matrix[i][j] == "I":
                    self.matrix[i][j-1] = "F"
                    self.matrix[i+1][j-1] = "N"
                    self.matrix[i+1][j] = "A"
                    lev_flag = 1
                    board.append(Fore.LIGHTGREEN_EX + Back.LIGHTGREEN_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                
                elif self.matrix[i][j] == "N" or self.matrix[i][j] == "A":
                    lev_flag = 1
                    board.append(Fore.LIGHTGREEN_EX + Back.LIGHTGREEN_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))


                # elif self.matrix[i][j] == "N":
                #     board.append(Fore.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j+1] = "A"
                #     self.matrix[i-1][j+1] = "I"
                #     self.matrix[i-1][j] = "F"

                # elif self.matrix[i][j] == "A":
                #     board.append(Fore.LIGHTRED_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j-1] = "N"
                #     self.matrix[i-1][j-1] = "F"
                #     self.matrix[i-1][j] = "I"

                elif self.matrix[i][j] == "R":
                    self.matrix[i][j+1] = "0"
                    self.matrix[i+1][j+1] = "K"
                    self.matrix[i+1][j] = "C"
                    lev_flag = 1
                    board.append(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                elif self.matrix[i][j] == "0":
                    self.matrix[i][j-1] = "R"
                    self.matrix[i+1][j-1] = "C"
                    self.matrix[i+1][j] = "K"
                    lev_flag = 1
                    board.append(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                elif self.matrix[i][j] == "C" or self.matrix[i][j] == "K":
                    lev_flag = 1
                    board.append(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j+1] = "K"
                #     self.matrix[i-1][j+1] = "0"
                #     self.matrix[i-1][j] = "R"

                # elif self.matrix[i][j] == "K":
                #     board.append(Fore.LIGHTBLACK_EX + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    
                #     self.matrix[i][j-1] = "C"
                #     self.matrix[i-1][j-1] = "R"
                #     self.matrix[i-1][j] = "0"                      
                        
                elif self.matrix[i][j] == "O" or self.matrix[i][j] == "?" or self.matrix[i][j] == ">" or self.matrix[i][j] == "<" or self.matrix[i][j] == "@" or self.matrix[i][j] == "G" or self.matrix[i][j] == "|":        
                    board.append(Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))

                elif self.matrix[i][j] == "#":
                    # board.append(Fore.WHITE + Back.WHITE + Style.BRIGHT+(self.matrix[i][j] + Style.RESET_ALL))
                    lev_flag = 1
                    board.append(Back.WHITE + (self.matrix[i][j] + Style.RESET_ALL))

                elif self.matrix[i][j] == ".":
                    board.append(Fore.LIGHTRED_EX + (self.matrix[i][j] + Style.RESET_ALL))

                elif variables.mp.start_index <= 981:
                    if j >= variables.paddle._posx and j < variables.paddle._posx +  variables.paddle.get_width():
                        if i >= variables.paddle._posy:
                            if i < variables.paddle._posy + variables.paddle._height:
                                z=0
                                if variables.SHOOT_FLAG == 1 and  ((self.matrix[i][j] == "/" and (self.matrix[i][j-1] == " " or self.matrix[i][j-1] == "")) or (self.matrix[i][j] == "/" and (self.matrix[i][j+1] == " " or self.matrix[i][j+1] == ""))): 
                                    board.append(Fore.LIGHTRED_EX + Back.LIGHTRED_EX + (self.matrix[i][j] + Style.RESET_ALL))
                                else:
                                    board.append(Fore.LIGHTCYAN_EX + Back.LIGHTCYAN_EX + (self.matrix[i][j] + Style.RESET_ALL))




            # if lev_flag == 0:
            #     variables.LEVEL_CHANGE_FLAG = 1
            # else:
            print(''.join(board))
        if lev_flag == 0:
                variables.LEVEL_CHANGE_FLAG = 1


    
        
        



    