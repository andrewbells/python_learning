
import simplegui

image = simplegui.load_image("https://dl-web.dropbox.com/get/pics/spaceinvaders.gif?w=AACSQ3b2hR-VsobM1-sFAd8DJPkQSaZpdi2zB0HUG_0ZSw")

# Handler for mouse click


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_image(image, (100,100), (100,100), (100,100), (100,100))

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 600)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
