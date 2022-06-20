from tkinter import *
import secrets
import string
import tkinter

# Basic settings for the tkinter root window
root = Tk()
root.config(bg="#637180")
root.title("Password Generator")
root.geometry("700x500")
root.resizable(0, 0)

# Password variable is first calculated then displayed in the tkinter window
password = StringVar()

# Defining the variables needed to determine if the checkbox state and the slider variable
numberCheck = IntVar()
uppercaseCheck = IntVar()
symbolsCheck = IntVar()
passLength = IntVar()

# Function to copy the password to the clipboard
def clipboardPrompt():
    passClipboardEmpty.lower()
    passClipboardButton.grid(row=5, column=0)
    passClipboardButton.tkraise()


def copyToClipboard():
    global password
    root.clipboard_clear()
    root.clipboard_append(password.get())
    passClipboardButton.grid_forget()

    passClipboardMessage = Label(root, bg="#637180", text="Copied!", justify="center", font="Helvetica 10 bold")
    passClipboardMessage.grid(row=5, column=0, pady=3)
    


def passwordSubmit():
    # Password used to set display to password, check variables used to determine if respective box is checked
    global password 
    global numberCheck
    global uppercaseCheck
    global symbolsCheck
    global passLength
    numberCheckBoolean = None
    uppercaseCheckBoolean = None
    symbolsCheckBoolean = None

    # The allowed character list is added to depending on which boxes are checked
    allowedCharacters = string.ascii_lowercase
    if numberCheck.get() == 1:
        allowedCharacters += string.digits
        numberCheckBoolean = True
    if uppercaseCheck.get() == 1:
        allowedCharacters += string.ascii_uppercase
        uppercaseCheckBoolean = True
    if symbolsCheck.get() == 1:
        allowedCharacters += string.punctuation
        symbolsCheckBoolean = True

    # The loop that checks that the generated password has all the requested characters. It will also open a prompt for copying the generated password.
    while True:
        generatedPassword = ''.join(secrets.choice(allowedCharacters) for i in range(passLength.get()))
        passwordLower = any(c.islower() for c in generatedPassword)
        passwordUpper = any(c.isupper() for c in generatedPassword)
        passwordDigit = (sum(c.isdigit() for c in generatedPassword) >= (passLength.get() // 4))
        passwordSymbol = (any(c.isalnum() for c in generatedPassword) <= 15)
        if any((numberCheckBoolean, uppercaseCheckBoolean, symbolsCheckBoolean)):
            if all((numberCheckBoolean, uppercaseCheckBoolean, symbolsCheckBoolean)):
                if all((passwordLower, passwordUpper, passwordDigit, passwordSymbol)):
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
            elif all((numberCheckBoolean, uppercaseCheckBoolean)):
                if all((passwordLower, passwordDigit, passwordUpper)):
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
            elif all((uppercaseCheckBoolean, symbolsCheckBoolean)):
                if all((passwordLower, passwordUpper, passwordSymbol)):
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
            elif all((numberCheckBoolean, symbolsCheckBoolean)):
                if all((passwordLower, passwordDigit, passwordSymbol)):
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
            elif numberCheckBoolean:
                if passwordDigit:
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
            elif uppercaseCheckBoolean:
                if passwordUpper:
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
            elif symbolsCheckBoolean:  
                if passwordLower:
                    password.set(generatedPassword)
                    clipboardPrompt()
                    break
        elif passwordLower:
            password.set(generatedPassword)
            clipboardPrompt()
            break        


# A title widget at the top of the window
passGenTitle = Label(root, bg="#637180", text="Password Generator", font="Helvetica 40 bold underline").grid(row=0, rowspan=2, column=0, padx=25, pady=25)

# The label used to display the generated password and a message that says when the password is copied to clipboard
passGen = Entry(root, textvariable=password, font=", 40", bg="#637180", justify="center").grid(row=2, rowspan=3, column=0, padx=75, pady=20)

passClipboardButton = Button(root, bg="#637180", text="Copy to clipboard?" , justify="center", font="Helvetica 10 bold", command=copyToClipboard)
passClipboardButton.grid(row=5, column=0)
passClipboardButton.grid_forget()

passClipboardEmpty = Label(root, bg="#637180", text="                      ", justify="center", font="Helvetica 10 bold")
passClipboardEmpty.grid(row=5, column=0, pady=3)

# Slider used to determine the number of wanted characters
lengthSlider = Scale(root, bg="#637180", orient="horizontal", from_=4, to=20, variable=passLength, length=200, bd=6, highlightbackground="#637180").grid(row=6, column=0, padx=10)
lengthDesc = Label(root, background="#637180", text="Length").place(x=475, y=280)

# Checkboxes to determine whether the user wants numbers, uppercase letters, or symbols, respectively
numberCheckbox = Checkbutton(root, bg="#637180", text="Numbers?", onvalue=1, offvalue=0, variable=numberCheck).grid(row=7, column=0, padx=10, pady=10)
uppercaseLetterCheckbox = Checkbutton(root, bg="#637180", text="Uppercase Letters?", onvalue=1, offvalue=0, variable=uppercaseCheck).grid(row=8, column=0, padx=10, pady=10)
symbolsCheckbox = Checkbutton(root, bg="#637180", text="Symbols?", onvalue=1, offvalue=0, variable=symbolsCheck).grid(row=9, column=0, padx=10, pady=10) 

# Button to submit the settings and generate a password
submitButton = Button(root, bg="#637180", text="      Submit      ", command=passwordSubmit).grid(row=10, column=0, padx=50, pady=15)

root.mainloop()