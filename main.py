from tkinter import *
import tkinter as tk
import numpy as np

def makeWindow(screenName, dimensionX, dimensionY, bgColor):
    global root
    root = tk.Tk()
    root.title(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))

def userSettings():
    global xSlide
    xSlide = Scale(root, from_=0, to=42)
    xSlide.pack()
    global ySlide
    ySlide = Scale(root, from_=0, to=200, orient=HORIZONTAL)
    ySlide.pack()

def applyChanges(x, y, bgColor="red"):
    root.geometry("%dx%d+0+0" % (x.get(), y.get()))
    root.configure(background=bgColor)

def makeButtons():
    editLayout = Button(root, text="Settings", command=lambda:applyChanges(xSlide, ySlide))

def main():
    makeWindow("Web Finder Beta", 1500, 800, "white")
    userSettings()

if __name__ == "__main__":
    main()

root.mainloop()
