import tkinter as tk
import string
import random
import pyperclip

#window config
root = tk.Tk()
root.geometry("600x500")
root.title("Password generator")
#root.config(bg="")

characters = ""

#checkbox status
hasLowercase = True
hasUppercase = False 
hasNumbers = False
hasSymbols = False

def addLowercase():
   global hasLowercase
   hasLowercase = not hasLowercase

def addUppercase():
   global hasUppercase
   hasUppercase = not hasUppercase

def addNumbers():
   global hasNumbers
   hasNumbers = not hasNumbers

def addSymbols():
   global hasSymbols
   hasSymbols = not hasSymbols

def generatePass():
   global characters
   characters = ""

   if hasLowercase:
      characters += string.ascii_lowercase

   if hasUppercase:
      characters += string.ascii_uppercase

   if hasNumbers:
      characters += string.digits

   if hasSymbols:
      characters += string.punctuation

   if characters == "":
      yourPassField.delete(0, tk.END)
      yourPassField.insert(0, "No characters!")
   else:
      password = ""
      passLength = passLengthSlider.get()
      randomNum = 0
      for i in range(0, passLength):
         randomNum = random.randint(0, len(characters) - 1)
         password += characters[randomNum]
      
      yourPassField.delete(0, tk.END)
      yourPassField.insert(0, password)

def copy():
   password = yourPassField.get()
   pyperclip.copy(password)


appNameLabel = tk.Label(root, text="Password Generator", font=('Arial', 18)).pack(pady=20)
yourPassLabel = tk.Label(root, text="Your password:", font=('Arial', 13)).pack(padx=20)

yourPassField = tk.Entry(root, width = 70, font=('Arial', 13))
yourPassField.pack(padx=20)

buttonFrame = tk.Frame(root)
generateButton = tk.Button(buttonFrame, text="Generate password",  font=('Arial', 13), command=generatePass).grid(row=0, column=0)
copyButton = tk.Button(buttonFrame, text="Copy", font=('Arial', 13), command=copy).grid(row=0, column=1)
buttonFrame.pack()

checkboxFrame = tk.Frame(root)
lowercaseCheckbox = tk.Checkbutton(checkboxFrame, text="Lowercase (a-z)", font=('Arial', 13), command=addLowercase)
lowercaseCheckbox.grid(row=1, column=0)
lowercaseCheckbox.select()
uppercaseCheckbox = tk.Checkbutton(checkboxFrame, text="Uppercase (A-Z)", font=('Arial', 13), command=addUppercase).grid(row=1, column=1)
numbersCheckbox = tk.Checkbutton(checkboxFrame, text="Numbers (0-9)", font=('Arial', 13), command=addNumbers).grid(row=2, column=0)
symbolsCheckbox = tk.Checkbutton(checkboxFrame, text="Symbols (e.g. %$#&)", font=('Arial', 13), command=addSymbols).grid(row=2, column=1)
checkboxFrame.pack()

passLengthLabel = tk.Label(root, text="Password length", font=('Arial', 13)).pack(padx=20)
passLengthSlider = tk.Scale(root, from_=5, to=30, orient="horizontal", font=('Arial', 13), length=300)
passLengthSlider.set(17)
passLengthSlider.pack()

root.mainloop()