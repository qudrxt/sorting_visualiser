"""
This file stores the properties and functionality of a button handler object.
"""


class ButtonHandler:

    def __init__(self, inpLabels, inpWidgets):
        self.buttonLabels = inpLabels
        self.buttonWidgets = inpWidgets
        self.buttonInd = 0

    def getLabels(self):
        return self.buttonLabels

    def getWidgets(self):
        return self.buttonWidgets

    def setLabels(self, inpLabels):
        self.buttonLabels = inpLabels

    def setWidgets(self, inpWidgets):
        self.buttonWidgets = inpWidgets

    def changeLabel(self, inpButton):
        buttonChangeValue = -1 if inpButton == self.buttonWidgets[0] else 1
        self.buttonInd = (self.buttonInd + buttonChangeValue) % len(self.buttonLabels)
        self.buttonWidgets[1].setCaption(self.buttonLabels[self.buttonInd])
        self.buttonWidgets[1].displayWidget()
