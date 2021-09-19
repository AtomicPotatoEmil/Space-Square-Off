import pygame
import random

class Enemy:

    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.enemy_rect = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        self.is_shooting = False
        self.shoot_timer = random.randint(0, 4)

    def update(self, dt):
        self.can_shoot(dt)
        self.draw()
        self.move(dt)
        pass

    def move(self, dt):
        self.y += self.speed * dt

    def draw(self):
        self.enemy_rect = pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
    
    def can_shoot(self, dt):
        self.shoot_timer -= 1 * dt
        if self.shoot_timer < 0:
            self.is_shooting = True
            self.shoot_timer = random.randint(1, 3)
        else:
            self.is_shooting = False