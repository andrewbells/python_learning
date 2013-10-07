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
score1 = 0
score2 = 0
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
right = True
left = False
message = ""

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    pass 
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if right:
        ball_vel[0] = random.randrange(120, 240) / 60
        ball_vel[1] = - random.randrange(60, 180) / 60
    elif not right:
        ball_vel[0] = - random.randrange(120, 240) / 60
        ball_vel[1] = - random.randrange(60, 180) / 60
            
        
# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    pass
    ball_init(right)
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, message
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] + BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT or paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] - BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score2 += 1
            if score2 == 3 and score2 > score1:
                message = "Player2 wins"
            else:
                ball_init(right)
    elif ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] + BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT or paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] - BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score1 += 1
            if score1 == 3 and score1 > score2:
                message = "Player1 wins"
            else:
                ball_init(left)
 
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos - HALF_PAD_HEIGHT <= 0:
        paddle1_pos = HALF_PAD_HEIGHT
    if paddle2_pos - HALF_PAD_HEIGHT <= 0:
        paddle2_pos = HALF_PAD_HEIGHT
    if paddle1_pos + HALF_PAD_HEIGHT >= HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos + HALF_PAD_HEIGHT >= HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    # canvas.draw_polygon(point_list, line_width, line_color, fill_color=None)
    # canvas.draw_line((10, 20), (80, 40), 12, "Blue")
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "Pink")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball and scores
    # canvas.draw_circle(center_point, radius, line_width, line_color, fill_color=None)
    c.draw_circle(ball_pos, BALL_RADIUS, 1,"White", "White")
    # canvas.draw_text(text, point, font_size, font_color)
    c.draw_text(str(score1), [WIDTH / 2 - 70, 50], 48, "Pink")
    c.draw_text(str(score2), [WIDTH / 2 + 50, 50], 48, "White")
    c.draw_text(message, [50, HEIGHT / 2], 100, "Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()