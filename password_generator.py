from tkinter import *
import secrets
import string

# Basic settings for the tkinter root window
root = Tk()
root.config(bg="#637180")
root.title("Password Generator")
root.geometry("700x500")
root.resizable(0, 0)

# Password variable is first calculated then displayed in the tkinter window
password = StringVar()

# Defining the variables needed to determine if the checkboxes are on or off
numberCheck = IntVar()
uppercaseCheck = IntVar()
symbolsCheck = IntVar()

# Function to copy the password to the clipboard
# def copyToClipboard():
    #global password
    #root.clipboard_clear()
    #root.clipboard_append('i can has clipboardz?')


def passwordSubmit():
    # Password used to set display to password, check variables used to determine if respective box is checked
    global password 
    global numberCheck
    global uppercaseCheck
    global symbolsCheck
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

    # 
    while True:
        generatedPassword = ''.join(secrets.choice(allowedCharacters) for i in range(15))
        passwordLower = any(c.islower() for c in generatedPassword)
        passwordUpper = any(c.isupper() for c in generatedPassword)
        passwordDigit = (sum(c.isdigit() for c in generatedPassword) >= 3)
        passwordSymbol = any(c.isalnum() for c in generatedPassword)
        if any((numberCheckBoolean, uppercaseCheckBoolean, not symbolsCheckBoolean)):
            if all((numberCheckBoolean, uppercaseCheckBoolean, not symbolsCheckBoolean)):
                if all((passwordLower, passwordUpper, passwordDigit, passwordSymbol)):
                    password.set(generatedPassword)
                    break
            elif all((numberCheckBoolean, uppercaseCheckBoolean)):
                if all((passwordLower, passwordDigit, passwordUpper)):
                    password.set(generatedPassword)
                    break
            elif all((uppercaseCheckBoolean, not symbolsCheckBoolean)):
                if all((passwordLower, passwordUpper, passwordSymbol)):
                    password.set(generatedPassword)
                    break
            elif all((numberCheckBoolean, not symbolsCheckBoolean)):
                if all((passwordLower, passwordDigit, passwordSymbol)):
                    password.set(generatedPassword)
                    break
            elif numberCheckBoolean:
                if passwordDigit:
                    password.set(generatedPassword)
                    break
            elif uppercaseCheckBoolean:
                if passwordUpper:
                    password.set(generatedPassword)
                    break
            elif symbolsCheckBoolean:  
                if passwordLower:
                    password.set(generatedPassword)
                    break
        elif passwordLower:
            password.set(generatedPassword)
            break        


# A title widget at the top of the window
passGenTitle = Label(root, bg="#637180", text="Password Generator", font="Helvetica 40 bold underline").grid(row=0, rowspan=2, column=0, padx=25, pady=25)


# The label used to display the generated password
passGen = Entry(root, textvariable=password, font=", 40", bg="#637180", justify="center").grid(row=2, rowspan=3, column=0, padx=75, pady=40)

# Checkboxes to determine whether the user wants numbers, uppercase letters, or symbols, respectively
numberCheckbox = Checkbutton(root, bg="#637180", text="Numbers?", onvalue=1, offvalue=0, variable=numberCheck).grid(row=5, column=0, padx=10, pady=10)
uppercaseLetterCheckbox = Checkbutton(root, bg="#637180", text="Uppercase Letters?", onvalue=1, offvalue=0, variable=uppercaseCheck).grid(row=6, column=0, padx=10, pady=10)
symbolsCheckbox = Checkbutton(root, bg="#637180", text="Symbols?", onvalue=1, offvalue=0, variable=symbolsCheck).grid(row=7, column=0, padx=10, pady=10) 

# Button to submit the settings and generate a password
submitButton = Button(root, bg="#637180", text="      Submit      ", command=passwordSubmit).grid(row=8, column=0, padx=50, pady=40)

root.mainloop()

