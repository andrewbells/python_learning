# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
guessed_num = 0
output = ""
num_tries = 0
ini_num_tries = 0

# define event handlers for control panel
def init():
    f.start()
    range100()
    
def range100():
    global guessed_num, output, num_tries, ini_num_tries
    guessed_num = random.randrange(0, 101)
    # 2 ** n >= high - low + 1
    num_tries = ini_num_tries = math.ceil(math.log(101 - 0 + 1, 2))
    output = "New game. Range  0 - 100. You have " + str(num_tries) + " tries."
    print output
    # button that changes range to range [0,100) and restarts

def range1000():
    global guessed_num, output, num_tries, ini_num_tries
    guessed_num = random.randrange(0, 1001)
    # 2 ** n >= high - low + 1
    num_tries = ini_num_tries = math.ceil(math.log(1001 - 0 + 1, 2))
    output = "New game. Range 0 - 1000. You have " + str(num_tries) + " tries."
    print output
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
    global output, num_tries
    if float(guess) > guessed_num and num_tries > 1:
        num_tries -= 1
        output = "You choose " + str(guess) + ". Lower! You have " + str(num_tries) + " tries."
        print output
    elif float(guess) < guessed_num and num_tries > 1:
        num_tries -= 1
        output = "You choose " + str(guess) + ". Higher! You have " + str(num_tries) + " tries."
        print output
    elif float(guess) == guessed_num:
        num_tries -= 1
        output = "You choose " + str(guess) + ". Correct! You've guessed with " + str(ini_num_tries - num_tries) + " tries."
        print output
        init()
    else:
        print "You lose:("
        init()
    # main game logic goes here	
    
def draw(canvas):
    canvas.draw_text(output, [10, 10], 12, "Red")

    
# create frame
f = simplegui.create_frame("Guess the Number Game", 200, 200)

# register event handlers for control elements
f.add_button("Range 0 - 100", range100, 200)
f.add_button("Range 0 - 1000", range1000, 200)
f.add_input("Your guess", get_input, 200)
f.set_draw_handler(draw)


# start frame

init()

# always remember to check your completed program against the grading rubric
