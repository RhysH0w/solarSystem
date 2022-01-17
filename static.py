import os
import pygame
pygame.init()

# Assign the colours
black = (0, 0, 0)
white = (255, 255, 255)
lime = (35, 225, 63)
pink = (255, 14, 156)
turquoise = (97, 231, 199)

sunCol = (237, 88, 26)
mercuryCol = (131, 134, 139)
venusCol = (231, 227, 224)
earthCol = (58, 65, 86)
marsCol = (253, 133, 96)
jupiterCol = (217, 199, 176)
saturnCol = (178, 167, 122)
uranusCol = (143, 161, 171)
neptuneCol = (108, 139, 183)

sizeInfo = pygame.display.Info()
size = (sizeInfo.current_w, sizeInfo.current_h)

centrex = size[0]/2
centrey = size[1]/2

infoFont = pygame.font.Font(os.path.join("static", "Slabo.ttf"), 50)
infoTitle = pygame.font.Font(os.path.join("static", "Slabo.ttf"), 60)
titleFont = pygame.font.SysFont('Calibri', 40, True, False)
buttonFont = pygame.font.SysFont('Calibri', 25, True, False)
optFont = pygame.font.Font(os.path.join("static", "Montserrat.ttf"), 45)
buttonFont2 = pygame.font.Font(os.path.join("static", "Montserrat.ttf"), 60)

background = pygame.image.load(os.path.join('static', 'solar_system_back.jpg'))
background = pygame.transform.scale(background, size)

a = size[0] - 30
b = size[0] - a

hashedPass = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" # This is a series of encoded characters that is used to compare to the encoded password




