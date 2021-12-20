import pygame
import math

sun = (237, 88, 26)
mercury = (131, 134, 139)
venus = (231, 227, 224)
earth = (58, 65, 86)
mars = (253, 133, 96)
jupiter = (217, 199, 176)
saturn = (178, 167, 122)
uranus = (143, 161, 171)
neptune = (108, 139, 183)



class Planet:
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def get_attr(self, attr):
        return self.__getattribute__(attr)

    def set_attr(self, attrName, value):
        setattr(attrName, value)

    def render(self, surface, size):
        self.UpdatePos()
        pygame.draw.circle(surface, mercury, (size[0]/2, size[1]/2), self.dfs, 1)
        pygame.draw.circle(surface ,self.colour, [self.X,self.Y], self.radius)

    def UpdatePos(self):
        self.angle += self.speed
        chanX = math.sin(self.angle) * self.dfs
        chanY = math.cos(self.angle) * self.dfs
        self.X = chanX + (self.size[0] / 2)
        self.Y = chanY + (self.size[1] / 2)
