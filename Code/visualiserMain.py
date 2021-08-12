"""
This file stores, constructs and executes the visualiser and its properties.
"""

from buttonClass import Button
from buttonHandlerClass import ButtonHandler
from fontClass import Font
from labelClass import Label
from sortingAlgorithms import *

import random
import sys
import pathlib
import pygame
pygame.init()


sortingAlgos = [("Bubble Sort", bubbleSort), ("Comb Sort", combSort), ("Counting Sort", countingSort),
                ("Insertion Sort", insertionSort), ("Merge Sort", mergeSort), ("Quick Sort", quickSort),
                ("Radix Sort", radixSort), ("Selection Sort", selectionSort), ("Shaker Sort", shakerSort),
                ("Shell Sort", shellSort)]

widthLabels, modeLabels, soundLabels = ["Thin", "Moderate", "Thick"], ["Standard", "Gradient"], ["On", "Off"]

BLACK, WHITE, GREY = (0, 0, 0), (255, 255, 255), (191, 191, 191)
DIM_WHITE, RED, GREEN = (230, 230, 230), (255, 0, 0), (0, 255, 0)
BLUE = (0, 0, 255)

filePath = str(pathlib.Path().absolute())
lightFontPath = filePath[:len(filePath)-4] + "Misc\\TafelSansPro-Light.ttf"
regularFontPath = filePath[:len(filePath)-4] + "Misc\\TafelSansPro-Regular.ttf"

exButtonSFX = filePath[:len(filePath)-4] + "Misc\\exButtonSFX.wav"
imButtonSFX = filePath[:len(filePath)-4] + "Misc\\imButtonSFX.wav"

exWidgetFont, imButtonFont = Font(lightFontPath, 20, WHITE), Font(lightFontPath, 25, GREY)
optionLabelFont, titleFont = Font(lightFontPath, 20, DIM_WHITE), Font(regularFontPath, 20, WHITE, True)
mainDetailFont, subDetailFont = Font(regularFontPath, 15, WHITE), Font(lightFontPath, 15, WHITE)

visWindow = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Sorting Visualiser")
pygame.display.flip()

sortButton = Button(visWindow, 100, 40, BLACK, "Sort", 537.5, 50, exWidgetFont, WHITE, exButtonSFX)
optionsButton = Button(visWindow, 100, 40, BLACK, "Options", 642.5, 50, exWidgetFont, WHITE, exButtonSFX)

pauseLabel = Label(visWindow, 100, 40, BLACK, "Pause (P)", 537.5, 50, exWidgetFont, BLACK)
menuLabel = Label(visWindow, 100, 40, BLACK, "Menu (M)", 642.5, 50, exWidgetFont, BLACK)

repeatButton = Button(visWindow, 100, 40, BLACK, "Repeat", 537.5, 50, exWidgetFont, WHITE, exButtonSFX)
menuButton = Button(visWindow, 100, 40, BLACK, "Menu", 642.5, 50, exWidgetFont, WHITE, exButtonSFX)

prevAlgoButton = Button(visWindow, 20, 40, BLACK, "<", 50, 50, imButtonFont, BLACK, imButtonSFX)
algoLabel = Label(visWindow, 200, 40, BLACK, "Bubble Sort", 70, 50, optionLabelFont, BLACK)
algoTitle = Label(visWindow, 200, 40, BLACK, "Algorithm", 70, 10, titleFont, BLACK)
nextAlgoButton = Button(visWindow, 20, 40, BLACK, ">", 270, 50, imButtonFont, BLACK, imButtonSFX)
algoButtons = [prevAlgoButton, algoLabel, nextAlgoButton]
algoHandler = ButtonHandler([algoPair[0] for algoPair in sortingAlgos], algoButtons)

prevModeButton = Button(visWindow, 20, 40, BLACK, "<", 310, 50, imButtonFont, BLACK, imButtonSFX)
modeLabel = Label(visWindow, 200, 40, BLACK, "Standard", 330, 50, optionLabelFont, BLACK)
modeTitle = Label(visWindow, 200, 40, BLACK, "Mode", 330, 10, titleFont, BLACK)
nextModeButton = Button(visWindow, 20, 40, BLACK, ">", 530, 50, imButtonFont, BLACK, imButtonSFX)
modeButtons = [prevModeButton, modeLabel, nextModeButton]
modeHandler = ButtonHandler(modeLabels, modeButtons)

prevWidthButton = Button(visWindow, 20, 40, BLACK, "<", 570, 50, imButtonFont, BLACK, imButtonSFX)
widthLabel = Label(visWindow, 200, 40, BLACK, "Thin", 590, 50, optionLabelFont, BLACK)
widthTitle = Label(visWindow, 200, 40, BLACK, "Width", 590, 10, titleFont, BLACK)
nextWidthButton = Button(visWindow, 20, 40, BLACK, ">", 790, 50, imButtonFont, BLACK, imButtonSFX)
widthButtons = [prevWidthButton, widthLabel, nextWidthButton]
widthHandler = ButtonHandler(widthLabels, widthButtons)

