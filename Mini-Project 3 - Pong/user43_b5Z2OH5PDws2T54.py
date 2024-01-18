# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    # The draw handler runs 60 times a second.
    # This means that if the velocity is wanted to be 
    # A pixels per second, it has to be written as 
    # A / 60 in this function because the draw handler
    # is the function that actualizes the value of the
    # variable ball_vel:
    ball_vel = [random.randrange(120 / 60, 240 / 60), 
                - random.randrange(60 / 60 , 180 / 60)]
    
    if direction == RIGHT:
        ball_vel[0] = ball_vel[0]
    elif direction == LEFT:
        ball_vel[0] = - ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0

    return spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # collide and reflect off of upper side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of lower side of canvas
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    if paddle1_pos <= 0:
        paddle1_pos = 0
    elif paddle1_pos >= HEIGHT - PAD_HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT
    paddle2_pos += paddle2_vel
    if paddle2_pos <= 0:
        paddle2_pos = 0
    elif paddle2_pos >= HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
    
    # draw paddles
        # left-hand side paddle
    canvas.draw_polygon([[0, paddle1_pos],
                        [PAD_WIDTH, paddle1_pos],
                        [PAD_WIDTH, paddle1_pos + PAD_HEIGHT],
                        [0, paddle1_pos + PAD_HEIGHT]],
                        1, 'White', 'White')
        # right-hand side paddle
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos],
                         [WIDTH, paddle2_pos],
                         [WIDTH, paddle2_pos + PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]],
                        1, 'White', 'White')
    
    # determine whether paddle and ball collide
        # collide with left-hand side paddle
    if (ball_pos[0] - BALL_RADIUS <= PAD_WIDTH) and (paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
        ball_vel[0] = - (11 * ball_vel[0] / 10)    
        # collide with right-hand side paddle
    elif (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH) and (paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
        ball_vel[0] = - (11 * ball_vel[0] / 10)
       
        # collide with gutters
            # collide with left-hand side gutter
    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        ball_pos[0] = WIDTH / 2
        ball_pos[1] = HEIGHT / 2
        score2 += 1
        return spawn_ball(RIGHT)
            # collide with right-hand side gutter
    elif ball_pos [0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        ball_pos[0] = WIDTH / 2
        ball_pos[1] = HEIGHT / 2
        score1 += 1
        return spawn_ball(LEFT)
       
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, HEIGHT / 8], 22, 'White')
    canvas.draw_text(str(score2), [3 * WIDTH / 4, HEIGHT / 8], 22, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    # control upward motion of paddles
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = - 12
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = - 12
    # control downward motion of paddles
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 12
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 12

def keyup(key):
    global paddle1_vel, paddle2_vel
    # control upward motion of paddles
    paddle1_vel = 0
    paddle2_vel = 0

# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# Callback event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game, 100)

# start frame
new_game()
frame.start()