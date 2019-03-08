#!/usr/bin/env python3

# Creating Graphical User Interfaces - "tkinter" program


# Task 1
# 1. Write a GUI application with a button labeled “Goodbye.” When the button
#is clicked, the window closes.

import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

button = tkinter.Button(frame, text='Goodbye', command=lambda:
window.destroy())
button.pack()
window.mainloop()

# Task 2

# Write a GUI application with a single button. Initially the button is labeled 0, 
# but each time it is clicked, the value on the button increases by 1.

import tkinter
def increment(text):
    """ Increment number represented by the contents of text by 1 and updatetext with the result.""" 
    count = int(text.get())
    text.set(str(count + 1))
    
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

text = tkinter.StringVar()
text.set('0')

button = tkinter.Button(frame, textvariable=text,command=lambda: increment(text))
button.pack()

window.mainloop()

# What is a more readable way to write the following?
# x = lambda: y

# I think this
# def x():
#     return y

# A DNA sequence is a string made up of As, Ts, Cs, and Gs. Write a GUI application 
# in which a DNA sequence is entered, and when the Count button is clicked, the number 
# of As, Ts, Cs, and Gs are counted and dis- played in the window (see the following image).

# Task 4

import tkinter
def count(text, out_data):
    """ Update out_data with the total number of As, Ts, Cs, and Gs found in 
    text.""" 
    data = text.get('0.0', tkinter.END)
    counts = {}
    for char in 'ATCG':
        counts[char] = data.count(char)
    out_data.set('Num As: {0} Num Ts: {1} Num Cs: {2} Num Gs: {3}'.format(
        counts['A'], counts['T'], counts['C'], counts['G']))

window = tkinter.Tk()
text = tkinter.Text(window, height=10, width=40)
text.pack()

out_data = tkinter.StringVar()

button = tkinter.Button(window, text='Count', command=lambda: count(text,
out_data))
button.pack()

label = tkinter.Label(window, textvar=out_data)
label.pack()
window.mainloop()

# In Defining Our Own Functions, on page 35, we wrote a function to 
# convert degrees Fahrenheit to degrees Celsius. Write a 
# GUI application that looks like the following image.

import tkinter
def convert(out_data, temp_data):
    """ Convert the value in temp_data, assumed to be in degrees Celsius,
        to Fahrenheit and store the result in out_data. """ 
    f = temp_data.get()
    out_data.set((f -32) * 5 / 9)
    
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
out_data = tkinter.StringVar()
temp_data = tkinter.DoubleVar()
tkinter.Label(frame, text='Temperature in Fahrenheit:').pack()

text = tkinter.Entry(frame, textvar=temp_data)
text.pack()
label = tkinter.Label(frame, textvar=out_data)
label.pack()

button = tkinter.Button(frame, text='Convert', command=lambda: 
convert(out_data, temp_data))
button.pack()

button2 = tkinter.Button(frame, text='Quit', command=lambda: 
window.destroy())

button2.pack()
window.mainloop()


# Rewrite the text editor code from Using Menu, 
# on page 337, as an object- oriented GUI.

import tkinter
import tkinter.filedialog as dialog
class TextEditor:
    """A simple text editor.""" 
    def __init__(self, parent):
        """Create the GUI.""" 
        # Framework
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        
        # Text box for editing.
        self.text = tkinter.Text(parent)
        self.text.pack()
        # Menus.
        menubar = tkinter.Menu(parent)
        filemenu = tkinter.Menu(menubar)
        
        filemenu.add_command(label='Save', command=self.save_click)
        filemenu.add_command(label='Quit', command=self.quit_click)
        
        menubar.add_cascade(label='File', menu=filemenu)
        window.config(menu=menubar)
    def save_click(self):
        """Handle click on 'Save' menu.""" 
        data = self.text.get('0.0', tkinter.END)
        filename = dialog.asksaveasfilename(
            parent=self.parent,
            filetypes=[('Text', '*.txt')],
            title='Save as...')
        writer = open(filename, 'w')
        writer.write(data)
        writer.close()
    def quit_click(self):
        """Handle click on 'Quit' menu.""" 
        self.parent.destroy()
        
if __name__ == '__main__':
    window = tkinter.Tk()
    app = TextEditor(window)
    window.mainloop()
