# "Guess the Number" Mini-project 2

import simplegui
import math
import random

num_range = 100

# Helper function to start and restart the game
def new_game():
    # Initializing global variables
    global num_range
    
    global secret_number
    secret_number = random.randrange(0, num_range)

    global n # Number of remaining guesses
    n = int(math.ceil((math.log(num_range - 0 + 1)) / (math.log(2))))
    
    # Printing message
    print "New game. Range is [0, " + str(num_range) + ")"
    print "Number of remaining guesses is 7"
    print

    
# Define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print "-----------------------"
    print "New game. Range is [0, 100)"
    print "Number of remaining guesses is 7"
    print
    
    # Initializing global variables
    global secret_number
    secret_number = random.randrange(0, 100)
    
    global num_range
    num_range = 100
    
    global n
    n = int(math.ceil((math.log(num_range - 0 + 1)) / (math.log(2))))
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    print "-----------------------"
    print "New game. Range is [0, 1000)"
    print "Number of remaining guesses is 10"
    print
    
    # Initializing global variables
    global secret_number
    secret_number = random.randrange(0, 1000)
    
    global num_range
    num_range = 1000
    
    global n
    n = int(math.ceil((math.log(num_range - 0 + 1)) / (math.log(2))))
    
def input_guess(guess):
    # main game logic goes here	
    # Calling global variables
    global secret_number
    guess = int(guess)
    
    global n
    n = n - 1
    
    print "Your guess is", guess
    print "Number of remaining guesses is", n
    
    # Set results
    lose = (n == 0)
    correct = (guess == secret_number)
    higher = (guess < secret_number)
    lower = (guess > secret_number)
    
    # Guessing answers
    if lose:
        if correct:
            print "Correct!"
            print
            print "-----------------------"
            return new_game()
        else:
            print "Out of tries. You lose"
            print "The secret number is", secret_number
            print
            print "-----------------------"
            return new_game()
    elif correct:
        print "Correct!"
        print
        print "-----------------------"
        return new_game()
    elif higher:
        print "Higher!"
    elif lower:
        print "Lower!"
        
    print

# Create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# Register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter your guess", input_guess, 200)

# Call new_game 
new_game()