import pygame
import sys

class Snake:
    def __init__(self,main):
        self.main = main
        self.surf = pygame.Surface((20,20))
        self.surf.fill((90, 90, 90))
        self.center = (
            int(self.main.screen.get_width()/2),int(self.main.screen.get_height()/2)
        )
        self.rect = self.surf.get_rect(center=(self.center))
        self.mov_pos = "option"
        # Agrega en el array cuándo come alimento
        self.position = [780, self.center[1]]

        self.body = [
            [780, self.center[1]],
            [800, self.center[1]],
        ]

    def key_pressed(self, key):
        if key == pygame.K_LEFT:
            self.mov_pos = "LEFT"
        elif key == pygame.K_UP:
            self.mov_pos = "UP"
        elif key == pygame.K_RIGHT:
            self.mov_pos = "RIGHT"
        elif key == pygame.K_DOWN:
            self.mov_pos = "DOWN"

    # Movimiento cuerpo
    def change_position_body(self):
        num = self.position.copy()
        self.body.insert(0,num)
        self.body.pop()

    def change_position(self):
        if self.mov_pos == "LEFT" and self.position[0] > -20 :
            self.position[0] -= 20
            self.change_position_body()
        elif self.mov_pos == "RIGHT" and self.position[0] < self.main.settings.SCREEN_WIDTH:
            self.position[0] += 20
            self.change_position_body()
        elif self.mov_pos == "UP" and self.position[1] > -20:
            self.position[1] -= 20
            self.change_position_body()
        elif self.mov_pos == "DOWN" and self.position[1] < self.main.settings.SCREEN_HEIGHT:
            self.position[1] += 20
            self.change_position_body()
        self.collision_snake_wall()

    def show_snake(self):
        for pixer in self.body:
            self.main.screen.blit(self.surf,pixer)

    # Colision en paredes
    def collision_snake_wall(self):
        if self.position[0] == -20 : sys.exit()
        if self.position[0] == self.main.settings.SCREEN_WIDTH : sys.exit()
        if self.position[1] == -20 : sys.exit()
        if self.position[1] == self.main.settings.SCREEN_HEIGHT : sys.exit()

    # Colisiona el cuerpo
    def collision_snake_body(self):
        head = self.body[0]
        for value in self.body[1:]:
            if head == value:
                sys.exit()