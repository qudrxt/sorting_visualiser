"""
This file stores the sorting algorithms used by the visualiser.
"""

from rectangleClass import Rectangle
from visualiserHandlerClass import VisualiserHandler
from typing import List
from math import floor

import threading
import winsound
import pathlib
import pygame
import math
import sys
pygame.init()

filePath = str(pathlib.Path().absolute())
labelSFX = filePath[:len(filePath)-4] + "Misc\\labelSFX.wav"

minFreq, maxFreq, maxDiff = 6000, 12000, 500
WHITE, GREEN = (255, 255, 255), (0, 255, 0)


                                        # <-- ITERATIVE ALGORITHMS --> #


def bubbleSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()

    for i in range(len(rectList)):

        for j in range(1, len(rectList)-i):
            if eventHandler(visHandObj):
                visHandObj.setEndInd(len(rectList))
                visHandObj.setHaltState(True)
                return

            elif rectList[j].getHeight() < rectList[j-1].getHeight():
                swapVisually(visHandObj, rectList[j], j, rectList[j-1], j-1)
                swapInternally(rectList, j, j-1)

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)
            visHandObj.setNumComps(visHandObj.getNumComps() + 1)

            if j % 5 == 0:
                detailHandler(visHandObj)

    if rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def combSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()
    rectGap, rectSwap = len(rectList), True

    while rectGap > 1 or rectSwap:
        rectGap, rectSwap = max(1, int(rectGap / 1.3)), False

        for i in range(len(rectList) - rectGap):
            if eventHandler(visHandObj):
                visHandObj.setEndInd(len(rectList))
                visHandObj.setHaltState(True)
                return

            elif rectList[i].getHeight() > rectList[i + rectGap].getHeight():
                swapVisually(visHandObj, rectList[i], i, rectList[i + rectGap], i + rectGap)
                swapInternally(rectList, i, i + rectGap)
                rectSwap = True

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)
            visHandObj.setNumComps(visHandObj.getNumComps() + 1)

            if (i + 1) % 5 == 0:
                detailHandler(visHandObj)

    if rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def insertionSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()

    for i in range(len(rectList)):
        j = i

        while j > 0 and rectList[j].getHeight() < rectList[j-1].getHeight():
            if eventHandler(visHandObj):
                visHandObj.setEndInd(i)
                visHandObj.setHaltState(True)
                return

            swapVisually(visHandObj, rectList[j], j, rectList[j-1], j-1)
            swapInternally(rectList, j, j-1)
            j -= 1

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)
            visHandObj.setNumComps(visHandObj.getNumComps() + 1)

            if (j + 1) % 5 == 0:
                detailHandler(visHandObj)

    if rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def selectionSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()

    for i in range(len(rectList)):
        minInd = i

        for j in range(i + 1, len(rectList)):
            if eventHandler(visHandObj):
                visHandObj.setEndInd(i)
                visHandObj.setHaltState(True)
                return

            elif rectList[j].getHeight() < rectList[minInd].getHeight():
                minInd = j

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)
            visHandObj.setNumComps(visHandObj.getNumComps() + 1)

        if i != minInd:
            swapVisually(visHandObj, rectList[i], i, rectList[minInd], minInd)
            swapInternally(rectList, i, minInd)

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

        if (i + 1) % 5 == 0:
            detailHandler(visHandObj)

    if rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def countingSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()
    apexRect = max(rectList, key = lambda x: x.getHeight())
    rectFreq = {i: 0 for i in range(apexRect.getHeight() + 1)}

    for subRect in rectList:
        rectFreq[subRect.getHeight()] += 1

    sanitisedFreq = [value for key, value in rectFreq.items()]

    for i in range(1, len(sanitisedFreq)):
        sanitisedFreq[i] += sanitisedFreq[i-1]

    for i in range(len(sanitisedFreq)-1, 0, -1):
        sanitisedFreq[i] = sanitisedFreq[i-1]

    sanitisedFreq[0] = 0
    startInds = {i: sanitisedFreq[i] for i in range(len(sanitisedFreq))}
    auxRectList = [None for _ in range(len(rectList))]

    for i in range(len(rectList)):
        indexToErase = startInds[rectList[i].getHeight()]
        auxRectList[indexToErase] = rectList[i]
        startInds[rectList[i].getHeight()] += 1

    for _ in range(4):

        for i in range(len(rectList)):
            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

            if (i + 1) % 5 == 0:
                detailHandler(visHandObj)

    for i in range(len(auxRectList)):
        if eventHandler(visHandObj):
            visHandObj.setCollection(auxRectList[:i] + rectList[i:])
            visHandObj.setEndInd(i)
            visHandObj.setHaltState(True)
            return

        modifyVisually(rectList[i], auxRectList[i], i, visHandObj.getSoundState())
        visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

        if (i + 1) % 5 == 0:
            detailHandler(visHandObj)

    visHandObj.setCollection(auxRectList)

    if auxRectList[0].getColour() == WHITE:
        colourSortedRects(visHandObj.getCollection())


