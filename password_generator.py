from tkinter import *
import secrets
import string

# Basic settings for the root
root = Tk()
root.config(bg="#637180")
root.title("Password Generator")
root.geometry("700x500")
root.resizable(0, 0)

# Function to copy the password to the clipboard
def copyToClipboard():
    global password
    root.clipboard_clear()
    root.clipboard_append('i can has clipboardz?')

# Configuring the grid
root.grid_columnconfigure(0, weight=1)

# A title widget at the top of the window
passGenTitle = Label(root, bg="#637180", text="Password Generator", font="Helvetica 40 bold underline").grid(row=0, rowspan=2, column=0, padx=25, pady=25)

password = StringVar()
password.set("3n(fn$laW15!.")
# The label used to display the generated password
passGen = Entry(root, textvariable=password, font=", 20", bg="#637180", justify="center").grid(row=2, rowspan=3, column=0, padx=75, pady=50)

# Checkboxes to determine whether the user wants numbers, uppercase letters, or symbols, respectively
numberCheckbox = Checkbutton(root, bg="#637180", text="Numbers?").grid(row=5, column=0, padx=10, pady=10)
uppercaseLetterCheckbox = Checkbutton(root, bg="#637180", text="Uppercase Letters?").grid(row=6, column=0, padx=10, pady=10)
symbolsCheckbox = Checkbutton(root, bg="#637180", text="Symbols?").grid(row=7, column=0, padx=10, pady=10) 

# Button to submit the settings and generate a password
submitButton = Button(root, bg="#637180", text="    Submit    ").grid(row=8, column=0, padx=50, pady=50)

root.mainloop()

