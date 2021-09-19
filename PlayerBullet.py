import pygame

class PlayerBullet:

    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.bullet_rect = pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
    
    def update(self, dt):
        self.draw()
        self.move(dt)

    def move(self, dt):
        self.y -= self.speed * dt

    def draw(self):
        self.bullet_rect = pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))