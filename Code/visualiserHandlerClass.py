"""
This file stores the properties and functionality of a visualiser handler object.
"""


class VisualiserHandler:

    def __init__(self, inpRects, inpSortLabel, inpSoundState, inpAccs = None, inpComps = None):
        self.rectCollection = inpRects
        self.visSortLabels = inpSortLabel
        self.visSoundState = inpSoundState
        self.algoNumAccs = inpAccs
        self.algoNumComps = inpComps
        self.rectEndInd = 0
        self.visHaltState = False

    def getCollection(self):
        return self.rectCollection

    def getSortLabels(self):
        return self.visSortLabels

    def getSoundState(self):
        return self.visSoundState

    def getNumAccs(self):
        return self.algoNumAccs

    def getNumComps(self):
        return self.algoNumComps

    def getEndInd(self):
        return self.rectEndInd

    def getHaltState(self):
        return self.visHaltState

    def setCollection(self, inpRectCollection):
        self.rectCollection = inpRectCollection

    def setSoundState(self, inpSoundState):
        self.visSoundState = inpSoundState

    def setNumAccs(self, inpNumAccs):
        self.algoNumAccs = inpNumAccs

    def setNumComps(self, inpNumComps):
        self.algoNumComps = inpNumComps

    def setEndInd(self, inpRectEndInd):
        self.rectEndInd = inpRectEndInd

    def setHaltState(self, inpRectHaltState):
        self.visHaltState = inpRectHaltState
