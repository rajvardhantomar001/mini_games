import turtle
import winsound
 
def paddle_a_up(): #defining a function 
    global wn, paddle_a,paddle_b,ball,pen,score_a,score_b
    y= paddle_a.ycor() 
    y+=60
    paddle_a.sety(y)
    
def paddle_a_down(): #defining a function 
    global wn, paddle_a,paddle_b,ball,pen,score_a,score_b
    y= paddle_a.ycor() 
    y-=60
    paddle_a.sety(y)
    
def paddle_b_up(): #defining a function 
    global wn, paddle_a,paddle_b,ball,pen,score_a,score_b
    y= paddle_b.ycor() 
    y+=60
    paddle_b.sety(y)
    
def paddle_b_down(): #defining a function 
    global wn, paddle_a,paddle_b,ball,pen,score_a,score_b
    y= paddle_b.ycor() 
    y-=60
    paddle_b.sety(y)
    
 
def start_rahul():
    global wn, paddle_a,paddle_b,ball,pen,score_a,score_b
    wn= turtle.Screen()
    wn.title("pong by @rahulmishra1402")
    wn.bgcolor("pink")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    #Paddle A
    paddle_a =turtle.Turtle()
    paddle_a.speed(0)#speed of animation not the paddle
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1) #streching the shape
    paddle_a.penup() # makes sure that the moving object that you've created does not draw anything on the window
    paddle_a.goto(-350,0)# paddle starts with -350 in x coordinate

    #Paddle B
    paddle_b =turtle.Turtle()
    paddle_b.speed(0)#speed of animation not the paddle
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1) #streching the shape
    paddle_b.penup() # makes sure that the moving object that you've created does not draw anything on the window
    paddle_b.goto(350,0)# paddle starts with -350 in x coordinate
   
    #ball
    ball=turtle.Turtle()
    ball.speed(0)#speed of animation not the paddle
    ball.shape("circle")
    ball.color("white")
    ball.penup() # makes sure that the moving object that you've created does not draw anything on the window
    ball.goto(0,0)# paddle starts with -350 in x coordinate
    ball.dx = 0.25 #ball will move 2 pixle in positive direction both up and right
    ball.dy = -0.25 #speed of movement of ball is given by dx and dy

    #pen
    pen =turtle.Turtle()
    pen.speed(0) #speed of animation 
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("player A:0 Player B:0",align="center" ,font =("courier",24,"normal"))
    score_a=0
    score_b=0
    wn.listen() #listen foe keyboard inputs
    wn.onkeypress(paddle_a_up,"w")#when user press w paddle gets up by +20)     
    wn.onkeypress(paddle_a_down,"x")
    wn.onkeypress(paddle_b_up,"i")#when user press w paddle gets up by +20)     
    wn.onkeypress(paddle_b_down,"m")
    while True:
        wn.update()  #this is used for updating after every run
        
        #for movving the ball
        ball.setx(ball.xcor() +ball.dx)
        ball.sety(ball.ycor() +ball.dy)
        
        #Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *=-1
            
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *=-1

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *=-1
            winsound.PlaySound('pong.wav ',winsound.SND_ASYNC) 
            score_a +=1
            pen.clear()
            pen.write("player A:{}  Player B: {} ".format(score_a,score_b) ,align="center" ,font =("courier",24,"normal")) 

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *=-1  
            winsound.PlaySound('pong.wav ',winsound.SND_ASYNC)
            score_b +=1
            pen.clear()
            pen.write("player A:{}  Player B: {} ".format(score_a,score_b) ,align="center" ,font =("courier",24,"normal"))

        #paddle and ball collision
        if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
                ball.setx(340)
                ball.dx *= -1 
            
        if (ball.xcor() <-340 and ball.xcor() <-340) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40):
                ball.setx(-340)
                ball.dx *= -1

                