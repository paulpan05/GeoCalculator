import ctypes
from tkinter import *
from tkinter import messagebox
from tkinter import font
from GoogleMapsAPI import *
from tkinter import simpledialog
from PIL import Image, ImageTk

# Dimensions

user32 = ctypes.windll.user32
sysHeight = user32.GetSystemMetrics(1)
sysHeight = sysHeight/2.0
sysWidth = sysHeight * (16.0/9.0)
newWidth = sysWidth * (775.0/768.0)

# tkinter Construction

root = Tk()
root.resizable(height=False, width=False)
root.iconbitmap(r'1494497497_globe-01.ico')

# Definitions

def quit():
    root.destroy()

def getFinalAddress():
    locCord = simpledialog.askstring("Prompt", "Enter Any Location")
    gMaps = GoogleMapsAPI(locCord)
    messagebox.showinfo("Results", "Full Address:   " + gMaps.getFormatedAddress())

def getFinalCoordiate():
    locCord = simpledialog.askstring("Prompt", "Enter Any Location")
    gMaps = GoogleMapsAPI(locCord)
    messagebox.showinfo("Results", gMaps.getFormatedCoordinate())

def getFinalElevation():
    locCord = simpledialog.askstring("Prompt", "Enter Any Location")
    gMaps = GoogleMapsAPI(locCord)
    messagebox.showinfo("Results", gMaps.getFormatedElevation())

def getFinalTime():
    locCord = simpledialog.askstring("Prompt", "Enter Any Location")
    gMaps = GoogleMapsAPI(locCord)
    messagebox.showinfo("Results", gMaps.getFormatedTime())

def getFinalPhysicalTimeDifference():
    locCord1 = simpledialog.askstring("Prompt", "Enter Location 1")
    locCord2 = simpledialog.askstring("Prompt", "Enter Location 2")
    messagebox.showinfo("Results", getFormatedPhysicalTimeDifference(locCord1, locCord2))

def getFinalDistance():
    locCord1 = simpledialog.askstring("Prompt", "Enter Location 1")
    locCord2 = simpledialog.askstring("Prompt", "Enter Location 2")
    messagebox.showinfo("Results", getFormatedDistance(locCord1, locCord2))

def getFinalFlightTime():
    locCord1 = simpledialog.askstring("Prompt", "Departure")
    locCord2 = simpledialog.askstring("Prompt", "Destination")
    messagebox.showinfo("Results", getFormatedFlightTime(locCord1, locCord2))

def getFinalTimeDifference():
    locCord1 = simpledialog.askstring("Prompt", "Enter Location 1")
    locCord2 = simpledialog.askstring("Prompt", "Enter Location 2")
    messagebox.showinfo("Results", getFormatedTimeDifference(locCord1, locCord2))

def aboutinfo():
    newWindow = Toplevel()
    newWindow.iconbitmap(r'1494497497_globe-01.ico')
    newWindow.resizable(height=False, width=False)
    newWindow.configure(background = "light grey")
    newLabel = Label(newWindow, text="GeoCalculator: A Useful Travel Companion\n\n"
                                     "This app is intended for providing users\n"
                                     "with accurate geographic data of one or\n"
                                     "more locations. Credit goes to Google Maps\n"
                                     "for giving this app the necessary APIs\n"
                                     "used for obtaining the raw data.\n\n"
                                     "© Copyright 2017 Junhong Pan (Paul Pan). "
                                     "All Rights Reserved.", bg="light grey", fg="black", font=("Segoe",int(3*(sysWidth/768.0))), justify=LEFT, padx = 10, pady = 10)
    newLabel.pack(fill=X, expand=YES, side=TOP)
    imageOrig1 = Image.open('earth-png-25606.png')
    newImg1 = imageOrig1.resize((int(newWidth/2.5), int(newWidth/3.89375)), Image.ANTIALIAS)
    filename1 = ImageTk.PhotoImage(newImg1)
    panel = Label(newWindow, image = filename1, bg="light grey")
    panel.pack(side=LEFT)
    def exit():
        newWindow.destroy()
    butOn = Button(newWindow, text="Exit", command=exit, font=("Verdana", 11))
    butOn.pack(anchor=SE, side = BOTTOM)
    newWindow.configure(padx=10, pady = 10)
    newWindow.mainloop()

# Background

