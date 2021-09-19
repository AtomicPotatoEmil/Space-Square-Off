import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, K_a, K_d
from PlayerBullet import *

class Player:

    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.screen_width, self.screen_height = screen.get_size()
        self.bullets = []
        self.shooting = False
        self.player_rect = pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x, self.y, self.width, self.height))

    def update(self, dt):
        self.shoot()
        self.draw()
        self.move(self.speed, dt)

    def move(self, player_speed, dt):
        key = pygame.key.get_pressed()
        if self.x < self.screen_width - self.width:
            if key[K_d] or key[K_RIGHT]:
                self.x += player_speed * dt
        if self.x > 0:
            if key[K_a] or key[K_LEFT]:
                self.x -= player_speed * dt

    def draw(self):
        self.player_rect = pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x, self.y, self.width, self.height))
    
    def shoot(self):
        key = pygame.key.get_pressed()
        if len(self.bullets) < 1 and key[K_SPACE]:
            self.bullets.append(PlayerBullet(self.screen, self.x + (self.width / 2 - 5), self.y, 10, 10, 500))
        pass
            