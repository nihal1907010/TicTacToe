import pygame

pygame.init()

WIDTH = 320
HEIGHT = 300 + 20 + 50 + 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.SysFont('Arial', 30)
timer = pygame.time.Clock()
fps = 60

nought = pygame.image.load('assets/nought.png')
nought = pygame.transform.scale(nought, (80, 80))

cross = pygame.image.load('assets/cross.png')
cross = pygame.transform.scale(cross, (80, 80))

image = [nought, cross]

BOARD = [[-1] * 3, [-1] * 3, [-1] * 3]
TURN = 0
NO_OF_MOVES = 0

piece_list = ['cross', 'nought']


def draw_board():
    for x in range(4):
        for y in range(4):
            pygame.draw.line(screen, 'black', (x * 100 + 10, y * 100 + 10), (300 + 10, y * 100 + 10), 4)
            pygame.draw.line(screen, 'black', (x * 100 + 10, y * 100 + 10), (x * 100 + 10, 300 + 10), 4)
    pygame.draw.rect(screen, 'white', [10, 320 + 5, 300, 50])


def draw_piece(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != -1:
                screen.blit(image[board[i][j]], (j * 100 + 10 + 10, i * 100 + 10 + 10))


def get_winner(board):
    winner = -1
    for i in range(0, 3):
        if board[i][0] != -1 and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            winner = board[i][0]

    for j in range(0, 3):
        if board[0][j] != -1 and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            winner = board[0][j]

    if board[0][0] != -1 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner = board[0][0]

    if board[0][2] != -1 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        winner = board[0][2]

    return winner


def minimax(board_, no_of_moves, nought_player):
    coords = (-1, -1)

    if no_of_moves == 9:
        winner = get_winner(board_)
        if winner == 0:
            return 1, coords
        elif winner == 1:
            return -1, coords
        else:
            return 0, coords

    if nought_player == 0:
        maxEval = -1000
        board = board_.copy()
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    board[i][j] = 0
                    val_move = minimax(board, no_of_moves + 1, 1 - nought_player)
                    if val_move[0] > maxEval:
                        maxEval = val_move[0]
                        coords = (i, j)
                    board[i][j] = -1
        return maxEval, coords
    else:
        minEval = 1000
        board = board_.copy()
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    board[i][j] = 1
                    val_move = minimax(board, no_of_moves + 1, 1 - nought_player)
                    if val_move[0] < minEval:
                        minEval = val_move[0]
                        coords = (i, j)
                    board[i][j] = -1
        return minEval, coords


output = (-1, (-1, -1))

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_piece(BOARD)
    if TURN == 1 and output == (-1, (-1, -1)):
        output = minimax(BOARD, NO_OF_MOVES, TURN)
        BOARD[output[1][0]][output[1][1]] = TURN
        TURN = 1 - TURN
        NO_OF_MOVES += 1
        output = (-1, (-1, -1))
    WINNER = get_winner(BOARD)
    if WINNER != -1:
        screen.blit(font.render(str(WINNER), True, 'black'), (20, 335))
    if NO_OF_MOVES == 9:
        screen.blit(font.render("Game Over!", True, 'black'), (20, 335))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            NO_OF_MOVES += 1
            x_coord = (event.pos[0] - 10) // 100
            y_coord = (event.pos[1] - 10) // 100
            BOARD[y_coord][x_coord] = TURN
            TURN = 1 - TURN

    pygame.display.flip()

pygame.quit()
