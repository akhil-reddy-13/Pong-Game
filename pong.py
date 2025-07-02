import turtle
single_player_mode = False  # set to False for 2 players | set to True for 1 player

# background
bg = turtle.Screen()
bg.title("Pong")
bg.bgcolor("black")
bg.bgpic("Turtle Projects/Pong/retrobg.gif")
bg.setup(width = 800, height = 600)
bg.tracer(0)  # sets the background before showing it to Player

# starting settings
score_a = 0
score_b = 0
paused = True
started = False

# intro screen
intro = turtle.Turtle()
intro.penup()
intro.hideturtle()
intro.color("white")
intro.goto(0, 0)
intro.write("Welcome to Pong!\nW/S = Left Paddle\n↑/↓ = Right Paddle\nP = Pause | R = Restart\nPress SPACE to Start", align="center", font=("Courier", 18, "bold"))

# paddle of user a
paddle_a = turtle.Turtle()
paddle_a.goto(-350, 0)
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(6, 1) #width (vertical), length (horizontal)
paddle_a.penup()

# paddle of user b
paddle_b = turtle.Turtle()
paddle_b.goto(350, 0)
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(6, 1) #width (vertical), length (horizontal)
paddle_b.penup()

# ball
ball = turtle.Turtle()
ball.goto(0, 0)
ball.speed(0)
ball.shape("circle")
ball.color("white", "red")
ball.penup()
ball.dx = 2
ball.dy = -2

# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("gold")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

# paddle movement
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 220:
        paddle_a.sety(y + 30)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -220:
        paddle_a.sety(y - 30)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 220:
        paddle_b.sety(y + 30)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -220:
        paddle_b.sety(y - 30)

# pause feature
def toggle_pause():
    global paused
    paused = not paused

# 'SPACE' to start game
def start_game():
    global started, paused
    started = True
    paused = False
    intro.clear()

# restart game
def restart_game():
    global score_a, score_b, game_over
    score_a = 0
    score_b = 0
    ball.goto(0, 0)
    ball.showturtle()
    ball.dx = 2
    ball.dy = -2
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    pen.clear()
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))
    game_over = False

# key bindings
bg.listen()
bg.onkeypress(paddle_a_up, "w")
bg.onkeypress(paddle_a_down, "s")
bg.onkeypress(paddle_b_up, "Up")
bg.onkeypress(paddle_b_down, "Down")
bg.onkeypress(restart_game, "r")
bg.onkeypress(toggle_pause, "p")
bg.onkeypress(start_game, "space")


game_over = False

# gameplay
while True: 
    bg.update()
    if game_over or paused or not started:
        continue

    if single_player_mode:
        # ai paddle A follows the ball
        paddle_a.color("cyan")
        if paddle_a.ycor() < ball.ycor() and paddle_a.ycor() < 250:
            paddle_a.sety(paddle_a.ycor() + 2)
        elif paddle_a.ycor() > ball.ycor() and paddle_a.ycor() > -250:
            paddle_a.sety(paddle_a.ycor() - 2)

    # moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right wall (A score)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

    # left wall (B score)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))

    # ball hits B paddle
    if (330 < ball.xcor() < 350) and (paddle_b.ycor() - 80 < ball.ycor() < paddle_b.ycor() + 80):
        ball.setx(330)
        ball.dx *= -1.05

    # ball hits A paddle
    if (-350 < ball.xcor() < -330) and (paddle_a.ycor() - 80 < ball.ycor() < paddle_a.ycor() + 80):
        ball.setx(-330)
        ball.dx *= -1.05

    # end game
    if score_a == 11:
        pen.clear()
        pen.write(f"Player A won!", align="center", font=("Courier", 24, "bold"))
        ball.hideturtle()
        ball.dx = 0
        ball.dy = 0
        game_over = True

    if score_b == 11:
        pen.clear()
        pen.write(f"Player B won!", align="center", font=("Courier", 24, "bold"))
        ball.hideturtle()
        ball.dx = 0
        ball.dy = 0
        game_over = True
