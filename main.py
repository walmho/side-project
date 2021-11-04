from tkinter.constants import HORIZONTAL


def makeWindow(screenName, dimensionX, dimensionY, bgColor):
    global root
    root = tk.Tk()
    root.title(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))

def userSettings():
    xSlide = Scale(root, from_=0, to=42)
    xSlide.pack()
    ySlide = Scale(root, from_=0, to=200, orient=HORIZONTAL)
    ySlide.pack()

def main():
    makeWindow("Web Finder Beta", 1500, 800, "white")
    userSettings()

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import Scale
    main()

root.mainloop()
