import os
import random
import time

WIDTH = 20
HEIGHT = 10
SLEEP = 0.2

def clear_screen():
    os.system('clear')

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(height//2, width//2)]
        self.direction = (0, 1)
        self.food = self.random_food()
        self.score = 0

    def random_food(self):
        while True:
            pos = (random.randint(1, self.height-2), random.randint(1, self.width-2))
            if pos not in self.snake:
                return pos

    def step(self):
        head_y, head_x = self.snake[0]
        dir_y, dir_x = self.direction
        new_head = ((head_y + dir_y) % self.height, (head_x + dir_x) % self.width)
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.random_food()
        else:
            self.snake.pop()
        # change direction randomly
        if random.random() < 0.3:
            self.direction = random.choice([(0,1),(1,0),(0,-1),(-1,0)])

    def render(self):
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for y, x in self.snake:
            board[y][x] = '#'
        fy, fx = self.food
        board[fy][fx] = '*'
        border = '+' + '-'*self.width + '+'
        print(border)
        for row in board:
            print('|' + ''.join(row) + '|')
        print(border)
        print('Score:', self.score)


def run_game(steps=50):
    game = SnakeGame(WIDTH, HEIGHT)
    for _ in range(steps):
        # clear_screen()
        game.render()
        game.step()
        time.sleep(SLEEP)
    # clear_screen()
    game.render()
    print('Game over! Final score:', game.score)

if __name__ == '__main__':
    run_game()
