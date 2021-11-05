from tkinter import *
import tkinter as tk

def makeWindow(screenName, dimensionX, dimensionY, bgColor):
    global root
    root = tk.Tk()
    root.title(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))

#Sub-window for settings
def userSettings():
    #Sub-window setup
    global settings
    settings = tk.Tk()
    settings.title("Settings")

    #Components within settings window
    global xSlide
    xSlide = Scale(root, from_=0, to=42, command=applyChanges)
    xSlide.pack()
    global ySlide
    ySlide = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=applyChanges)
    ySlide.pack()

#Button command to apply changes
def applyChanges(x, y, bgColor="red"):
    root.geometry("%dx%d+0+0" % (x.get(), y.get()))
    root.configure(background=bgColor)
    print(x)
    print(y)

def main():
    makeWindow("Web Finder Beta", 1000, 600, "white")
    userSettings()

if __name__ == "__main__":
    main()

root.mainloop()
