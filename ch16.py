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

# Models, Views, and Controllers
# Models (How do we represent the data?), Views (How do we display the data?), and Controllers (How do we modify the data?)


# Click button counter
import tkinter
# The controller.
def click():
    counter.set(counter.get() + 1)
if __name__ == '__main__': 
    window = tkinter.Tk()
    # The model.
    counter = tkinter.IntVar() 
    counter.set(0)
    # The views.
    frame = tkinter.Frame(window)
    frame.pack()
    button = tkinter.Button(frame, text='Click', command=click) 
    button.pack()
    label = tkinter.Label(frame, textvariable=counter)
    label.pack()
    # Start the machinery!
    
    window.mainloop()

    # Using Lambda
    # lower the counter’s value as well as raise it.

import tkinter
window = tkinter.Tk()
# The model.
counter = tkinter.IntVar()
counter.set(0)
# Two controllers.
def click_up(): 
    counter.set(counter.get() + 1)
def click_down(): 
    counter.set(counter.get() - 1)
    # The views.
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=click_up) 
button.pack()
button = tkinter.Button(frame, text='Down', command=click_down) 
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()
window.mainloop()

# The expression lambda: 3 on the first line creates a nameless function that always returns the number 3. 
# The second expression creates this function and immediately calls it, which has the same effect as this:
# The name lambda function comes from lambda calculus, a mathematical system for investigating function definition 
# and application that was developed in the 1930s by Alonzo Church and Stephen Kleene.

lambda: 3
print((lambda: 3)())
def f():
    return 3
print((lambda x: 2 * x)(3))

import tkinter
window = tkinter.Tk()
# The model.
counter = tkinter.IntVar()
counter.set(0)
# General controller.
def click(var, value): 
    var.set(var.get() + value)
# The views.
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=lambda: click(counter, 1)) 
button.pack()
button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1)) 
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()
window.mainloop()


# Customizing the Visual Style

# Changing Fonts

import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text='Hello',
                        font=('Courier', 14, 'bold italic'))
button.pack()
window.mainloop()   

# white text on a bright green background is not particularly readable.

import tkinter
window = tkinter.Tk()
button = tkinter.Label(window, text='Hello', bg='green', fg='white') 
button.pack()
window.mainloop()


# RGB

import tkinter
def change(widget, colors):
    """ Update the foreground color of a widget to show the RGB color value
    stored in a dictionary with keys 'red', 'green', and 'blue'.  Does
    *not* check the color value.
    """
    new_val = '#'
    for name in ('red', 'green', 'blue'):
        new_val += colors[name].get() 
    widget['bg'] = new_val
# Create the application.
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
# Set up text entry widgets for red, green, and blue, storing the # associated variables in a dictionary for later use.
colors = {}
for (name, col) in (('red', '#FF0000'),
                    ('green', '#00FF00'),
                    ('blue', '#0000FF')): 
    colors[name] = tkinter.StringVar()
    colors[name].set('00')
    entry = tkinter.Entry(frame, textvariable=colors[name], bg=col, fg='white')
    entry.pack()
                            
# Display the current color.
current = tkinter.Label(frame, text=' ', bg='#FFFFFF') 
current.pack()
# Give the user a way to trigger a color update.
update = tkinter.Button(frame, text='Update', command=lambda: change(current, colors))
update.pack()
tkinter.mainloop()

# providing a side argument to method pack:
# Setting side to "left" tells tkinter that the leftmost part of the label is to be placed 
# next to the left edge of the frame, and then the leftmost part of the entry field is 
# placed next to the right edge of the label—in short, that widgets are to be packed using their left edges.

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window) 
frame.pack()
label = tkinter.Label(frame, text='Name') 
label.pack(side='left')
entry = tkinter.Entry(frame) 
entry.pack(side='left')
window.mainloop()


#In the following code, we place the label in the upper left (row 0, column 0)
#and the entry field in the lower right (row 1, column 1).

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame, text='Name:') 
label.grid(row=0, column=0)
entry = tkinter.Entry(frame) 
entry.grid(row=1, column=1)
window.mainloop()


# Using Text
# The Entry widget that we have been using since the start of
#  this chapter allows for only a single line of text. If we want 
# multiple lines of text, we use the Text widget instead, as shown here:

import tkinter 
def cross(text):
    text.insert(tkinter.INSERT, 'X')
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
text = tkinter.Text(frame, height=3, width=10)
text.pack()
button = tkinter.Button(frame, text='Add', command=lambda: cross(text)) 
button.pack()
window.mainloop()

# Using Checkbuttons for RGB select

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
red = tkinter.IntVar()
green = tkinter.IntVar()
blue = tkinter.IntVar()

for (name, var) in (('R', red), ('G', green), ('B', blue)): 
    check = tkinter.Checkbutton(frame, text=name, variable=var) 
    check.pack(side='left')

def recolor(widget, r, g, b): 
    color = '#'
    for var in (r, g, b):
        color += 'FF' if var.get() else '00'
    widget.config(bg=color)
label = tkinter.Label(frame, text='[ ]') 
button = tkinter.Button(frame, text='update', command=lambda: recolor(label, red, green, blue))

button.pack(side='left') 
label.pack(side='left') 
window.mainloop()

# Using Menu
# The last widget we will look at is Menu. The following 
# code uses this to create a simple text editor:
# The program begins by defining two functions: save, which saves the contents of a text widget,
#  and quit, which closes the application. Function save uses tkFileDialog to create a standard “Save as...” 
# dialog box, which will prompt the user for the name of a text file.

import tkinter
import tkinter.filedialog as dialog

def save(root, text):
    data = text.get('0.0', tkinter.END) 
    filename = dialog.asksaveasfilename(
        parent=root, 
        filetypes=[('Text', '*.txt')], 
        title='Save as...')
    writer = open(filename, 'w') 
    writer.write(data) 
    writer.close()
def quit(root): 
    root.destroy()
window = tkinter.Tk()
text = tkinter.Text(window)
text.pack()

menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label='Save', command=lambda : save(window, text)) 
filemenu.add_command(label='Quit', command=lambda : quit(window))

menubar.add_cascade(label = 'File', menu=filemenu) 
window.config(menu=menubar)
window.mainloop()


# Object-Oriented GUIs

import tkinter
class Counter:
    """A simple counter GUI using object-oriented programming.""" 
    def __init__(self, parent):
        """Create the GUI."""
        # Framework.
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        # Model.
        self.state = tkinter.IntVar()
        self.state.set(1)
        # Label displaying current state.
        self.label = tkinter.Label(self.frame, textvariable=self.state)
        self.label.pack()
        # Buttons to control application.
        self.up = tkinter.Button(self.frame, text='up', command=self.up_click) 
        self.up.pack(side='left')
        self.right = tkinter.Button(self.frame, text='quit', command=self.quit_click) 
        self.right.pack(side='left')
    def up_click(self):
        """Handle click on 'up' button."""
        self.state.set(self.state.get() + 1)
    def quit_click(self):
        """Handle click on 'quit' button."""
        self.parent.destroy()

if __name__ == '__main__':
    window = tkinter.Tk()
    myapp = Counter(window)
    window.mainloop()

