# "Stopwatch: The Game"

# Define global variables

import simplegui

counter = 0
scored = 0
tries = 0
score_monitor = True

# Define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """ Convers time in tenths of seconds into formatted
    string A:BC.D """
    
    global counter, scored, tries
    
    """ Configuration of numbers as they appear on canvas """
    if counter < 10:
        return "0:00." + str(counter)
    
    elif 10 <= counter < 100:
        return "0:0" + str(counter / 10) + "." + str(counter % 10)
    
    elif 100 <= counter < 600:
        return "0:" + str(counter / 10) + "." + str(counter % 10)
    
    elif 600 <= counter < 36000:
        """ Convert tenths of a second into minutes, seconds
        and units of tenth of a second"""
        minutes = counter / 600
        seconds = (counter % 600) / 10
        
        """ Configuration of numbers as they appear on canvas """
        units_tenth_seconds = (counter % 600) % 10
        if seconds < 10:
            return str(minutes) + ":0" + str(seconds) + "." + str(units_tenth_seconds)
        
        elif 10 <= seconds < 60:
            return str(minutes) + ":" + str(seconds) + "." + str(units_tenth_seconds)
    
    elif counter == 36000:
        scored = 0
        tries = 0
        counter = 0
        timer.stop()
        return str(counter)

# Define numerical counters for game
def game_counter(x, y):
    global scored, tries
    return str(scored) + "/" + str(tries)

# Define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global score_monitor
    score_monitor = True
    
def stop():
    timer.stop()
    global scored, tries, counter, score_monitor
    """ Use Boolean variable "score_monitor" to control
    adding points to the score (the score does not
    increment when pressing "Stop" button when 
    counter = 0) """
    if (counter % 10 == 0 and counter != 0 and score_monitor == True):
        scored += 1
        tries += 1
        score_monitor = False
    elif counter == 0:
        scored += 0
        tries += 0
    elif (counter % 10 != 0 and score_monitor == True):
        tries += 1
        score_monitor = False

def reset():
    """ Resets Stopwatch and game """
    global counter, scored, tries
    scored = 0
    tries = 0
    if counter != 0:
        counter = 0
        timer.stop()
        return format(counter)

# Define event handler for timer with 0.1 sec interval
def time_handler():
    global counter
    counter += 1
    return format(counter)

# Define draw handlers
def draw_handler(canvas):
    """ Draws Stopwatch """
    canvas.draw_text(str(format(counter)), (190, 150), 50, "White")
    """ Draws game score """
    canvas.draw_text(str(game_counter(scored, tries)), (420, 50), 40, "Green")

# Create frame and timer
frame = simplegui.create_frame("Stopwatch: The Game", 500, 300)
frame.set_canvas_background("Black")
                
# Register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button("Start", start, 100)
button2 = frame.add_button("Stop", stop, 100)
button3 = frame.add_button("Reset", reset, 100)

# Start frame
frame.start()
