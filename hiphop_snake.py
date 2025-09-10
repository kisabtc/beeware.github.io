import curses
import random
import time

# Hip Hop Snake Game
# Use arrow keys to move.
# Collect records to grow and keep the beat going!

EMOJI_SNAKE_HEAD = '😎'
EMOJI_SNAKE_BODY = '🧢'
EMOJI_RECORD = '💿'


def create_food(snake, screen_height, screen_width):
    while True:
        food = [
            random.randint(1, screen_height - 2),
            random.randint(1, screen_width - 2)
        ]
        if food not in snake:
            return food


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    direction = curses.KEY_RIGHT
    food = create_food(snake, sh, sw)
    score = 0

    while True:
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(0, 2, ' Yo! Hip Hop Snake ')
        stdscr.addstr(0, sw - 15, f'Score: {score}')

        stdscr.addstr(food[0], food[1], EMOJI_RECORD)
        for idx, part in enumerate(snake):
            char = EMOJI_SNAKE_HEAD if idx == 0 else EMOJI_SNAKE_BODY
            stdscr.addstr(part[0], part[1], char)

        key = stdscr.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = key

        head = [snake[0][0], snake[0][1]]
        if direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1

        snake.insert(0, head)

        if snake[0] == food:
            score += 1
            food = create_food(snake, sh, sw)
        else:
            snake.pop()

        if (
            snake[0][0] in [0, sh-1] or
            snake[0][1] in [0, sw-1] or
            snake[0] in snake[1:]
        ):
            msg = ' Game Over! Press Q to quit. '
            stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            stdscr.nodelay(0)
            while True:
                key = stdscr.getch()
                if key in [ord('q'), ord('Q')]:
                    return

        stdscr.refresh()


def run():
    curses.wrapper(main)


if __name__ == '__main__':
    run()
