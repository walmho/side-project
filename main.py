from tkinter import *
import tkinter as tk

def mainWindow(screenName, dimensionX, dimensionY, bgColor):
    global root
    root = tk.Tk()
    root.title(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))

    settings = Button(root, text="Settings", command=lambda:userSettings())
    settings.pack()

#Sub-window for settings
def userSettings():
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
    color = "grey"

    #Buttons
    finishChanges = Button(settings, text="Apply", command=lambda:applyChanges(xSlide.get(), ySlide.get(), color))
    finishChanges.pack()

#Button command to apply changes
def applyChanges(x, y, bgColor):
    root.geometry("%dx%d+0+0" % (x, y))
    root.configure(background=bgColor)
    print(x)
    print(y)

def main():
    mainWindow("Web Finder Beta", 1000, 600, "white")

if __name__ == "__main__":
    main()

root.mainloop()
