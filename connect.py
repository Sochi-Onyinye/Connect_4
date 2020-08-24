import numpy as np
import pygame
import sys
import math

pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)


def connect_4_board():
    board = [[0 for j in range(7)]for i in range(6)]
    return board


def is_column_empty(new_board, play):
    if new_board[len(new_board)-1][play] == 0:
        return True
    else:
        return False


def get_open_row(new_board, play):
    for index in range(len(new_board)):
        if new_board[index][play] == 0:
            return index


def drop_a_play(new_board, play, row, token):
    new_board[row][play] = token
    return new_board


def print_flip_new_board(new_board):
    print(np.flip(new_board, 0))


def win_win(new_board, token):
    # check for horizontal win
    for i in range(len(new_board)):
        for j in range(len(new_board[i])-3):
            if new_board[i][j] == token and new_board[i][j + 1] == token and new_board[i][j + 2] == token and new_board[i][j + 3] == token:
                return True
    # Right diagonal win
    for i in range(len(new_board)-3):
        for j in range(len(new_board[i])-3):
            if new_board[i][j] == token and new_board[i + 1][j + 1] == token and new_board[i + 2][j + 2] == token and new_board[i + 3][j + 3] == token:
                    return True
    # Vertical win
    for i in range(len(new_board)-3):
        for j in range(len(new_board[i])):
            if new_board[i][j] == token and  new_board[i+ 1][j] == token and new_board[i + 2][j] == token and new_board[i + 3][j] == token:
                return True
    # Left diagonal win
    for i in range(3, len(new_board)):
        for j in range(len(new_board[i])-3):
            if new_board[i][j] == token and  new_board[i - 1][j + 1] == token and new_board[i - 2][j + 2] == token and new_board[i - 3][j + 3] == token:
                return True


def create_board(new_board):
    for j in range(len(new_board[0])):
        for i in range(len(new_board)):
            pygame.draw.rect(screen, GREEN, ((j*Board_size), ((i*Board_size) + Board_size), Board_size, Board_size))
            pygame.draw.circle(screen, BLACK, (int(j*Board_size + Board_size/2), int(i*Board_size + Board_size + Board_size/2)), radius)
    for j in range(len(new_board[0])):
        for i in range(len(new_board)):
            if new_board[i][j] == 1:
                pygame.draw.circle(screen, YELLOW, (int(j*Board_size + Board_size/2), length - int(i*Board_size  + Board_size/2)), radius)
            elif new_board[i][j] == 2:
                pygame.draw.circle(screen, PURPLE, (int(j*Board_size + Board_size/2), length - int(i*Board_size + Board_size/2)), radius)
    pygame.display.update()


Board_size = 100
width = 7 * Board_size
length = 6 * Board_size

size = (width, length)
radius = int(Board_size/2 - 5)
new_radius = int(Board_size)

screen = pygame.display.set_mode(size)

my_font = pygame.font.SysFont("dejavuserif", 75)
my_text = pygame.font.SysFont("dejavuserif", 25)
end_game = True


def start_play():
    new_board = connect_4_board()
    create_board(new_board)
    pygame.display.update()
    token_1 = 1
    token_2 = 2
    play_count = 0
    end_game = True

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if end_game:
                        pygame.draw.rect(screen, BLACK, (0, 0, width, Board_size))
                        position_x = event.pos[0]
                        if play_count == 0:
                            pygame.draw.circle(screen, YELLOW, (position_x, int(Board_size/2)), radius)
                        else:
                            pygame.draw.circle(screen, PURPLE, (position_x, int(Board_size/2)), radius)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if end_game:
                        pygame.draw.rect(screen, BLACK, (0, 0, width, Board_size))
                        # ask for each players input
                        if play_count == 0:
                            position_x = event.pos[0]
                            play = int(math.floor(position_x / Board_size))
                            if is_column_empty(new_board, play):
                                row = get_open_row(new_board, play)
                                drop_a_play(new_board, play, row, token_1)
                                if win_win(new_board, token_1):
                                    say_win = my_font.render("Player 1 wins!!", True, YELLOW)
                                    screen.blit(say_win, (40, 10))
                                    end_game = False
                                    pygame.display.update()
                                    pygame.time.wait(3000)
                                    pygame.draw.rect(screen, YELLOW, (0, 0, width, length))
                                    pygame.draw.rect(screen, PURPLE, (100, 150, 175, 150))
                                    pygame.draw.rect(screen, PURPLE, (400, 150, 175, 150))
                                    choice_time = my_text.render("RESTART:)", True, BLACK)
                                    screen.blit(choice_time, (105, 200))
                                    choice_time = my_text.render("QUIT :(", True, BLACK)
                                    screen.blit(choice_time, (415, 200))

                                pygame.display.update
                            print_flip_new_board(new_board)
                            play_count = 1
                        else:
                            position_x = event.pos[0]
                            play = int(math.floor(position_x / Board_size))
                            if is_column_empty(new_board, play):
                                row = get_open_row(new_board, play)
                                drop_a_play(new_board, play, row, token_2)
                                if win_win(new_board, token_2):
                                    say_win = my_font.render("Player 2 wins!!", True, PURPLE)
                                    screen.blit(say_win, (40, 10))
                                    end_game = False
                                    pygame.display.update()
                                    pygame.time.wait(3000)
                                    pygame.draw.rect(screen, PURPLE, (0, 0, width, length))
                                    pygame.draw.rect(screen, YELLOW, (100, 150, 175, 150))
                                    pygame.draw.rect(screen, YELLOW, (400, 150, 175, 150))
                                    choice_time = my_text.render("RESTART :)", True, BLACK)
                                    screen.blit(choice_time, (105,200))
                                    choice_time = my_text.render(" QUIT :(", True, BLACK)
                                    screen.blit(choice_time, (415, 200))
                                    pygame.display.update()
                            print_flip_new_board(new_board)
                            play_count = 0
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.pos[0] >= 100 and event.pos[0] <= 275 and event.pos[1] >= 150 and event.pos[1] <= 300:
                                start_play()

                            elif event.pos[0] >= 400 and event.pos[0] <= 575 and event.pos[1] > 150 and event.pos[1] < 300:
                                pygame.quit()
                                sys.exit()
        if end_game:
            create_board(new_board)
        pygame.display.update()


start_play()
if end_game is False:
        pygame.time.wait(3000)
