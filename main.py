import pygame

pygame.init()

WIDTH = 320
HEIGHT = 300+20 + 50+10

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

board = [[-1] * 3] * 3

def draw_board():
    for x in range(4):
        for y in range(4):
            pygame.draw.line(screen, 'black', (x * 100 + 10, y * 100 + 10), (300 + 10, y * 100 + 10), 4)
            pygame.draw.line(screen, 'black', (x * 100 + 10, y * 100 + 10), (x * 100 + 10, 300 + 10), 4)
    pygame.draw.rect(screen, 'white', [10, 320 + 5, 300, 50])

def place_image(cur_coords):
    print(cur_coords)
    screen.blit(image[turn], cur_coords)

turn = 0
cur_coords = (-1, -1)

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = (event.pos[0] - 10) // 100
            y_coord = (event.pos[1] - 10) // 100
            cur_coords = (x_coord, y_coord)
            place_image(cur_coords)

    pygame.display.flip()
pygame.quit()
