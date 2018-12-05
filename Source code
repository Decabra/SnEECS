''' World's Best Ever Snake Game: SnEEcs '''


import turtle
import time
import random
# variables
delay = 0.1
score = 0
HighScore = 0
# Screen of the snake game 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgpic("Box 4.gif")
wn.setup(width=590, height=590)
wn.tracer(0)
# Snake head 
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'
# Food of Snake 
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)
# Score Turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.shape('square')
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write('Score: 0 High Score: 0', align = 'center', font = ('courier', 24, 'bold'))

# Functions to orient direction
def GoUp():
    if head.direction != 'down':
        head.direction = 'up'
def GoDown():
    if head.direction != 'up':
        head.direction = 'down'
def GoRight():
    if head.direction != 'left':
        head.direction = 'right'
def GoLeft():
    if head.direction != 'right':
        head.direction = 'left'
# Function to move the snake 
def move():
    if head.direction == 'up':
        y=head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y=head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x=head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x=head.xcor()
        head.setx(x - 20)
# Keyboard Binding
wn.listen()
wn.onkeypress(GoUp,'Up')
wn.onkeypress(GoDown,'Down')
wn.onkeypress(GoRight,'Right')
wn.onkeypress(GoLeft,'Left')

segments = []


# Main game Loop
while True:
    wn.update()
    # Check for Border collisions
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(0.8)
        head.goto(0,0)
        head.direction = 'stop'
        # Score Reset
        pen.clear()
        score = 0
        pen.write('Score: {} High Score: {}'.format(score, HighScore), align = 'center', font = ('courier', 24, 'bold'))
        # Hide the all cleared segments of the snake body
        for segment in segments:
            segment.hideturtle()
        segments.clear()
        # Reset the Delay
        delay = 0.1
            
    # Check the food to move it randomly on the screen
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        # Creates a new turtle object when snake eat its food
        Newsegment = turtle.Turtle()
        Newsegment.shape('circle')
        Newsegment.color('grey')
        Newsegment.speed(0)
        Newsegment.penup()
        segments.append(Newsegment)
        # To avoid game slowu=ing down
        delay -= 0.001 
        # Update score when snake hit food
        pen.clear()
        score += 10
        if score > HighScore:
            HighScore = score
        pen.write('Score: {} High Score: {}'.format(score, HighScore), align = 'center', font = ('courier', 24, 'bold'))
        

    # Move the end snake body segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    # Die the snake if he collides with its body
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(0.8)
            head.goto(0,0)
            head.direction = 'stop'
            # Hide the all cleared segments of the snake body
            for segment in segments:
                segment.hideturtle()    
            segments.clear()
            
            # Reset the delay
            delay = 0.1
            
            # Score Reset
            pen.clear()
            score = 0
            pen.write('Score: {} High Score: {}'.format(score, HighScore), align = 'center', font = ('courier', 24, 'bold'))
            
    time.sleep(delay)
wn.mainloop()