C = Canvas(root, bg = "blue", height = int(sysHeight), width = int(sysWidth))
imageOrig = Image.open('Geography.png')
newImg = imageOrig.resize((int(newWidth), int(newWidth*(12.0/16.0))), Image.ANTIALIAS)
filename = ImageTk.PhotoImage(newImg)
C.pack(side = TOP, fill = BOTH, expand = YES)
C.create_image(0, 0, image=filename, anchor=NW)


# Copyright Label

status = Label(root, text = "© Copyright 2017 Junhong Pan (Paul Pan). "
                            "All Rights Reserved.", bd = 4*(sysHeight/432.0), relief = SUNKEN, anchor=E)
status.pack(fill = X, expand = YES, side = BOTTOM)

# Title

root.title("GeoCalculator")
titleLabel = Label(root, text = "GeoCalculator", bg = "light grey", fg="green", font=("Courier New", 24, font.BOLD))
titleWindow = C.create_window(sysWidth*0.5, 0, anchor = N, window = titleLabel, width = newWidth)
title2Label = Label(root, text = "A Useful Travel Companion", bg = "light grey", fg="green", font=("Courier New", 12))
title2Window = C.create_window(sysWidth*0.5, sysHeight*(32.0/432.0), anchor = N, window = title2Label, width = newWidth)

# Menu

menu = Menu(root)
root.config(menu = menu)
subMenu = Menu(menu, tearoff=False)
menu.add_cascade(label = "Functions", menu = subMenu)
subMenu.add_command(label = "Get Full Address", command = getFinalAddress)
subMenu.add_command(label = "Get Coordinate", command = getFinalCoordiate)
subMenu.add_command(label = "Get Elevation", command = getFinalElevation)
subMenu.add_command(label = "Get Date and Time", command = getFinalTime)
subMenu.add_command(label = "Calculate Physical Time Difference", command = getFinalPhysicalTimeDifference)
subMenu.add_command(label = "Calculate Distance", command = getFinalDistance)
subMenu.add_command(label = "Calculate Flight Time", command = getFinalFlightTime)
subMenu.add_command(label = "Calculate Time Difference", command = getFinalTimeDifference)
menu.add_command(label = "About", command = aboutinfo)
menu.add_command(label = "Exit", command = quit)

# Buttons

b1 = Button(root, text = "Exit", command = quit, font=("Verdana", 11))
exitButton = C.create_window(sysWidth*0.85, sysHeight*0.81, anchor = N, window = b1)
b2 = Button(root, text = "Get Full Address", command = getFinalAddress, font=("Verdana", 11))
addressButton = C.create_window(sysWidth*0.15, sysHeight*0.23, anchor = N, window = b2)
b3 = Button(root, text = "Get Coordinate", command = getFinalCoordiate, font=("Verdana", 11))
coordinateButton = C.create_window(sysWidth*0.15, sysHeight*0.52, anchor = N, window = b3)
b4 = Button(root, text = "Get Elevation", command = getFinalElevation, font=("Verdana", 11))
elevationButton = C.create_window(sysWidth*0.15, sysHeight*0.81, anchor = N, window = b4)
b5 = Button(root, text = "Get Date and Time", command = getFinalTime, font=("Verdana", 11))
timeButton = C.create_window(sysWidth*0.5, sysHeight*0.23, anchor = N, window = b5)
b6 = Button(root, text = "Calculate Physical\nTime Difference", command = getFinalPhysicalTimeDifference, font=("Verdana", 11))
physicalButton = C.create_window(sysWidth*0.5, sysHeight*0.52, anchor = N, window = b6)
b7 = Button(root, text = "Calculate Distance", command = getFinalDistance, font=("Verdana", 11))
distanceButton = C.create_window(sysWidth*0.5, sysHeight*0.81, anchor = N, window = b7)
b8 = Button(root, text = "Calculate Flight\nTime", command = getFinalFlightTime, font=("Verdana", 11))
flightButton = C.create_window(sysWidth*0.85, sysHeight*0.23, anchor = N, window = b8)
b9 = Button(root, text = "Calculate Time\nDifference", command = getFinalTimeDifference, font=("Verdana", 11))
differenceButton = C.create_window(sysWidth*0.85, sysHeight*0.52, anchor = N, window = b9)

# Scaling

root.tk.call('tk', 'scaling', 4.0)

# Loop

root.mainloop()
