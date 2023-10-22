"""
This file stores the properties and functionality of a label object.
"""

from labelClass import Label

import pygame
pygame.init()

WHITE = (255, 255, 255)


class Button(Label):

    def __init__(self, inpScreen, inpWidth, inpHeight, inpBackColour, inpCaption, inpLeftPos, inpTopPos, inpFont, inpBorderColour, inpSFX, inpAnchor = None):
        super().__init__(inpScreen, inpWidth, inpHeight, inpBackColour, inpCaption, inpLeftPos, inpTopPos, inpFont, inpBorderColour, inpAnchor)
        self.buttonSFX = inpSFX
        self.buttonHandler = None

    def getSFX(self):
        return self.buttonSFX

    def getHandler(self):
        return self.buttonHandler

    def setSFX(self, inpSFX):
        self.buttonSFX = inpSFX

    def setHandler(self, inpHandler):
        self.buttonHandler = inpHandler

    def checkInBounds(self):
        pygame.event.poll()
        mouseXPos, mouseYPos = pygame.mouse.get_pos()

        mouseXBound = self.getLeftPos() + self.getWidth() > mouseXPos > self.getLeftPos()
        mouseYBound = self.getTopPos() + self.getHeight() > mouseYPos > self.getTopPos()

        return mouseXBound, mouseYBound

    def onHoverColourChange(self):
        buttonClicked = False
        mouseXPos, mouseYPos = self.checkInBounds()
        backColour, foreColour = self.getColour(), self.getBorderColour()

        while mouseXPos and mouseYPos:
            self.inverseColours(backColour, foreColour)

            if pygame.mouse.get_pressed(3)[0]:
                buttonClicked = True
                break

            mouseXPos, mouseYPos = self.checkInBounds()

        self.inverseColours(foreColour, backColour)

        return True if buttonClicked else None

    def onHoverFontChange(self):
        buttonClicked = False
        mouseXPos, mouseYPos = self.checkInBounds()
        origFontSize = self.getFont().getSize()
        origFontColour = self.getFont().getColour()

        while mouseXPos and mouseYPos:
            self.getFont().setSize(round(origFontSize * 1.5))
            self.getFont().setColour(WHITE)
            self.getFont().setFont()
            self.displayWidget()

            if pygame.mouse.get_pressed(3)[0]:
                buttonClicked = True
                break

            mouseXPos, mouseYPos = self.checkInBounds()

        self.labelFont.setSize(origFontSize)
        self.labelFont.setColour(origFontColour)
        self.labelFont.setFont()
        self.displayWidget()

        return True if buttonClicked else None

    def inverseColours(self, colourOne, colourTwo):
        self.setBorderColour(colourOne)
        self.labelFont.setColour(colourOne)
        self.setColour(colourTwo)
        self.displayWidget()

    def playSFX(self):
        pass
