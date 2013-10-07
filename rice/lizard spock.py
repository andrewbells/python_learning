# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else:
        return "None"
    

    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    if name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else:
        return "None"


    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(guess): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(guess)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if difference >=3:
        victory = "Computer wins"
    elif difference > 0 and difference <=2:
        victory = "Player wins"
    else:
        victory = "Player and computer tie!"
    print "Player chooses " + guess
    print "Computer chooses " + number_to_name(comp_number)
    print victory
    print ""
       
    # convert comp_number to name using number_to_name
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


