import pygame, sys
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
background_color = 0, 0, 0

WINDOW_SIZE = (600, 600)
window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

position = 300, 300
gravity_f = 0
player = pygame.Rect(position, (32, 64))


platform = pygame.Rect((0, 500), (600, 64))

key_pressed = -1

def move(entity, velocity, gravity):
    entity.x += velocity[0]

    velocity[1] += gravity
    entity.y += velocity[1]
    
    if entity.colliderect(platform):
        if velocity[1] > 0:
            entity.bottom = platform.top
    return entity

while True:
    window.fill(background_color)

    gravity_f += 0.25

    if gravity_f >= 5:
        gravity_f = 5
    if gravity_f > 250:
        gravity_f = 250
    
    velocity = [0, 0]
    
    if key_pressed == 0:
        velocity[0] -= 5
    if key_pressed == 1:
        velocity[0] += 5
    if key_pressed == 2:
        gravity_f = -5
        key_pressed = False

    player = move(player, velocity, gravity_f)

    pygame.draw.rect(window, (255, 255, 0), platform)
    pygame.draw.rect(window, (255, 255, 255), player)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                key_pressed = 0
            if event.key == K_d:
                key_pressed = 1
            if event.key == K_w:
                key_pressed = 2
        if event.type == KEYUP:
            if event.key == K_a:
                key_pressed = -1
            if event.key == K_d:
                key_pressed = -1
        
    pygame.display.update()
    clock.tick(60)
