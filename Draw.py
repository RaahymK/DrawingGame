import pygame
pygame.init()

width, height = 700, 600
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Draw World 1.0')

running = True

draw = False

red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (76, 153, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)
white = (255, 255, 255)
black = (0, 0, 0)

brush_size = 10


current_color = red
while running:
    pygame.time.delay(20)

    for event in pygame.event.get():
        # rect_time = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

        keys = pygame.key.get_pressed()
        # Clear all
        if keys[pygame.K_c]:
            screen.fill((0, 0, 0))

        # Fill tool
        if keys[pygame.K_f]:
            screen.fill(current_color)

    # Color Selection Visuals
    pygame.draw.rect(screen, (134, 134, 134), (0, 0, 100, 700))
    pygame.draw.rect(screen, red, (30, 10, 40, 40))
    pygame.draw.rect(screen, orange, (30, 60, 40, 40))
    pygame.draw.rect(screen, yellow, (30, 110, 40, 40))
    pygame.draw.rect(screen, green, (30, 160, 40, 40))
    pygame.draw.rect(screen, blue, (30, 210, 40, 40))
    pygame.draw.rect(screen, indigo, (30, 260, 40, 40))
    pygame.draw.rect(screen, violet, (30, 310, 40, 40))
    pygame.draw.rect(screen, white, (30, 360, 40, 40))
    pygame.draw.rect(screen, black, (30, 410, 40, 40))

    # Brush Size Selection Visuals
    pygame.draw.circle(screen, white, (50, 470), 5)
    pygame.draw.circle(screen, white, (50, 500), 10)
    pygame.draw.circle(screen, white, (50, 540), 20)

    # Drawing inputs
    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[0] > 100:
        pygame.draw.circle(screen, current_color, mouse_pos, brush_size)
    # Simplified color and brush size selecting inputs
    if draw and mouse_pos[0] < 100:
        if 30 <= mouse_pos[0] <= 70:
            # Colors
            if 10 <= mouse_pos[1] <= 50:
                current_color = red
            if 60 <= mouse_pos[1] <= 100:
                current_color = orange
            if 110 <= mouse_pos[1] <= 150:
                current_color = yellow
            if 160 <= mouse_pos[1] <= 200:
                current_color = green
            if 210 <= mouse_pos[1] <= 250:
                current_color = blue
            if 260 <= mouse_pos[1] <= 300:
                current_color = indigo
            if 310 <= mouse_pos[1] <= 350:
                current_color = violet
            if 360 <= mouse_pos[1] <= 400:
                current_color = white
            if 410 <= mouse_pos[1] <= 450:
                current_color = black
        if 30 <= mouse_pos[0] <= 70:
            if 460 <= mouse_pos[1] <= 480:
                brush_size = 5
            if 490 <= mouse_pos[1] <= 510:
                brush_size = 10
            if 530 <= mouse_pos[1] <= 550:
                brush_size = 20
    pygame.display.update()

