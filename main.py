import pygame
import math
import random
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
WORD_FONTS = pygame.font.SysFont("Comic Sans MS", 40)

#Game variables
hangmanStatus = 0
word = random.choice(open("Words.txt").read().split())
guessed = []

def draw():
    screen.fill((255, 255, 255))
    
    #draw word
    drawWord = ""
    for letter in word:
        if letter in guessed:
            drawWord += letter + " "
        else:
            drawWord += "_ "
    text = WORD_FONTS.render(drawWord, 1, (0, 0, 0))
    screen.blit(text, (400, 200))

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
                    guessed.append(ltr)
                    if ltr not in word:
                        hangmanStatus += 1

    draw()
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        screen.fill((255,255,255))
        text = WORD_FONTS.render("You WON!!!", 1, (0, 0, 0))
        screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangmanStatus == 6:
        screen.fill((255,255,255))
        text = WORD_FONTS.render("You Lost!!!", 1, (0, 0, 0))
        screen.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        break 

pygame.quit() 









