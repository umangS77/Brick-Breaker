import board
import objects
import config 

mp = board.Map()



ORG_BALL_SPEED_X = 0.2
ORG_BALL_SPEED_Y = 0.2
PADDLE_SPEED = 0.3

BALL_SPEED_X = ORG_BALL_SPEED_X
BALL_SPEED_Y = ORG_BALL_SPEED_Y

BONUS_ROW = 0
BONUS_COLUMN = 0

message = ""

TIME_REM = 0
TIME_BEGUN = 0
TIME_TOTAL = 100
LAST_TIME = 0

POWERUP_TIME_FAST = -1
POWERUP_TIME_THROUGH = -1
POWERUP_TIME_SHRINK = -1
POWERUP_TIME_EXPAND = -1
POWERUP_TIME_FIREBALL = -1
POWERUP_TIME_SHOOT = -1

FIREBALL_FLAG = 0
SHOOT_FLAG = 0
POWERUP_DURATION = 20

LEVEL = 1
LEVEL_CHANGE_FLAG = 0
BRICK_DROP = 0
BRICK_FALL_TIME = 40



paddle_base = mp.height - len(config.paddle) - 3
paddle_start = 50
# paddle_length = len(config.paddle)
paddle = objects.Paddle(config.paddle, paddle_start, paddle_base, config.lives)
ball_base = paddle_base-1
ball_start = paddle_start + 3
ball = objects.Ball(config.ball, ball_start, ball_base)

# powerups = ["?", "@", "U", "<", ">"] # fast through grab expand shrink

powerups = []

powerups_index = []

bricks = []




