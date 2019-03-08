#!/usr/bin/env python3

# Creating Graphical User Interfaces - "tkinter" program

# Tk is a class that represents the root window of a tkinter GUI. 
# This root window’s mainloop method handles all the events for the GUI, 
# so it’s important to create only one instance of Tk.

import tkinter
window = tkinter.Tk() 
window.mainloop()
print('Anybody home?')


# creating a Label that belongs to the root window—its parent widget—and we 
# specify the text to be displayed by assigning it to the Label’s text parameter.
import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text='This is our label.') 
label.pack()
window.mainloop()

import tkinter
window = tkinter.Tk()
label = tkinter.Label(window, text='First label.') 
label.pack()
label.config(text='Second label.')
window.mainloop()

# Using Mutable Variables with Widgets
# Notice that this time we assign to the textvariable parameter of the label rather than the text parameter.
# because of the way module tkinter is structured, you cannot create a 
# StringVar or any other mutable variable until you have created the root Tk window.

import tkinter
window = tkinter.Tk()
data = tkinter.StringVar()
data.set('Data to display') 
label = tkinter.Label(window, textvariable=data) 
label.pack()
window.mainloop()

# Grouping Widgets with the Frame Type
# Note that we call pack on every widget; if we omit one of these calls, that widget will not be displayed.

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
first = tkinter.Label(frame, text='First label') 
first.pack()
second = tkinter.Label(frame, text='Second label') 
second.pack()
third = tkinter.Label(frame, text='Third label') 
third.pack()
window.mainloop()

# example with the same three Labels but with two frames instead of one. The second frame has a visual border around it:

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
frame2 = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE) 
frame2.pack()
first = tkinter.Label(frame, text='First label')
first.pack()
second = tkinter.Label(frame2, text='Second label') 
second.pack()
third = tkinter.Label(frame2, text='Third label') 
third.pack()
window.mainloop()

# Getting Information from the User with the Entry Type
# Here’s an example that associates a single StringVar with both a Label and an Entry. 
# When the user enters text in the Entry, the StringVar’s contents will change. 
# This will cause the Label to be updated, and so the Label will display whatever is currently in the Entry.

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
var = tkinter.StringVar()
label = tkinter.Label(frame, textvariable=var)
label.pack()
entry = tkinter.Entry(frame, textvariable=var)
entry.pack()
window.mainloop()

