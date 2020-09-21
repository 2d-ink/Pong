import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Points for score board
score_a = 0
score_b = 0

#Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation
paddle_a.shape("square") #shape of paddle 
paddle_a.color("white") #color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #make paddle longer
paddle_a.penup()
paddle_a.goto(-350, 0) #paddle A will start on the left side -350

#Paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation
paddle_b.shape("square") #shape of paddle 
paddle_b.color("white") #color of the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #make paddle longer
paddle_b.penup()
paddle_b.goto(350, 0) #paddle A will start on the right side 350

#Ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation
ball.shape("square") #shape of ball 
ball.color("white") #color of the ball
ball.penup()
ball.goto(0, 0) #ball A will start on the middle
ball.dx = 2 #move ball x cordinate, 2 pixel
ball.dy = 2 #move ball y cordinate, 2 pixel

#score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Palyer A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()#cordinate of paddle a 
    y += 20 #add 20 pixel up on y cordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()#cordinate of paddle a 
    y -= 20 #subtract 20 pixel down on y cordinate
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()#cordinate of paddle a 
    y += 20 #add 20 pixel up on y cordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()#cordinate of paddle a 
    y -= 20 #subtract 20 pixel down on y cordinate
    paddle_b.sety(y)

#Keyboard listening
win.listen()
win.onkeypress(paddle_a_up, "w") #move paddle A up using key w
win.onkeypress(paddle_a_down, "x") #move paddle A down using key x
win.onkeypress(paddle_b_up, "Up") #moving paddle b up using arrow key up
win.onkeypress(paddle_b_down, "Down") #moving paddle b down using arrow key down


#Game loop
while True:
    win.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border  checking prevent call from going off the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)#set the ball back to center
        ball.dx *= -1
        score_a += 1 #score
        pen.clear() #clear the score and print new score
        pen.write("Palyer A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0) #set the ball back to center
        ball.dx *= -1
        score_b += 1 #score
        pen.clear() #clear the score and print new score
        pen.write("Palyer A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and Ball 
    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor()< -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1