import sys, pygame
pygame.init()

size = width, height = 640, 480
logo_size = logo_width, logo_height = 150, 100
logo_height_ratio = height / logo_height
logo_width_ratio = width / logo_width
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

logo = pygame.image.load("dvd_logo.png")
sized_logo = pygame.transform.scale(logo, logo_size)
logorect = sized_logo.get_rect()
clock = pygame.time.Clock()
pygame.display.set_caption("DVD SIM!")

running = True

while running:
    clock.tick(70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.WINDOWMAXIMIZED:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            screen = pygame.display.set_mode(size)
            screen = pygame.display.set_mode(size) # only seems to work when executed twice :/
                
        elif event.type == pygame.WINDOWSIZECHANGED:
            logo_size = screen.get_width() / logo_width_ratio, screen.get_height() / logo_height_ratio
            sized_logo = pygame.transform.scale(logo, logo_size)
            logorect = sized_logo.get_rect()
            if screen.get_height() > 1280:
                speed = [2, 2]
            else:
                speed = [1, 1]

    logorect = logorect.move(speed)
    if logorect.left < 0 or logorect.right > screen.get_width():
        speed[0] = -speed[0]
    if logorect.top < 0 or logorect.bottom > screen.get_height():
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(sized_logo, logorect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()