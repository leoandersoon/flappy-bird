import turtle, time, random

window = turtle.Screen()
canvas = window.getcanvas()
root = canvas.winfo_toplevel()
window.title('Flappy Bird')
window.bgcolor('blue')
window.bgpic('background.gif')
window.setup(width=500, height=700)
window.tracer(0)

window.register_shape('bird.gif')

bird = turtle.Turtle()
bird.speed(0)
bird.color('yellow')
bird.shape('bird.gif')
bird.penup()
bird.goto(-180, 0)
bird.dx = 0
bird.dy = 1

score = 100
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color('white')
score_board.shape('square')
score_board.hideturtle()
score_board.penup()
score_board.goto(0, 300)
score_board.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'bold'))

gravity = -0.3

def bird_up(x, y):
    bird.dy = bird.dy + 8

    if bird.dy > 8:
        bird.dy = 8

def close():
    global devam
    devam = False

pipes = []
window.listen()
window.onscreenclick(bird_up)
root.protocol("WM_DELETE_WINDOW", close)
continuation = True

starting_time = time.time()
while continuation:
    time.sleep(0.02)
    window.update()

    bird.dy = bird.dy + gravity

    if (time.time() - starting_time > random.randint(5, 15)):
        starting_time = time.time()
        pipe_up = turtle.Turtle()
        pipe_up.speed(0)
        pipe_up.color('red')
        pipe_up.shape('square')
        pipe_up.h = random.randint(10, 20)
        pipe_up.shapesize(pipe_up.h, 2, outline=None)
        pipe_up.penup()
        pipe_up.goto(300, 250)
        pipe_up.dx = -2
        pipe_up.dy = 0

        pipe_down = turtle.Turtle()
        pipe_down.speed(0)
        pipe_down.color('red')
        pipe_down.shape('square')
        pipe_down.h = 40 - pipe_up.h - random.randint(1, 10)
        pipe_down.shapesize(pipe_down.h, 2, outline=None)
        pipe_down.penup()
        pipe_down.goto(300, -250)
        pipe_down.dx = -2
        pipe_down.dy = 0

        pipes.append((pipe_up, pipe_down))


    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)

    if len(pipes) > 0:
        for pipe in pipes:
            x = pipe[0].xcor()
            x = x + pipe[0].dx
            pipe[0].setx(x)
            x = pipe[1].xcor()
            x = x + pipe[1].dx
            pipe[1].setx(x)
            if pipe[0].xcor() < -300:
                pipe[0].hideturtle()
                pipe[1].hideturtle()
                pipes.pop(pipes.index((pipe)))
            if (bird.xcor()+10>pipe[0].xcor()-20) and (bird.xcor()-10<pipe[0].xcor()+20):
                if (bird.ycor()+10>pipe[0].ycor()-pipe[0].h*10) or (bird.ycor()-10<pipe[1].ycor()+pipe[1].h*10):
                    score = score - 1
                    score_board.clear()
                    score_board.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'bold'))

    if score< 0:
        score_board.clear()
        score_board.write('You Lost!', align='center', font=('Courier', 24, 'bold'))