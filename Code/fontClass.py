"""
This file stores the properties and functionality of a font object.
"""

import pygame
pygame.init()


class Font:

    def __init__(self, inpPath, inpSize, inpColour, setUnderline = False):
        self.fontPath = inpPath
        self.fontSize = inpSize
        self.fontColour = inpColour
        self.rendFont = pygame.font.Font(self.fontPath, self.fontSize)

        if setUnderline:
            self.rendFont.set_underline(True)

    def getPath(self):
        return self.fontPath

    def getSize(self):
        return self.fontSize

    def getColour(self):
        return self.fontColour

    def getFont(self):
        return self.rendFont

    def setPath(self, inpPath):
        self.fontPath = inpPath

    def setSize(self, inpSize):
        self.fontSize = inpSize

    def setColour(self, inpColour):
        self.fontColour = inpColour

    def setFont(self):
        self.rendFont = pygame.font.Font(self.fontPath, self.fontSize)