def radixSort(visHandObj: VisualiserHandler, inpBase: int = 10):
    maxPos = int((math.log(max(visHandObj.getCollection(), key = lambda x: x.getHeight()).getHeight(), inpBase)) + 1)

    for i in range(maxPos):
        if visHandObj.getHaltState():
            return

        radixSubroutine(visHandObj.getCollection(), visHandObj, i, inpBase)

    if visHandObj.getCollection()[0].getColour() == WHITE:
        colourSortedRects(visHandObj.getCollection())


def calcDigit(inpNumber: int, inpDigit: int, inpBase: int):
    return (inpNumber // inpBase ** inpDigit) % inpBase


def radixSubroutine(rectList: List[Rectangle], visHandObj: VisualiserHandler, digitValue: int, baseValue: int = 10):
    freqList = [0 for _ in range(baseValue)]
    returnList = [None for _ in range(len(rectList))]

    # Count the frequency of each element

    for subRect in rectList:
        freqList[calcDigit(subRect.getHeight(), digitValue, baseValue)] += 1

    # Pre-processing computation

    for i in range(1, len(freqList)):
        freqList[i] += freqList[i-1]

    for j in range(len(freqList)-1, 0, -1):
        freqList[j] = freqList[j-1]

    freqList[0] = 0

    for _ in range(4):

        for i in range(len(rectList)):
            if eventHandler(visHandObj):
                visHandObj.setEndInd(len(rectList))
                visHandObj.setHaltState(True)
                return

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

            if (i + 1) % 5 == 0:
                detailHandler(visHandObj)

    for i in range(len(rectList)):
        rectPos = calcDigit(rectList[i].getHeight(), digitValue, baseValue)
        returnList[freqList[rectPos]] = rectList[i]

        modifyVisually(rectList[freqList[rectPos]], returnList[freqList[rectPos]], freqList[rectPos], visHandObj.getSoundState())
        visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

        freqList[rectPos] += 1

        if (i + 1) % 5 == 0:
            detailHandler(visHandObj)

    visHandObj.setCollection(returnList)


def shakerSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()

    for boundaryInd in range(len(rectList)):
        startInd = len(rectList)-boundaryInd-1
        endInd = len(rectList)-boundaryInd
        loopParas = [[1, endInd, 1], [startInd, 0, -1]]

        for para in range(len(loopParas)):
            startPos = loopParas[para][0]
            endPos = loopParas[para][1]
            stepVal = loopParas[para][2]

            for i in range(startPos, endPos, stepVal):
                if eventHandler(visHandObj):
                    visHandObj.setEndInd(len(rectList))
                    visHandObj.setHaltState(True)
                    return

                elif rectList[i].getHeight() < rectList[i-1].getHeight():
                    swapVisually(visHandObj, rectList[i], i, rectList[i-1], i-1)
                    swapInternally(rectList, i, i-1)

                visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)
                visHandObj.setNumComps(visHandObj.getNumComps() + 1)

                if (i + 1) % 5 == 0:
                    detailHandler(visHandObj)

    if rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def shellSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()
    rectGap = len(rectList) // 2

    while rectGap > 0:

        for i in range(rectGap, len(rectList)):
            j = i

            while j >= rectGap and rectList[j].getHeight() < rectList[j-rectGap].getHeight():
                if eventHandler(visHandObj):
                    visHandObj.setEndInd(len(rectList))
                    visHandObj.setHaltState(True)
                    return

                swapVisually(visHandObj, rectList[j], j, rectList[j-rectGap], j-rectGap)
                swapInternally(rectList, j, j-rectGap)
                j -= rectGap

                visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)
                visHandObj.setNumComps(visHandObj.getNumComps() + 1)

                if (j + 1) % 5 == 0:
                    detailHandler(visHandObj)

        rectGap //= 2

    if rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


                                        # <-- RECURSIVE ALGORITHMS --> #


def quickSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()
    quickSortAux(visHandObj, rectList, 0, len(rectList)-1)

    if not visHandObj.getHaltState() and rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def quickSortAux(visHandObj: VisualiserHandler, rectList: List[Rectangle], startInd, endInd):
    if startInd >= endInd:
        return

    sortedInd = partition(visHandObj, rectList, startInd, endInd)

    if visHandObj.getHaltState():
        return

    quickSortAux(visHandObj, rectList, startInd, sortedInd-1)
    quickSortAux(visHandObj, rectList, sortedInd+1, endInd)


def partition(visHandObj: VisualiserHandler, rectList: List[Rectangle], startInd, endInd):
    pivotInd = (startInd + endInd) // 2
    pivotRect = rectList[pivotInd]
    boundaryInd = startInd

    if not visHandObj.getHaltState():

        swapVisually(visHandObj, rectList[startInd], startInd, pivotRect, pivotInd)
        swapInternally(rectList, startInd, pivotInd)

        visHandObj.setNumAccs(visHandObj.getNumAccs() + 1)

        for i in range(startInd + 1, endInd + 1):
            if eventHandler(visHandObj):
                visHandObj.setEndInd(len(rectList))
                visHandObj.setHaltState(True)
                return

            elif rectList[i].getHeight() < pivotRect.getHeight():
                boundaryInd += 1
                swapVisually(visHandObj, rectList[boundaryInd], boundaryInd, rectList[i], i)
                swapInternally(rectList, boundaryInd, i)

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 1)
            visHandObj.setNumComps(visHandObj.getNumComps() + 1)

            if (i + 1) % 5 == 0:
                detailHandler(visHandObj)

    if not visHandObj.getHaltState():
        swapVisually(visHandObj, rectList[startInd], startInd, rectList[boundaryInd], boundaryInd)
        swapInternally(rectList, startInd, boundaryInd)
        return boundaryInd


def mergeSort(visHandObj: VisualiserHandler):
    rectList = visHandObj.getCollection()
    mergeSortAux(visHandObj, rectList, 0, len(rectList)-1, [None for _ in range(len(rectList))])

    if not visHandObj.getHaltState() and rectList[0].getColour() == WHITE:
        colourSortedRects(rectList)


def mergeSortAux(visHandObj: VisualiserHandler, rectList: List[Rectangle], startInd, endInd, auxList):
    if startInd >= endInd or visHandObj.getHaltState():
        return

    midInd = (startInd + endInd) // 2
    mergeSortAux(visHandObj, rectList, startInd, midInd, auxList)
    mergeSortAux(visHandObj, rectList, midInd + 1, endInd, auxList)
    merge(visHandObj, rectList, startInd, midInd, endInd, auxList)

    if not visHandObj.getHaltState():

        # auxList is sorted -> copy its content to rectList

        for i in range(startInd, endInd + 1):
            if eventHandler(visHandObj):
                visHandObj.setEndInd(endInd)
                visHandObj.setHaltState(True)
                return

            modifyVisually(rectList[i], auxList[i], i, visHandObj.getSoundState())
            rectList[i] = auxList[i]

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

            if (i + 1) % 5 == 0:
                detailHandler(visHandObj)


