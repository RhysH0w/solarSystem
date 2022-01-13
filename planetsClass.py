import pygame
import math
from static import *
import random


class Planet:
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def get_attr(self, attr):
        return self.__getattribute__(attr)

    def set_attr(self, attrName, value):
        setattr(attrName, value)

    def render(self, surface, size, image):
        self.UpdatePos()
        pygame.draw.circle(surface, mercuryCol, (size[0]/2, size[1]/2), self.dfs, 1)
        pygame.draw.circle(surface ,self.colour, [self.X,self.Y], self.radius)
        surface.blit(image, [self.X - self.radius, self.Y - self.radius])

    def UpdatePos(self):
        self.angle += self.speed
        chanX = math.sin(self.angle) * self.dfs
        chanY = math.cos(self.angle) * self.dfs
        self.X = chanX + (self.screen[0] / 2)
        self.Y = chanY + (self.screen[1] / 2)

    def get_centrex(self):
        return self.X

    def get_centrey(self):
        return self.Y

    @classmethod
    def speedUp(cls, planets):
        for x in planets:
            x.speed *= 1.5
            x.start *= 1.5

    @classmethod
    def slowDown(cls, planets):
        for x in planets:
            x.speed *= 0.5
            x.start *= 0.5

    @classmethod
    def Stop(cls, planets):
        for x in planets:
            x.start = x.speed
            x.speed = 0

    @classmethod
    def Start(cls, planets):
        for x in planets:
            x.speed = x.start

    @classmethod
    def speed(cls, planets):
        for x in planets:
            return x.speed


Sun = Planet(name='Sun', radius=50, colour=sunCol, speed=200, start = 0 , dfs=0, mass='1,989,000,000,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size =  "696,340 km", screen = size, gravPull = "274", gravVel = "0")
# original = 856.26


Mercury = Planet(name='Mercury', radius=3, colour=mercuryCol, speed=0.00477, start = 0 , dfs=60, mass='328,500,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "2,439.7 km", screen = size, gravPull = "3.7", gravVel = "47.9")

Venus = Planet(name='Venus', radius=7, colour=venusCol, speed=0.00354, dfs=80, start = 0 , mass='4,867,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "6,051.8 km", screen = size, gravPull = "8.87", gravVel = "35.0")

Earth = Planet(name='Earth', radius=8, colour=earthCol, speed=0.003, dfs=100, start = 0 , mass='5,972,200,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "6,371 km", screen = size, gravPull = "9.807", gravVel = "29.8")

Mars = Planet(name='Mars', radius=4, colour=marsCol, speed=0.002424, dfs=120, start = 0 , mass='639,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "3,389.5 km", screen = size, gravPull = "3.721", gravVel = "24.1")

Jupiter = Planet(name='Jupiter', radius=35,  colour = jupiterCol, speed=0.001317, start = 0 , dfs=183, mass='1,898,000,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "69,911 km", screen = size, gravPull = "24.79", gravVel = "13.1")

Saturn = Planet(name='Saturn', radius=30,  colour = saturnCol, speed=0.000975, start = 0 , dfs=255, mass='568,300,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "58,232 km", screen = size, gravPull = "10.44", gravVel = "9.7")

Uranus = Planet(name='Uranus', radius=25,  colour = uranusCol, speed=0.000684, start = 0 , dfs=315, mass='86,810,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "25,362 km", screen = size, gravPull = "8.87", gravVel = "6.8")

Neptune = Planet(name='Neptune', radius=24,  colour = neptuneCol, speed=0.000546, start = 0 , dfs=370, mass='102,400,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "24,622 km", screen = size, gravPull = "11.15", gravVel = "5.4")

planets = (Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

sunImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
sunImg = pygame.transform.scale(sunImg, [Sun.get_attr("radius")*2, Sun.get_attr("radius")*2])

MercuryImg = pygame.image.load(os.path.join('static', 'mercury.PNG'))
MercuryImg = pygame.transform.scale(MercuryImg, [Mercury.get_attr("radius")*2, Mercury.get_attr("radius")*2])

VenusImg = pygame.image.load(os.path.join('static', 'venus.PNG'))
VenusImg = pygame.transform.scale(VenusImg, [Venus.get_attr("radius")*2, Venus.get_attr("radius")*2])

EarthImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
EarthImg = pygame.transform.scale(EarthImg, [Earth.get_attr("radius")*2, Earth.get_attr("radius")*2])

MarsImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
MarsImg = pygame.transform.scale(MarsImg, [Mars.get_attr("radius")*2, Mars.get_attr("radius")*2])

JupiterImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
JupiterImg = pygame.transform.scale(JupiterImg, [Jupiter.get_attr("radius")*2, Jupiter.get_attr("radius")*2])

SaturnImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
SaturnImg = pygame.transform.scale(SaturnImg, [Saturn.get_attr("radius")*2, Saturn.get_attr("radius")*2])

UranusImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
UranusImg = pygame.transform.scale(UranusImg, [Uranus.get_attr("radius")*2, Uranus.get_attr("radius")*2])

NeptuneImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
NeptuneImg = pygame.transform.scale(NeptuneImg, [Neptune.get_attr("radius")*2, Neptune.get_attr("radius")*2])
