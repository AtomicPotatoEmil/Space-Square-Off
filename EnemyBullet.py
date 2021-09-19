import pygame

class EnemyBullet:

    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.bullet_rect = pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        pass

    def update(self, dt):
        self.draw()
        self.move(dt)
        pass

    def move(self, dt):
        self.y += self.speed * dt
        pass

    def draw(self):
        self.bullet_rect = pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        pass