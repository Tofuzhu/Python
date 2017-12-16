import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_up:
            self.bottom -= self.ai_settings.ship_speed_factor
        elif self.moving_down:
            self.bottom += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
