from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
red = LED(18)
green = LED(23)
blue = LED(24)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTIONS ###
def redToggle():
    if red.is_lit:
        red.off() 
        redButton["text"] = "Turn red LED on"
    else:
        red.on()
        redButton["text"] = "Turn red LED off"

def greenToggle():
    if green.is_lit:
        green.off() 
        greenButton["text"] = "Turn green LED on"
    else:
        green.on()
        greenButton["text"] = "Turn green LED off"

def blueToggle():
    if blue.is_lit:
        blue.off() 
        blueButton["text"] = "Turn blue LED on"
    else:
        blue.on()
        blueButton["text"] = "Turn blue LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
redButton = Button(win, text = 'Turn red LED on', font = myFont, command = redToggle, bg = 'red', height = 1, width = 14)
greenButton = Button(win, text = 'Turn green LED on', font = myFont, command = greenToggle, bg = 'green', height = 1, width = 14)
blueButton = Button(win, text = 'Turn blue LED on', font = myFont, command = blueToggle, bg = 'blue', height = 1, width = 14) 
redButton.grid(row = 0, column = 1)
greenButton.grid(row = 1, column = 1)
blueButton.grid(row = 2, column = 1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'bisque2', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)

win.protocol("WM DELETE WINDOW", close) # Exit cleanly 
win.mainloop() # Loop indefinitely