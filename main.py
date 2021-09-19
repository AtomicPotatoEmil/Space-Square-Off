from SceneManager import SceneManager
import pygame
from Player import *

screen = pygame.display.set_mode((540, 360))
pygame.display.set_caption("Space Square Off")

clock = pygame.time.Clock()

player = Player(screen, 320, 340, 50, 15, 300)
scene_manager = SceneManager(screen, player)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    dt = clock.tick(60) / 1000

    scene_manager.scene_state(dt)

    pygame.display.update()

pygame.quit()
