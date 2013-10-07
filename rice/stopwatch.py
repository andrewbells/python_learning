# template for "Stopwatch: The Game"

import simplegui

# define global variables
width = 300
height = 300
val = 0
stopped = 0
guessed = 0
started = False

# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(val):
    a = val // 600
    b = (val - a * 600) // 100
    c = (val - a * 600) // 10 - b * 10
    d = (val - a * 600) % 10
    
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    started = True
    timer.start()
    
def stop():
    global guessed, stopped, started
    timer.stop()
    if val % 10 == 0 and started == True:
        guessed += 1
        stopped += 1
        started = False
    elif started == True:
        stopped += 1
        started = False
        
def reset():
    global val, guessed, stopped
    timer.stop()
    val = 0
    guessed = 0
    stopped = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global val
    val += 1
   
def draw(canvas):
    canvas.draw_text(format(val), [100, 150], 28, "White")
    canvas.draw_text(str(guessed) + "/" + str(stopped), [250, 40], 24, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start timer and frame
frame.start()
# remember to review the grading rubric