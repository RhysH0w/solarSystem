# Import the libraries
import pygame
import random
from planetsClass import *
from static import *

# Initialise the engines
pygame.init()
pygame.font.init()

# assign planets



Sun = Planet(name='Sun', radius=50, colour=sun, speed=200, start = 0 , dfs=0, mass='1,989,000,000,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size =  "696,340 km", screen = size, gravPull = "274", gravVel = "0")
# original = 856.26


Mercury = Planet(name='Mercury', radius=3, colour=mercury, speed=0.00477, start = 0 , dfs=60, mass='328,500,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "2,439.7 km", screen = size, gravPull = "3.7", gravVel = "47.9")

Venus = Planet(name='Venus', radius=7, colour=venus, speed=0.00354, dfs=80, start = 0 , mass='4,867,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "6,051.8 km", screen = size, gravPull = "8.87", gravVel = "35.0")

Earth = Planet(name='Earth', radius=8, colour=earth, speed=0.003, dfs=100, start = 0 , mass='5,972,200,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "6,371 km", screen = size, gravPull = "9.807", gravVel = "29.8")

Mars = Planet(name='Mars', radius=4, colour=mars, speed=0.002424, dfs=120, start = 0 , mass='639,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "3,389.5 km", screen = size, gravPull = "3.721", gravVel = "24.1")

Jupiter = Planet(name='Jupiter', radius=35, colour=jupiter, speed=0.001317, start = 0 , dfs=183, mass='1,898,000,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "69,911 km", screen = size, gravPull = "24.79", gravVel = "13.1")

Saturn = Planet(name='Saturn', radius=30, colour=saturn, speed=0.000975, start = 0 , dfs=255, mass='568,300,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "58,232 km", screen = size, gravPull = "10.44", gravVel = "9.7")

Uranus = Planet(name='Uranus', radius=25, colour=uranus, speed=0.000684, start = 0 , dfs=315, mass='86,810,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "25,362 km", screen = size, gravPull = "8.87", gravVel = "6.8")

Neptune = Planet(name='Neptune', radius=24, colour=neptune, speed=0.000546, start = 0 , dfs=370, mass='102,400,000,000,000,000,000,000,000', angle = random.uniform(0,6.2832), size = "24,622 km", screen = size, gravPull = "11.15", gravVel = "5.4")


planets = (Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("Solar System")


def factPage(Title, mass, size, gravPull,gravVel):
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and 140 < mouse[0] < 300 and 644 < mouse[1] < 714:
                end = True

        mouse = pygame.mouse.get_pos()

        gameDisplay.fill(black)
        # Setting the variable texts
        title = infoTitle.render(Title, True, white)
        Mass = infoFont.render("The mass of the planet is: " + mass, True, white)
        Size = infoFont.render("The radius of the planet is: " + size, True, white)
        GravPull = infoFont.render("The gravitational pull is: " + gravPull + " m/s²", True, white)
        GravVel = infoFont.render("The gravitational velocity is: " + gravVel + " km/s", True, white)
        if 140 < mouse[0] < 300 and 644 < mouse[1] < 714:
            Back = buttonFont2.render("Back", True, mercury)
        else:
            Back = buttonFont2.render("Back", True, white)

        # Inserting the text on the screen
        gameDisplay.blit(title, [144, 100])
        gameDisplay.blit(Mass, [144, 244])
        gameDisplay.blit(Size, [144, 344])
        gameDisplay.blit(GravPull, [144, 444])
        gameDisplay.blit(GravVel, [144, 544])
        gameDisplay.blit(Back, [144, 644])

        pygame.display.flip()

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
                x = Planet.speed(planets)
                if x != 0:
                    Planet.Stop(planets)
                else:
                    Planet.Start(planets)

            for planet in planets:
                ax = planet.get_centrex()
                ay = planet.get_centrey()
                radius1 = planet.get_attr("radius")
                if event.type == pygame.MOUSEBUTTONDOWN and ax - radius1 < mouse[0] < ax + radius1 and ay - radius1 < mouse[1] < ay + radius1:

                    title = planet.get_attr("name")
                    mass = planet.get_attr("mass")
                    scale = planet.get_attr("size")
                    gravPull = planet.get_attr("gravPull")
                    gravVel = planet.get_attr("gravVel")

                    factPage(title, mass, scale, gravPull, gravVel)


        # selecting the Fonts
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

        if Planet.speed(planets) == 0:
            direct = "Start"
        else:
            direct = "Stop"

        if 40 < mouse[0] < 220 and 70 < mouse[1] < 130:
            speedMore = optFont.render("+ Speed", True, mercury)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render(direct, True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        elif 40 < mouse[0] < 220 and 140 < mouse[1] < 200:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, mercury)
            Start = optFont.render(direct, True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        elif 40 < mouse[0] < 220 and 210 < mouse[1] < 270:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render(direct, True, mercury)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        else:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render(direct, True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        for planet in planets:
            ax = planet.get_centrex()
            ay = planet.get_centrey()
            radius1 = planet.get_attr("radius")
            name1 = planet.get_attr("name")
            if ax - radius1 < mouse[0] < ax + radius1 and ay - radius1 < mouse[1] < ay + radius1:
                planetName = optFont.render(name1, True, mercury)
                gameDisplay.blit(planetName, [ax, ay + radius1 + 10])

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

            if event.type == pygame.MOUSEBUTTONDOWN and 190 < mouse[0] < 340 and 530 < mouse[1] < 610:
                play1()

            if event.type == pygame.MOUSEBUTTONDOWN and 690 < mouse[0] < 1060 and 530 < mouse[1] < 600:
                instrucions()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        # Game logic

        # Select font
        title = titleFont.render("Welcome To The Solar System", True, pink)

        if 190 < mouse[0] < 340 and 530 < mouse[1] < 610:
            play = buttonFont2.render("Play", True, mercury)
            instruct = buttonFont2.render("Instructions", True, white)
        elif 690 < mouse[0] < 1060 and 530 < mouse[1] < 600:
            play = buttonFont2.render("Play", True, white)
            instruct = buttonFont2.render("Instructions", True, mercury)
        else:
            play = buttonFont2.render("Play", True, white)
            instruct = buttonFont2.render("Instructions", True, white)

        # Drawing code here
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, lime, [190, 530, 150, 80])
        pygame.draw.rect(gameDisplay, lime, [690, 530, 370, 70])
        gameDisplay.blit(title, [350, 100])
        gameDisplay.blit(play, [200, 530])
        gameDisplay.blit(instruct, [700, 530])
        pygame.display.flip()

    pygame.QUIT


start()
