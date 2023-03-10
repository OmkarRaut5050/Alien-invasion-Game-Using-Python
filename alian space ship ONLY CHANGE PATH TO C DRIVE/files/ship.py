import pygame
from pygame.sprite import Sprite
class ship(Sprite):
    def __init__(self,ai_settings,screen):
        self.screen = screen
        super().__init__()
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r"D:\PROJECTS\alian space ship ONLY CHANGE PATH TO C DRIVE\Images\ship.jpeg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_factor
        self.rect.centerx = self.center
    def center_ship(self):
        self.center = self.screen_rect.centerx
    def blitme(self):
        self.screen.blit(self.image,self.rect)
