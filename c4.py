# small turtle program provied a graphical interface for your connect 4 code (connect4.py)

import turtle
import connect4

nCols, nRows = 7,6
window_width, window_height = nCols*100, nRows*100

screen = turtle.Screen()
screen.setup(window_width, window_height)
screen.title("Connect4!")
screen.setworldcoordinates(-1,-1,nCols+1,nRows+1)
screen.bgcolor('light gray')
screen.tracer(0,0)

turtle.hideturtle()


def draw_board(grid):
    # board itself
    turtle.pencolor('royal blue')
    turtle.fillcolor('royal blue')
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.seth(0)
    for _ in range(2):
        turtle.forward(nCols)
        turtle.left(90)
        turtle.forward(nRows)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

    # holes & checkers
    for r in range(nRows):
        for c in range(nCols):
            draw_checker(c,nRows - r -1, grid[r][c])


def draw_checker(x,y,colour='white'):
    if colour == 'empty': colour = 'white'
    turtle.up()
    turtle.goto(x+0.5,y+0.05)
    turtle.seth(0)
    turtle.begin_fill()
    turtle.fillcolor(colour)
    turtle.color(colour)
    turtle.down()
    turtle.circle(0.45, steps=100)
    turtle.end_fill()

def draw(b):
    draw_board(b)
    screen.update()
    
def play(x,y):
    global turn
    global grid
    global player

    print(f"({x:+5.3},{y:+5.3}) ", end='')
    if x < 0 or int(x) > nCols:
        print('  - mouse not over board')
        return

    col = int(x)
    #print(col)
    if not connect4.play(grid, col, player[0]):
        print('  - not a valid play')
        return
    print(f'  - play {player[0]} in column {col}')
    

    draw(grid)

    win = connect4.win(grid, col)

    if win == 'empty':
        if player[0] == 'red':
            player[0] = 'black'
        else:
            player[0] = 'red'
        return

    # someone won!
    print( f'WINNER!!  {player[0]} is the winner!' )
    again = ""
    while again.lower() not in ['yes','no']:
        again = screen.textinput(f"Winner is {player[0]}", "Play again? yes/no")
    if again == 'yes':
        grid = connect4.makeGrid()
        draw(grid)
    else:
        print('game exiting')
        turtle.bye()


grid = connect4.makeGrid(nRows , nCols)   
player = ['red']
c = nCols//2
draw(grid)

screen.onclick(play)

turtle.mainloop()
