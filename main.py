def makeWindow(screenName, dimensionX, dimensionY, bgColor):
    root = tk.Tk(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))
    root.mainloop()

def main():
    makeWindow("Test", 50, 50, "white")

if __name__ == "__main__":
    import tkinter as tk
    main()

