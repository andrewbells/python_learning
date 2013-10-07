# implementation of card game - Memory

import simplegui
import random

deck = []
exposed = []
state = 0
clicked_1 = 16
clicked_2 = 16
moves = 0

# helper function to initialize globals
def init():
    global deck, num, exposed, moves, clicked_1, clicked_2
    deck = [x % 8 for x in range(16)]
    random.shuffle(deck)
    exposed = [False for i in range(16)]
    state = 0
    moves = 0
    clicked_1 = 0
    clicked_2 = 0
         
# define event handlers
def mouseclick(pos):
    global exposed, state, clicked_1, clicked_2, moves
    if state == 0:
        for i in range(16):
            if pos[0] > i * 46 and pos[0] < 46 + i * 46 and exposed[i] == False:
                exposed[i] = True
                clicked_1 = i
                state = 1
                # print "st0", clicked_1, clicked_2
                moves += 1
    elif state == 1:
        for i in range(16):
            if pos[0] > i * 46 and pos[0] < 46 + i * 46 and exposed[i] == False:
                exposed[i] = True
                clicked_2 = clicked_1
                clicked_1 = i
                state = 2
                # print "st1", clicked_1, clicked_2
                # moves += 1
    else:
        for i in range(16):
            if pos[0] > i * 46 and pos[0] < 46 + i * 46 and exposed[i] == False:
                exposed[i] = True
                if deck[clicked_1] == deck[clicked_2]:
                    clicked_2 = clicked_1
                    clicked_1 = i
                    state = 1
                    # print "st2", clicked_1, clicked_2
                else:
                    exposed[clicked_1] = False
                    exposed[clicked_2] = False
                    clicked_2 = clicked_1
                    clicked_1 = i
                    state = 1
                    # print "st2f", clicked_1, clicked_2
                moves += 1
                                 
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed, moves
    l.set_text("Moves " + str(moves))
    
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([(i * 46, 0), (i * 46, 100), (46 + i * 46, 100), (46 + i * 46, 0)], 1, "Black", "Green")
        else:
            canvas.draw_text(str(deck[i]), [8 + i * 46, 70], 68, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 736, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric