"""
This file stores the properties and functionality of a widget object.
"""

import pygame
pygame.init()


class Label:

    def __init__(self, inpScreen, inpWidth, inpHeight, inpBackColour, inpCaption, inpLeftPos, inpTopPos, inpFont, inpBorderColour, inpAnchor = None):
        self.labelScreen = inpScreen
        self.labelWidth = inpWidth
        self.labelHeight = inpHeight
        self.labelColour = inpBackColour
        self.labelCaption = inpCaption
        self.labelLeftPos = inpLeftPos
        self.labelTopPos = inpTopPos
        self.labelFont = inpFont
        self.labelBorderColour = inpBorderColour
        self.labelAnchor = inpAnchor
        self.labelPyObj = pygame.Rect(self.labelLeftPos, self.labelTopPos, self.labelWidth, self.labelHeight)

    def getScreen(self):
        return self.labelScreen

    def getWidth(self):
        return self.labelWidth

    def getHeight(self):
        return self.labelHeight

    def getColour(self):
        return self.labelColour

    def getCaption(self):
        return self.labelCaption

    def getLeftPos(self):
        return self.labelLeftPos

    def getTopPos(self):
        return self.labelTopPos

    def getFont(self):
        return self.labelFont

    def getBorderColour(self):
        return self.labelBorderColour

    def getAnchor(self):
        return self.labelAnchor

    def setScreen(self, inpScreen):
        self.labelScreen = inpScreen

    def setWidth(self, inpWidth):
        self.labelWidth = inpWidth

    def setHeight(self, inpHeight):
        self.labelHeight = inpHeight

    def setColour(self, inpColour):
        self.labelColour = inpColour

    def setCaption(self, inpCaption):
        self.labelCaption = inpCaption

    def setLeftPos(self, inpPos):
        self.labelLeftPos = inpPos

    def setTopPos(self, inpPos):
        self.labelTopPos = inpPos

    def setFont(self, inpFont):
        self.labelFont = inpFont

    def setBorderColour(self, inpColour):
        self.labelBorderColour = inpColour

    def setAnchor(self, inpAnchor):
        self.labelAnchor = inpAnchor

    def displayWidget(self):
        pygame.draw.rect(self.labelScreen, self.labelColour, self.labelPyObj, 0)
        pygame.draw.rect(self.labelScreen, self.labelBorderColour, self.labelPyObj, 1)

        # Declare surface and rectangle for text

        labelCapSurf = self.labelFont.rendFont.render(self.labelCaption, True, self.labelFont.getColour())
        labelCapRect = labelCapSurf.get_rect()

        # Center text on rectangle

        xCenterPos = self.labelLeftPos + (self.labelWidth // 2)
        yCenterPos = self.labelTopPos + (self.labelHeight // 2)
        labelCapRect.center = (xCenterPos, yCenterPos)

        if self.labelAnchor == "LEFT":
            labelCapRect.left = self.labelLeftPos + 5

        self.labelScreen.blit(labelCapSurf, labelCapRect)
        pygame.display.update(labelCapRect)
