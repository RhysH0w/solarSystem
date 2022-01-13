import os
import pygame
pygame.init()

# Assign the colours
black = (0, 0, 0)
white = (255, 255, 255)
lime = (35, 225, 63)
pink = (255, 14, 156)
turquoise = (97, 231, 199)
mercury = (131, 134, 139)

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
