import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

x = 50
y = 50
width = 40
height = 40
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.key.key_code("a")] and x > vel:
        x -= vel
        # print(x)
    if keys[pygame.K_RIGHT] or keys[pygame.key.key_code("d")] and x < 500 - width - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_UP] or keys[pygame.key.key_code("w")] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] or keys[pygame.key.key_code("s")] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    if x <= 5:
        run = False
    if x >= 455:
        run = False
    if y <= 5:
        run = False
    if y >= 455:
        run = False


    win.fill((0,0,0))
    #drawing walls:
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 500, 5))
    pygame.draw.rect(win, (255, 0, 0), (0, 495, 500, 5))
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 5, 500))
    pygame.draw.rect(win, (255, 0, 0), (495, 0, 5, 500))
    
    #drawing player:
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update() #update


pygame.quit()
