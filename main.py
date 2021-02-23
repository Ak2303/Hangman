import pygame
import math
#initialise
pygame.init()

#display
WIDTH, HEIGHT  = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Title
pygame.display.set_caption("Hangman")

#FPS
FPS = 60
clock = pygame.time.Clock()

#images
images = []
for i in range(7):
    image = pygame.image.load("images\hangman"+ str(i) + ".png")
    images.append(image)
    
#Button variables
RADIUS = 20
GAP = 15
letters = []
startX = round((WIDTH - (RADIUS * 2 + GAP) * 13)/2)
startY = 400
for i in range(26):
    x = startX + GAP *2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = startY + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(65 + i), True])

#fonts
LETTER_FONTS = pygame.font.SysFont("ink free", 28)

#Game variables
hangmanStatus = 6

def draw():
    screen.fill((255, 255, 255))
    
    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, (0, 0, 0), (x, y), RADIUS, 3)
            text = LETTER_FONTS.render(ltr, 1, (0, 0, 0))
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    screen.blit(images[hangmanStatus], (150,100))
    pygame.display.update()

#Game loop
run = True
while run:
    clock.tick(FPS)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mx, My = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                distance = math.sqrt((x - Mx)**2 + (y - My)**2)
                if distance < RADIUS:
                    letter[3] = False



pygame.quit() 











