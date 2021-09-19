from pygame import font
from pygame.constants import K_RETURN
from Enemy import Enemy
import pygame
import random
from Enemy import *
from EnemyBullet import *

class SceneManager:

    def __init__(self, screen, player_instance):
        self.screen = screen
        self.player_instance = player_instance

        self.main_game_scene_enemy_container = []
        self.enemy_spawn_time = random.randint(1, 5)
        self.enemy_bullets = []

        pygame.font.init()
        self.font = pygame.font.Font("Oswald.ttf", 14, bold=True)

        self.points = 0

        self.scene = "GameScene"

    def scene_state(self, dt):
        if self.scene == "GameScene":
            self.main_game_scene(dt)
        if self.scene == "GameOver":
            self.game_over_scene()

    def main_game_scene(self, dt):
        self.enemy_spawn_time -= 1 * dt
        if self.enemy_spawn_time < 0:
            self.main_game_scene_enemy_container.append(Enemy(self.screen, random.randint(0, 540 - 30), 0 - 30, 30, 30, 100))
            self.enemy_spawn_time = random.randint(1, 2)

        self.screen.fill((0, 0, 0))

        for enemy in self.main_game_scene_enemy_container:
            enemy.update(dt)
            if enemy.is_shooting:
                self.enemy_bullets.append(EnemyBullet(self.screen, enemy.x + (enemy.width / 2 - 5), enemy.y + 30, 10, 10, 200))
            if enemy.y > 360:
                self.scene = "GameOver"
            if enemy.enemy_rect.colliderect(self.player_instance.player_rect):
                self.scene = "GameOver"
        
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(dt)
            if enemy_bullet.y < 0:
                self.enemy_bullets.remove(enemy_bullet)
            if enemy_bullet.bullet_rect.colliderect(self.player_instance.player_rect):
                self.scene = "GameOver"

        for bullet in self.player_instance.bullets:
            bullet.update(dt)
            if bullet.y + bullet.height < 0:
                self.player_instance.bullets.remove(bullet)
            for enemy in self.main_game_scene_enemy_container:
                if bullet.bullet_rect.colliderect(enemy.enemy_rect):
                    self.main_game_scene_enemy_container.remove(enemy)
                    self.player_instance.bullets.remove(bullet)
                    self.points += 1

        self.player_instance.update(dt)

        text = self.font.render(f"Points: {self.points}", True, (255,255,255))
        self.screen.blit(text, (10, 10))

    def game_over_scene(self):
        key = pygame.key.get_pressed()
        self.screen.fill((0, 0, 0))
        header_text = self.font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(header_text, (250, 150))
        points_text = self.font.render(f"Your points: {self.points}", True, (255, 255, 255))
        self.screen.blit(points_text, (240, 170))
        play_again_text = self.font.render("Press Enter to try again!", True, (255, 255, 255))
        self.screen.blit(play_again_text, (220, 190))
        if key[K_RETURN]:
            self.enemy_bullets.clear()
            self.main_game_scene_enemy_container.clear()
            self.points = 0
            self.scene = "GameScene"