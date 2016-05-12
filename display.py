__author__ = 'Mars'
import pygame
from pygame.locals import *
screen = pygame.display.set_mode([1024,768])
screen = pygame.display.set_mode((1024, 768), FULLSCREEN)
monster = pygame.image.load('C:\Users\Mars\Documents\Classes\HFOSS\PokeMath\PokeMath\images\Green-Monster.png')
screen.blit(monster,(50,100))
#pygame.display.flip()

class MonsterSprite:
    def __init__(image, self):
        self.image = image

class Button:
    def __init__(text, self):
        self.text = text