prevSoundButton = Button(visWindow, 20, 40, BLACK, "<", 830, 50, imButtonFont, BLACK, imButtonSFX)
soundLabel = Label(visWindow, 200, 40, BLACK, "On", 850, 50, optionLabelFont, BLACK)
soundTitle = Label(visWindow, 200, 40, BLACK, "Sound", 850, 10, titleFont, BLACK)
nextSoundButton = Button(visWindow, 20, 40, BLACK, ">", 1050, 50, imButtonFont, BLACK, imButtonSFX)
soundButtons = [prevSoundButton, soundLabel, nextSoundButton]
soundHandler = ButtonHandler(soundLabels, soundButtons)

applyButton = Button(visWindow, 100, 40, BLACK, "Apply", 1125, 50, exWidgetFont, WHITE, exButtonSFX)

sortLabel = Label(visWindow, 175, 30, BLACK, "Algorithm | Bubble Sort", 10, 10, mainDetailFont, BLACK, "LEFT")
accessLabel = Label(visWindow, 185, 30, BLACK, "Array Accesses | 0", 10, 40, subDetailFont, BLACK, "LEFT")
compLabel = Label(visWindow, 175, 30, BLACK, "Comparisons | 0", 10, 70, subDetailFont, BLACK, "LEFT")
rectAmtLabel = Label(visWindow, 175, 30, BLACK, "Elements | 1280", 10, 100, subDetailFont, BLACK, "LEFT")

startMenuButtons, duringSortLabels = [sortButton, optionsButton], [pauseLabel, menuLabel]
sortDetailLabels, postSortButtons = [sortLabel, accessLabel, compLabel, rectAmtLabel], [repeatButton, menuButton]
optionMenuTitles = [algoTitle, modeTitle, widthTitle, soundTitle]

optionMenuWidgets = [prevAlgoButton, algoLabel, nextAlgoButton, prevWidthButton, widthLabel, nextWidthButton, nextSoundButton,
                     soundLabel, prevSoundButton, prevModeButton, modeLabel, nextModeButton, applyButton]

optionMenuButtons = [prevAlgoButton, nextAlgoButton, prevWidthButton, nextWidthButton, prevSoundButton, nextSoundButton,
                     prevModeButton, nextModeButton]

algoDict, modeDict = {algoName: algoFunc for algoName, algoFunc in sortingAlgos}, {"Standard": False, "Gradient": True}
widthDict, soundDict = {"Thin": 1, "Moderate": 2, "Thick": 4}, {"On": True, "Off": False}

visAlgo, visMode = algoDict[algoLabel.getCaption()], modeDict[modeLabel.getCaption()]
rectWidth, visSound = widthDict[widthLabel.getCaption()], soundDict[soundLabel.getCaption()]

