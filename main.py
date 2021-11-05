from tkinter import *
import tkinter as tk

def mainWindow(screenName, dimensionX, dimensionY, bgColor, colorCounter):
    global root
    root = tk.Tk()
    root.title(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))

    settings = Button(root, text="Settings", command=lambda:userSettings(colorCounter))
    settings.pack()

def colorCycle(colorCounter):
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "pale violet red", "light salmon", "gold", "spring green", "light sky blue"]
    if colorCounter >= len(colors):
        colorCounter = 0
    else:
        colorCounter += 1
    print(colorCounter)
    global chosenColor
    chosenColor = colors[colorCounter]
    print(chosenColor)

#Sub-window for settings
def userSettings(colorCounter):
    #Sub-window setup
    global settings
    settings = tk.Tk()
    settings.title("Settings")

    #Components within settings window
    #Sliders to adjust window size - you can do this manually, but again. Learning experience
    x = DoubleVar()
    global xSlide
    xSlide = Scale(settings, from_=0, to=1000, orient=HORIZONTAL, variable=x)
    xSlide.pack()

    y = DoubleVar()
    global ySlide
    ySlide = Scale(settings, from_=0, to=500, orient=VERTICAL, variable=y)
    ySlide.pack()

    #Temp color var for testing - eventually make a button that toggles
    changeColor = Button(settings, text="Toggle Colors", command=lambda:colorCycle(colorCounter))
    changeColor.pack()

    #Buttons
    #Error handling for if the user hasn't changed the color
    try:
        finishChanges = Button(settings, text="Apply", command=lambda:applyChanges(xSlide.get(), ySlide.get(), chosenColor))
        finishChanges.pack()
    except NameError:
        finishChanges = Button(settings, text="Apply", command=lambda:applyChanges(xSlide.get(), ySlide.get(), chosenColor="white"))
        finishChanges.pack()

#Button command to apply changes
def applyChanges(x, y, bgColor):
    root.geometry("%dx%d+0+0" % (x, y))
    root.configure(background=bgColor)

def main():
    colorCounter = -1
    mainWindow("Web Finder Beta", 1000, 600, "white", colorCounter)

if __name__ == "__main__":
    main()

root.mainloop()
