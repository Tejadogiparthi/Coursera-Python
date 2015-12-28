# template for "Stopwatch: The Game"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
Counter, Total, Good = 0, 0, 0
Timer, stopscore = "", ""
Running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    lastSec, t = t%10, t//10
    middleSec2, t = t%10, t//10
    firstSec1, Min = t%6, t//6
   # print "%1d:%1d%1d.%1d" % (Min, firstSec1, middleSec2, lastSec)
    return str(Min)+":"+str(firstSec1)+str(middleSec2)+"."+str(lastSec)

def Score():
    return str(Good) + "/" + str(Total)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global Running
    timer.start()
    Running = True

def stop():
    global Running, Total, Good
    timer.stop()
    #print Running
    if Running:
        Total += 1
        if Counter%10 == 0:
            Good += 1
    Running = False

def reset():
    global Running, Counter, Total, Good
    timer.stop()
    Counter, Total, Good = 0, 0, 0
    Running = False

# define event handler for timer with 0.1 sec interval
def tick():
    global Counter
    Counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(Counter), [60, 85], 36, "White")
    canvas.draw_text(Score(), [155, 25], 26, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
