import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {"up" : False, "down" : False, "left" : False, "right" : False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def update(self, tilemap, movement=(0, 0)):
        # collisions reset every frame
        self.collisions = {"up" : False, "down" : False, "left" : False, "right" : False}

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # update position based on frame_movement which is passed a movement var which are booleans that are updated on keydown
        self.pos[0] += frame_movement[0]
        # dynamically creating rect for entity
        entity_rect = self.rect()
        # each rectangle in the physics rects around the entity pos
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # if moving right and collision
                if frame_movement[0] > 0:
                    # make right edge of entity snap to left edge of tile
                    entity_rect.right = rect.left
                    self.collisions["right"] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions["left"] = True
                # update player position
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        # dynamically creating rect for entity
        entity_rect = self.rect()
        # each rectangle in the physics rects around the entity pos
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # if moving up and collision
                if frame_movement[1] > 0:
                    # make bottom edge of entity snap to top edge of tile
                    entity_rect.bottom = rect.top
                    self.collisions["down"] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions["up"] = True
                # update player position
                self.pos[1] = entity_rect.y

        # gravity - won't exceed 5
        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        # reset vertical velocity / gravity on upwasrds or downwards collision
        if self.collisions["down"] or self.collisions["up"]:
            self.velocity[1] = 0
        
        # below code would keep accelerating
        # self.velocity[1] += self.velocity[1] + .1



    def render (self, surf, offset=(0, 0)):
        surf.blit(self.game.assets["player"], (self.pos[0] - offset[0], self.pos[1] - offset[1]))