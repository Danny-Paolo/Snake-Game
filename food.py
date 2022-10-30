import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self,main):
        super().__init__()
        self.main = main
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255,0,0))
        # self.position_random = [
        #     (220,420)
        # ]
        self.position_random = [
            (
                random.randrange(0,self.main.settings.SCREEN_WIDTH-20,20),
                random.randrange(0,self.main.settings.SCREEN_HEIGHT,20)
            )
        ]
        self.rect = self.surf.get_rect()

    # Muestra comida posiciones random
    def show_food(self,value):
        if value :
            self.position_random[0] = value
        return self.main.screen.blit(self.surf,self.position_random[0])