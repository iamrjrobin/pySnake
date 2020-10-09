import random
import curses

sur = curses.initscr()
curses.curs_set(0)

sH , sW = sur.getmaxyx()
window = curses.newwin(sH, sW , 0, 0)
window.keypad(1)
window.timeout(100)

snk_x = sW/4
snk_y = sH/2

snake = [

    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2],

]

food = [sH/2, sW/2]

window.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sH] or snake [0][1] in [0, sW] or snake [0] in snake [1:]:
        curses.endwin()
        quit()
    
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)


    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sH-1),
                random.randint(1, sW-1)
            ]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')
    
    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)