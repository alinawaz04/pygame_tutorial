import pygame
import sys
from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("ninja game")

        # set resolution of window
        self.screen = pygame.display.set_mode((640, 480))
        # generates empty surface for rendering to therefore scale onto screen creating pixel art effect
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            "decor": load_images("tiles/decor"),
            "grass": load_images("tiles/grass"),
            "large_decor": load_images("tiles/large_decor"),
            "spawners": load_images("tiles/spawners"),
            "stone": load_images("tiles/stone"),
            "player": load_image("entities/player.png")
        }

        self.player = PhysicsEntity(self, "player", (50, 50), (8, 15))

        self.tilemap = Tilemap(self, tile_size = 16)

        # camera movement, see render of tiles and player
        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.fill((14,219,248))


            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.tilemap.render(self.display, offset=render_scroll)

            # updating x value of postion (right and left movement)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            print(self.tilemap.physics_rects_around(self.player.pos))
            print(self.tilemap.tiles_around(self.player.pos))


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
                    if event.key == pygame.K_w:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:                        
                        self.movement[1] = False
                
            # blit display onto screen, then scale to size of screen, scaling up size of image
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            
            pygame.display.update()
            # set fps to 60
            self.clock.tick(60)

Game().run()