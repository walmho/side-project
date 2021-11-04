def makeWindow(screenName, dimensionX, dimensionY, bgColor):
    root = tk.Tk()
    root.title(screenName)
    root.configure(background=bgColor)
    root.geometry("%dx%d+0+0" % (dimensionX, dimensionY))
    root.mainloop()

def main():
    makeWindow("Web Finder Beta", 1500, 800, "white")

if __name__ == "__main__":
    import tkinter as tk
    main()

