# Import the librarys
import pygame
import random
from planetsClass import *

# Initialise the engines
pygame.init()
pygame.font.init()

# Assign the colours
black = (0, 0, 0)
white = (255, 255, 255)
lime = (35, 225, 63)
pink = (255, 14, 156)
turquoise = (97, 231, 199)
mercury = (131, 134, 139)
# assign planets

size = (1200, 795)

Sun = Planet(name='Sun', radius=50, colour=sun, speed=200, dfs=0, mass='1.989 × 10^30', angle = random.uniform(0,6.2832), size = size)
# original = 856.26


Mercury = Planet(name='Mercury', radius=3, colour=mercury, speed=0.00477, dfs=60, mass='3.285 × 10^23', angle = random.uniform(0,6.2832), size = size)
MerDis = Mercury.get_attr("dfs") + Mercury.get_attr("radius") + Sun.get_attr("radius")
# Original = 3

Venus = Planet(name='Venus', radius=7, colour=venus, speed=0.00354, dfs=80, mass='4.867 × 10^24', angle = random.uniform(0,6.2832), size = size)
VenDis = Venus.get_attr("dfs") + Venus.get_attr("radius") + Sun.get_attr("radius")
# Original = 7.44

Earth = Planet(name='Earth', radius=8, colour=earth, speed=0.003, dfs=100, mass='5.9722 × 10^24', angle = random.uniform(0,6.2832), size = size)
EarDis = Earth.get_attr("dfs") + Earth.get_attr("radius") + Sun.get_attr("radius")
# original = 7.83

Mars = Planet(name='Mars', radius=4, colour=mars, speed=0.002424, dfs=120, mass='6.39 × 10^23', angle = random.uniform(0,6.2832), size = size)
MarDis = Mars.get_attr("dfs") + Mars.get_attr("radius") + Sun.get_attr("radius")
# Original = 4.17

Jupiter = Planet(name='Jupiter', radius=35, colour=jupiter, speed=0.001317, dfs=183, mass='1.898 × 10^27', angle = random.uniform(0,6.2832), size = size)
JupDis = Jupiter.get_attr("dfs") + Jupiter.get_attr("radius") + Sun.get_attr("radius")
# Original = 85.97

Saturn = Planet(name='Saturn', radius=30, colour=saturn, speed=0.000975, dfs=255, mass='5.683 × 10^26', angle = random.uniform(0,6.2832), size = size)
SatDis = Saturn.get_attr("dfs") + Saturn.get_attr("radius") + Sun.get_attr("radius")
# original = 71.61

Uranus = Planet(name='Uranus', radius=25, colour=uranus, speed=0.000684, dfs=315, mass='8.681 × 10^25', angle = random.uniform(0,6.2832), size = size)
UraDis = Uranus.get_attr("dfs") + Uranus.get_attr("radius") + Sun.get_attr("radius")
# Original = 31.19

Neptune = Planet(name='Neptune', radius=24, colour=neptune, speed=0.000546, dfs=370, mass='1.024 × 10^26', angle = random.uniform(0,6.2832), size = size)
NepDis = Neptune.get_attr("dfs") + Neptune.get_attr("radius") + Sun.get_attr("radius")
# Create the clock
clock = pygame.time.Clock()

planets = (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("Solar System")


def instrucions():
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and 100 < mouse[0] < 190 and 530 < mouse[1] < 585:
                end = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        titleFont = pygame.font.SysFont('Calibri', 40, True, False)
        buttonFont = pygame.font.SysFont('Calibri', 25, True, False)
        menu = buttonFont.render("Menu", True, white)
        instruct = titleFont.render("Instructions", True, white)

        gameDisplay.fill(turquoise)
        pygame.draw.rect(gameDisplay, black, [100, 530, 90, 55])
        gameDisplay.blit(menu, [114, 547])
        gameDisplay.blit(instruct, [290, 40])
        pygame.display.flip()


# Creates the function for the instructions
def play1():
    # defining 'finish'
    finish = False
    # game program loop
    while not finish:
        # event loop
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # question to exit
            if event.type == pygame.QUIT:
                # exit the entire program
                pygame.quit()

            mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and 100 < mouse[0] < 190 and 530 < mouse[1] < 585:
                finish = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and 40 < mouse[0] < 220 and 70 < mouse[1] < 130:
                Planet.speedUp(planets)

            if event.type == pygame.MOUSEBUTTONDOWN and 40 < mouse[0] < 220 and 140 < mouse[1] < 200:
                Planet.slowDown(planets)

            if event.type == pygame.MOUSEBUTTONDOWN and 40 < mouse[0] < 220 and 210 < mouse[1] < 270:
                Planet.Start(planets)

        # selecting the Fonts
        buttonFont = pygame.font.SysFont('Calibri', 25, True, False)
        optFont = pygame.font.Font('Montserrat.ttf', 45)
        menu = buttonFont.render("Menu", True, white)

        gameDisplay.fill(black)
        # pygame.draw.circle(Sun) ~ ~ ~
        pygame.draw.rect(gameDisplay, lime, [100, 530, 90, 55])
        gameDisplay.blit(menu, [114, 547])
        Sun.render(gameDisplay, size)
        Mercury.render(gameDisplay, size)
        Venus.render(gameDisplay, size)
        Earth.render(gameDisplay, size)
        Mars.render(gameDisplay, size)
        Jupiter.render(gameDisplay, size)
        Saturn.render(gameDisplay, size)
        Uranus.render(gameDisplay, size)
        Neptune.render(gameDisplay, size)
        pygame.draw.rect(gameDisplay, lime, [40, 70, 180, 60])
        pygame.draw.rect(gameDisplay, lime, [40, 140, 180, 60])
        pygame.draw.rect(gameDisplay, lime, [40, 210, 180, 60])

        if 40 < mouse[0] < 220 and 70 < mouse[1] < 130:
            speedMore = optFont.render("+ Speed", True, mercury)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render("Start", True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        elif 40 < mouse[0] < 220 and 140 < mouse[1] < 200:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, mercury)
            Start = optFont.render("Start", True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        elif 40 < mouse[0] < 220 and 210 < mouse[1] < 270:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render("Start", True, mercury)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        else:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render("Start", True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])
        pygame.display.flip()


def start():
    # Defining 'done'
    done = False

    # Main program loop
    while not done:
        # Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If the user clicked close
                done = True  # Flag that we are done and exit the loop

            mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and 100 < mouse[0] < 190 and 530 < mouse[1] < 585:
                play1()

            if event.type == pygame.MOUSEBUTTONDOWN and 370 < mouse[0] < 500 and 255 < mouse[1] < 300:
                instrucions()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        # Game logic

        # Select font
        titleFont = pygame.font.SysFont('Calibri', 40, True, False)
        buttonFont = pygame.font.SysFont('Calibri', 25, True, False)
        title = titleFont.render("Welcome To The Solar System", True, pink)
        play = buttonFont.render("Play", True, turquoise)
        instruct = buttonFont.render("Instuctions", True, turquoise)

        # Drawing code here
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, white, [200, 530, 90, 55])
        pygame.draw.rect(gameDisplay, white, [370, 255, 130, 45])
        gameDisplay.blit(title, [350, 100])
        gameDisplay.blit(play, [220, 547])
        gameDisplay.blit(instruct, [380, 270])
        pygame.display.flip()

    pygame.QUIT


start()
