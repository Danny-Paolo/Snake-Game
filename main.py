import pygame
import random
import time
import sys
from settings.setting_main import Settings
from snake import Snake
from food import Food

class BOARD:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT)
        )

        self.snake = Snake(self)
        self.food = Food(self)

        # Tiempo ejecución proceso
        self.FPS = 10
        self.fpsClock = pygame.time.Clock()

        # Mostrar puntaje en la pantalla
        self.fuente = pygame.font.SysFont(self.settings.text_font,self.settings.text_size)
        # Puntaje
        self.score = 0

    def screen_design(self):
        pygame.display.set_caption("Mi primer juego snake")
        self.screen.fill(self.settings.SCREEN_BG)
        self.render_texto()

    def event_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.snake.key_pressed(event.key)

    def render_texto(self):
        texto = self.fuente.render(str(self.score),True,self.settings.text_color)
        self.screen.blit(texto,(self.settings.SCREEN_WIDTH-40,20))
    
    def update_score(self):
        self.score += 1
    
    # Actualiza comida
    def food_position_random(self):
        return (
            random.randrange(0,self.settings.SCREEN_WIDTH-20,20),
            random.randrange(0,self.settings.SCREEN_HEIGHT,20)
        )

    # Retorna comida en posicion random cuando colisionan
    def collision_snake_food(self):
        if (self.snake.position[0] == self.food.position_random[0][0] and self.snake.position[1] == self.food.position_random[0][1]) :
            # Agrega objeto ultima posicion
            self.snake.body.append(
                [self.snake.body[-1][0],self.snake.body[-1][1]]
            )
            self.update_score()
            return self.food_position_random()

    def main(self):
        while True:
            self.event_keys()
            self.screen_design()
            self.snake.show_snake()
            self.snake.change_position()
            self.food.show_food(self.collision_snake_food())
            self.snake.collision_snake_body()
            pygame.display.flip()
            self.fpsClock.tick(self.FPS)

if __name__ == "__main__":
    board = BOARD()
    board.main()
