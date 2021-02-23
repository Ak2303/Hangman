import pygame

#initialise
pygame.init()

#dispaly
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
    

#Game variables
hangmanStatus = 6

#Game loop
run = True
while run:
    clock.tick(FPS)

    screen.fill((255, 255, 255))
    screen.blit(images[hangmanStatus], (150,100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)


pygame.quit() 











