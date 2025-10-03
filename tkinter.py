from tkinter import *
parent =Tk()
parent.title("Color Buttons")
red_button = Button(parent, text="Red", fg="red")
red_button.pack(side=LEFT)
black_button = Button(parent, text="Black", fg="black")
black_button.pack(side=RIGHT)
blue_button = Button(parent, text="Blue", fg="blue")
blue_button.pack(side=TOP)
green_button = Button(parent, text="Green", fg="green")
green_button.pack(side=BOTTOM)
parent.mainloop()

from tkinter import *

# Create the main window
top = Tk()
top.geometry("400x250")
top.title("User Form")

# Labels
Label(top, text="Name").place(x=30, y=50)
Label(top, text="Email").place(x=30, y=90)
Label(top, text="Password").place(x=30, y=130)

# Entry fields
Entry(top).place(x=100, y=50)
Entry(top).place(x=100, y=90)
Entry(top, show="*").place(x=100, y=130)  # Password field masked

# Run the application
top.mainloop()