visRects = [Rectangle(visWindow, rectWidth, random.randrange(20, 580), WHITE) for _ in range(1280 // rectWidth)]
visHandler = VisualiserHandler(visRects, sortDetailLabels, soundDict[soundLabel.getCaption()])


def visLoop():
    setHandler(algoButtons, algoHandler)
    setHandler(widthButtons, widthHandler)
    setHandler(soundButtons, soundHandler)
    setHandler(modeButtons, modeHandler)

    initialRun, widthChanged, modeChanged = True, False, False

    while True:
        eraseWidgets()
        displayWidgets(startMenuButtons)

        if initialRun:
            displayRects()

        elif widthChanged:
            eraseRects()
            displayRects()

        elif modeChanged:
            displayRects()

        initialRun, optionSelected = False, False
        widthChanged, modeChanged = False, False
        startMenuButton = None

        while not optionSelected:
            startMenuButton = buttonColourEffect(startMenuButtons)

            if startMenuButton is not None:
                checkSound(startMenuButton)
                optionSelected = True

        if startMenuButton == sortButton:
            repeatSort = True

            while repeatSort:
                eraseWidgets(False)
                displayWidgets(sortDetailLabels + duringSortLabels)
                visHandler.setNumAccs(0)
                visHandler.setNumComps(0)
                visAlgo(visHandler)

                if visHandler.getHaltState():
                    visHandler.setHaltState(False)
                    eraseDetails()
                    eraseWidgets(False)
                    shuffleRects(visHandler.getEndInd())
                    break

                eraseWidgets(False)
                displayWidgets(postSortButtons)
                optionSelected, postSortButton = False, None

                while not optionSelected:
                    postSortButton = buttonColourEffect(postSortButtons)

                    if postSortButton is not None:
                        checkSound(postSortButton)
                        optionSelected = True

                if postSortButton == menuButton:
                    repeatSort = False

                if not visMode:
                    resetColour()

                eraseWidgets(False)
                eraseDetails()
                shuffleRects()

        elif startMenuButton == optionsButton:
            optionSelected = False
            eraseWidgets(False)
            displayWidgets(optionMenuTitles)
            displayWidgets(optionMenuWidgets)
            buttonEffects = [buttonFontEffect, buttonColourEffect]
            buttonEffectArgs = [optionMenuButtons, [applyButton]]
            prevWidth, prevMode = widthLabel.getCaption(), modeLabel.getCaption()

            while not optionSelected:

                for i in range(len(buttonEffects)):
                    buttonEffect = buttonEffects[i]
                    buttonList = buttonEffectArgs[i]
                    optionMenuButton = buttonEffect(buttonList)

                    if optionMenuButton and optionMenuButton != applyButton:
                        checkSound(optionMenuButton)
                        optionButtonHandler = optionMenuButton.getHandler()
                        optionButtonHandler.changeLabel(optionMenuButton)

                    elif optionMenuButton == applyButton:
                        checkSound(optionMenuButton)
                        optionSelected = True
                        break

            if prevWidth != widthLabel.getCaption():
                widthChanged = True

            if prevMode != modeLabel.getCaption():
                modeChanged = True

            formHandler(widthChanged, modeChanged)


def formHandler(changeWidth, changeMode):
    global visRects, visAlgo, visMode, rectWidth, visSound
    visAlgo = algoDict[algoLabel.getCaption()]
    visMode = modeDict[modeLabel.getCaption()]
    rectWidth = widthDict[widthLabel.getCaption()]
    visSound = soundDict[soundLabel.getCaption()]
    visHandler.setSoundState(visSound)
    sortLabel.setCaption(f"Algorithm | {algoLabel.getCaption()}")
    rectAmtLabel.setCaption(f"Elements | {1280 // rectWidth}")

    if changeWidth:
        visRects = [Rectangle(visWindow, rectWidth, random.randrange(20, 580), WHITE) for _ in range(1280 // rectWidth)]
        setGradientMode(genGradPalette()) if visMode else None
        visHandler.setCollection(visRects)

    elif changeMode:
        setGradientMode(genGradPalette()) if visMode else resetColour()


def genGradPalette():
    gradPalette = []
    minValue, maxValue = 0, 1
    gradientSteps = len(visRects) // 2
    deltaValue = (maxValue - minValue) / gradientSteps
    initColours = list((list(zip(RED, GREEN)), (list(zip(GREEN, BLUE)))))

    for i in range(len(initColours)):

        for j in range(gradientSteps):
            timeOffset = minValue + j * deltaValue
            interColour = []

            for k in range(len(initColours[i])):
                startColour, endColour = initColours[i][k][0], initColours[i][k][1]
                interColour.append(interpolateColour(startColour, endColour, timeOffset))

            gradPalette.append(interColour)

    return gradPalette


def interpolateColour(startPoint, endPoint, timeValue):
    return startPoint + (endPoint - startPoint) * timeValue


def setGradientMode(gradPalette):
    refList = sorted(visRects, key = lambda x: x.getHeight())
    refDict = {subRect: coreColour for subRect, coreColour in list(zip(refList, gradPalette))}

    for subRect in visRects:
        subRect.setColour(refDict[subRect])


def resetColour():
    for i in range(len(visRects)):
        visRects[i].setColour(WHITE)


def shuffleRects(endInd = len(visRects)):
    global visRects
    visRects = visHandler.getCollection()
    auxRects = visRects[:endInd]
    random.shuffle(auxRects)

    for i in range(len(auxRects)):
        auxRects[i].setColour(auxRects[i].getColour())
        modifyVisually(visRects[i], auxRects[i], i, False)

    visHandler.setCollection(auxRects + visRects[endInd:])


def displayRects():
    global visRects
    visRects = visHandler.getCollection()
    for i in range(len(visRects)):
        visRects[i].drawRect(i)


def eraseRects():
    erasePortion = [0, 90, visWindow.get_width(), 630]
    visWindow.fill(BLACK, erasePortion)


def displayWidgets(widgetList):
    for subWidget in widgetList:
        subWidget.displayWidget()


def eraseWidgets(fullErase = True):
    if fullErase:
        erasePortion = [0, 0, 1280, 90]

    else:
        # Only erase buttons
        erasePortion = [537.5, 50, 205, 40]

    visWindow.fill(BLACK, erasePortion)


def eraseDetails():
    erasePortion = [0, 0, 200, 130]
    visWindow.fill(BLACK, erasePortion)


def buttonColourEffect(buttonList):
    for subButton in buttonList:
        checkHalt()
        if subButton.onHoverColourChange():
            return subButton


def buttonFontEffect(buttonList):
    for subButton in buttonList:
        checkHalt()
        if subButton.onHoverFontChange():
            return subButton


def checkSound(pressedButton):
    if visSound:
        pressedButton.playSFX()

    else:
        # Incur delay for stability
        pygame.time.delay(100)


def setHandler(buttonList, buttonHandler):
    for subButton in buttonList:
        if isinstance(subButton, Button):
            subButton.setHandler(buttonHandler)


def checkHalt():
    for keyEvent in pygame.event.get():
        if keyEvent.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    visLoop()
