"""
This file stores the properties and functionality of a rectangle object.
"""

import pygame
pygame.init()


class Rectangle:

    E_COLOUR = (0, 0, 0)

    def __init__(self, inpScreen, inpWidth, inpHeight, inpColour):
        self.rectScreen = inpScreen
        self.rectWidth = inpWidth
        self.rectHeight = inpHeight
        self.rectColour = inpColour
        self.rectPyObj = None

    def getScreen(self):
        return self.rectScreen

    def getWidth(self):
        return self.rectWidth

    def getHeight(self):
        return self.rectHeight

    def getColour(self):
        return self.rectColour

    def setScreen(self, inpScreen):
        self.rectScreen = inpScreen

    def setWidth(self, inpWidth):
        self.rectWidth = inpWidth

    def setHeight(self, inpHeight):
        self.rectHeight = inpHeight

    def setColour(self, inpColour):
        self.rectColour = inpColour

    def setRectPyObj(self, inpPos):
        screenHeight = pygame.display.get_window_size()[1]
        rectLeftPos = self.rectWidth * inpPos
        rectTopPos = screenHeight - self.rectHeight
        self.rectPyObj = pygame.Rect(rectLeftPos, rectTopPos, self.rectWidth, self.rectHeight)

    def eraseRect(self, inpPos):
        origColour = self.rectColour
        self.setColour(Rectangle.E_COLOUR)
        self.drawRect(inpPos)
        self.setColour(origColour)

    def drawRect(self, inpPos):

        # Check if Rect obj is not set or leftPos has changed

        if not self.rectPyObj or self.rectPyObj.left != self.rectWidth * inpPos:
            self.setRectPyObj(inpPos)

        pygame.draw.rect(self.rectScreen, self.rectColour, self.rectPyObj)
        pygame.display.update(self.rectPyObj)
