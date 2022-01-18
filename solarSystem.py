# Import the libraries
import pygame
import random
from planetsClass import *
from static import *
from hashlib import sha256

# Initialise the engines
pygame.init()
pygame.font.init()

def factPage(Title, mass, size, gravPull,gravVel, planetName):
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and 46 < mouse[0] < 206 and 644 < mouse[1] < 714:
                end = True

            if event.type == pygame.MOUSEBUTTONDOWN and 270 < mouse[0] < 435 and 100 < mouse[1] < 170:
                Planet.sizeUp(planetName)

        mouse = pygame.mouse.get_pos()

        gameDisplay.blit(background, [0,0])
        # Setting the variable texts
        title = infoTitle.render(Title, True, white)
        Mass = infoFont.render("The mass of the planet is: " + mass + "kg", True, white)
        Size = infoFont.render("The radius of the planet is: " + size, True, white)
        GravPull = infoFont.render("The gravitational pull is: " + gravPull + " m/s²", True, white)
        GravVel = infoFont.render("The gravitational velocity is: " + gravVel + " km/s", True, white)
        if 46 < mouse[0] < 206 and 644 < mouse[1] < 714:
            Back = buttonFont2.render("Back", True, mercuryCol)
        else:
            Back = buttonFont2.render("Back", True, white)

        sizeUp = buttonFont2.render("size +", True, white)
        # Inserting the text on the screen
        gameDisplay.blit(title, [50, 100])
        gameDisplay.blit(Mass, [50, 244])
        gameDisplay.blit(Size, [50, 344])
        gameDisplay.blit(GravPull, [50, 444])
        gameDisplay.blit(GravVel, [50, 544])
        gameDisplay.blit(Back, [50, 644])
        pygame.draw.rect(gameDisplay, lime, [270,100,165,70])
        gameDisplay.blit(sizeUp, [275, 100])
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

        gameDisplay.blit(background, [0,0])
        pygame.draw.rect(gameDisplay, black, [100, 530, 90, 55])
        gameDisplay.blit(menu, [114, 547])
        gameDisplay.blit(instruct, [290, 40])
        pygame.display.flip()


# Creates the function for the instructions
def play1():
    sunImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    MercuryImg = pygame.image.load(os.path.join('static', 'mercury.PNG'))
    VenusImg = pygame.image.load(os.path.join('static', 'venus.PNG'))
    EarthImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    MarsImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    JupiterImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    SaturnImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    UranusImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    NeptuneImg = pygame.image.load(os.path.join('static', 'sun.PNG'))
    # defining 'finish'
    finish = False
    # game program loop
    while not finish:
        sunImg = pygame.transform.scale(sunImg, [Sun.get_attr("radius") * 2, Sun.get_attr("radius") * 2])
        MercuryImg = pygame.transform.scale(MercuryImg, [Mercury.get_attr("radius") * 2, Mercury.get_attr("radius") * 2])
        VenusImg = pygame.transform.scale(VenusImg, [Venus.get_attr("radius") * 2, Venus.get_attr("radius") * 2])
        EarthImg = pygame.transform.scale(EarthImg, [Earth.get_attr("radius") * 2, Earth.get_attr("radius") * 2])
        MarsImg = pygame.transform.scale(MarsImg, [Mars.get_attr("radius") * 2, Mars.get_attr("radius") * 2])
        JupiterImg = pygame.transform.scale(JupiterImg, [Jupiter.get_attr("radius") * 2, Jupiter.get_attr("radius") * 2])
        SaturnImg = pygame.transform.scale(SaturnImg, [Saturn.get_attr("radius") * 2, Saturn.get_attr("radius") * 2])
        UranusImg = pygame.transform.scale(UranusImg, [Uranus.get_attr("radius") * 2, Uranus.get_attr("radius") * 2])
        NeptuneImg = pygame.transform.scale(NeptuneImg, [Neptune.get_attr("radius") * 2, Neptune.get_attr("radius") * 2])
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


                    factPage(title, mass, scale, gravPull, gravVel, planet)


        # selecting the Fonts
        menu = buttonFont.render("Menu", True, white)

        gameDisplay.blit(background, [0,0])
        # pygame.draw.circle(Sun) ~ ~ ~
        pygame.draw.rect(gameDisplay, lime, [100, 530, 90, 55])
        gameDisplay.blit(menu, [114, 547])
        Sun.render(gameDisplay, size, sunImg)
        Mercury.render(gameDisplay, size, MercuryImg)
        Venus.render(gameDisplay, size, VenusImg)
        Earth.render(gameDisplay, size, EarthImg)
        Mars.render(gameDisplay, size, MarsImg)
        Jupiter.render(gameDisplay, size, JupiterImg)
        Saturn.render(gameDisplay, size, SaturnImg)
        Uranus.render(gameDisplay, size, UranusImg)
        Neptune.render(gameDisplay, size, NeptuneImg)
        pygame.draw.rect(gameDisplay, lime, [40, 70, 180, 60])
        pygame.draw.rect(gameDisplay, lime, [40, 140, 180, 60])
        pygame.draw.rect(gameDisplay, lime, [40, 210, 180, 60])

        if Planet.speed(planets) == 0:
            direct = "Start"
        else:
            direct = "Stop"

        if 40 < mouse[0] < 220 and 70 < mouse[1] < 130:
            speedMore = optFont.render("+ Speed", True, mercuryCol)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render(direct, True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        elif 40 < mouse[0] < 220 and 140 < mouse[1] < 200:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, mercuryCol)
            Start = optFont.render(direct, True, white)
            gameDisplay.blit(speedMore, [40, 70])
            gameDisplay.blit(speedLess, [48, 140])
            gameDisplay.blit(Start, [75, 210])

        elif 40 < mouse[0] < 220 and 210 < mouse[1] < 270:
            speedMore = optFont.render("+ Speed", True, white)
            speedLess = optFont.render("- Speed", True, white)
            Start = optFont.render(direct, True, mercuryCol)
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
                planetName = optFont.render(name1, True, mercuryCol)
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

            if event.type == pygame.MOUSEBUTTONDOWN and a < mouse[0] < size[0] and 0 < mouse[1] and 30:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        # Game logic

        # Select font
        title = titleFont.render("Welcome To The Solar System", True, pink)

        if 190 < mouse[0] < 340 and 530 < mouse[1] < 610:
            play = buttonFont2.render("Play", True, mercuryCol)
            instruct = buttonFont2.render("Instructions", True, white)
        elif 690 < mouse[0] < 1060 and 530 < mouse[1] < 600:
            play = buttonFont2.render("Play", True, white)
            instruct = buttonFont2.render("Instructions", True, mercuryCol)
        else:
            play = buttonFont2.render("Play", True, white)
            instruct = buttonFont2.render("Instructions", True, white)

        # Drawing code here
        gameDisplay.blit(background, [0,0])
        pygame.draw.rect(gameDisplay, lime, [190, 530, 150, 80])
        pygame.draw.rect(gameDisplay, lime, [690, 530, 370, 70])
        gameDisplay.blit(title, [350, 100])
        gameDisplay.blit(play, [200, 530])
        gameDisplay.blit(instruct, [700, 530])
        a = size[0] - 30
        b = size[0] - a
        pygame.draw.rect(gameDisplay, lime, [a, 0, b, 30])
        pygame.display.flip()

    pygame.QUIT

password = input("Please enter the password - ")
hold = sha256(password.encode('utf-8')).hexdigest()
if hold != hashedPass:
    print("hi")
else:
    gameDisplay = pygame.display.set_mode(size)
    pygame.display.set_caption("Solar System")
    start()