def merge(visHandObj: VisualiserHandler, rectList: List[Rectangle], startInd: int, midInd: int, endInd: int, auxList):

    # midInd and endInd are inclusive for leftInd and rightInd

    curInd, destInd, leftInd, rightInd = 0, startInd, startInd, midInd + 1

    if not visHandObj.getHaltState():

        while leftInd <= midInd and rightInd <= endInd:
            if eventHandler(visHandObj):
                visHandObj.setEndInd(endInd)
                visHandObj.setHaltState(True)
                return

            elif rectList[leftInd].getHeight() < rectList[rightInd].getHeight():
                auxList[destInd] = rectList[leftInd]
                leftInd += 1

            else:
                auxList[destInd] = rectList[rightInd]
                rightInd += 1

            curInd += 1
            destInd += 1

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 3)
            visHandObj.setNumComps(visHandObj.getNumComps() + 1)

            if (curInd + 1) % 5 == 0:
                detailHandler(visHandObj)

    if not visHandObj.getHaltState():
        remainInd = leftInd if leftInd <= midInd else rightInd
        boundInd = midInd if leftInd <= midInd else endInd

        while remainInd <= boundInd:
            if eventHandler(visHandObj):
                visHandObj.setEndInd(remainInd)
                visHandObj.setHaltState(True)
                return

            auxList[destInd] = rectList[remainInd]
            remainInd += 1
            curInd += 1
            destInd += 1

            visHandObj.setNumAccs(visHandObj.getNumAccs() + 2)

            if curInd % 5 == 0:
                detailHandler(visHandObj)


                                    # <-- AUXILIARY & DRAWING METHODS --> #


def modifyVisually(rectOne: Rectangle, rectTwo: Rectangle, rectInd, playSortSound):
    if playSortSound:
        beepFreq = getFrequency(rectTwo.getHeight())
        soundThread = threading.Thread(target = sortSort, args = (beepFreq, 100, ))
        soundThread.start()

    rectOne.eraseRect(rectInd)
    rectTwo.drawRect(rectInd)


def swapVisually(visHandObj: VisualiserHandler, rectOne: Rectangle, indOne, rectTwo: Rectangle, indTwo) -> None:
    playSortSound = visHandObj.getSoundState()
    modifyVisually(rectOne, rectTwo, indOne, playSortSound)
    modifyVisually(rectTwo, rectOne, indTwo, playSortSound)


def swapInternally(rectList: List[Rectangle], indOne, indTwo) -> None:
    rectList[indOne], rectList[indTwo] = rectList[indTwo], rectList[indOne]


def signifySorted(sortedRect: Rectangle, rectInd) -> None:
    sortedRect.setColour(GREEN)
    sortedRect.drawRect(rectInd)


def colourSortedRects(sortedRectList) -> None:
    for i in range(len(sortedRectList)):
        checkEvents()
        signifySorted(sortedRectList[i], i)


def detailHandler(visHandObj: VisualiserHandler):
    sortDetails = visHandObj.getSortLabels()
    sortDetails[1].setCaption(f"Array Accesses | {visHandObj.getNumAccs()}")
    sortDetails[2].setCaption(f"Comparisons | {visHandObj.getNumComps()}")

    sortDetails[1].displayWidget()
    sortDetails[2].displayWidget()


def sortSort(beepFreq, beepDur):
    winsound.Beep(beepFreq, beepDur)

    # Incur delay for better pronounced beeps

    pygame.time.delay(100)


def getFrequency(rectHeight):
    return floor((rectHeight / maxDiff) * (maxFreq - minFreq)) + minFreq


def checkEvents():
    for keyEvent in pygame.event.get():
        if keyEvent.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif keyEvent.type == pygame.KEYDOWN:
            if keyEvent.key == pygame.K_p:
                return "Pause"
            
            elif keyEvent.key == pygame.K_m:
                return "Menu"


def eventHandler(visHandObj: VisualiserHandler):
    buttonPressed = checkEvents()

    if buttonPressed:

        if visHandObj.getSoundState():
            winsound.PlaySound(labelSFX, winsound.SND_ALIAS)

        if buttonPressed == "Pause":
            visPaused = True

            while visPaused:
                buttonPressed = checkEvents()

                if buttonPressed == "Pause":
                    visPaused = False

                    if visHandObj.getSoundState():
                        winsound.PlaySound(labelSFX, winsound.SND_ALIAS)

        elif buttonPressed == "Menu":
            visHandObj.setHaltState(True)
            return True
