import pygame
import sys
from scripts.utils import load_image
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("ninja game")

        # set resolution of window
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "player": load_image("entities/player.png")
        }

        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))

    def run(self):
        while True:
            self.screen.fill((14,219,248))

            # updating x value of postion (right and left movement)
            self.player.update(((self.movement[1] - self.movement[0]), 0))
            self.player.render(self.screen)

            for event in pygame.event.get():

                # quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # movement events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:                        
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:                        
                        self.movement[1] = False
                
            pygame.display.update()

            # set fps to 60
            self.clock.tick(60)

Game().run()