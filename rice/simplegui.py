# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter = counter + 1

# Define event handler functions
def tick():
    increment()
    print counter
    
def buttonpress():
    global counter
    counter = 0
    
def draw(canvas):
    canvas.draw_text(str(counter), [50,50], 36, "Red")

# Create a frame
frame = simplegui.create_frame("SimpleGUI test", 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me!", buttonpress)
frame.set_draw_handler(draw)

# Start frame and timers
frame.start()
timer.start()


