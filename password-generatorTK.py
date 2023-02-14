import random
import string
import tkinter as tk

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits 
    if special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
      new_char = random.choice(characters)
      pwd += new_char
      
      if new_char in digits:
        has_number = True
      elif new_char in special:
        has_special = True
        
      meets_criteria = True 
      if numbers:
        meets_criteria = has_number
      if special_characters:
        meets_criteria = meets_criteria and has_special
      
    return pwd

def generate_and_display_password():
    min_length = int(min_length_entry.get())
    has_number = has_number_var.get()
    has_special = has_special_var.get()
    pwd = generate_password(min_length, has_number, has_special)
    password_display_label.configure(text="Generated Password: " + pwd)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create the UI elements
min_length_label = tk.Label(root, text="Minimum Length:")
min_length_entry = tk.Entry(root)
has_number_var = tk.BooleanVar()
has_number_checkbox = tk.Checkbutton(root, text="Include numbers", variable=has_number_var)
has_special_var = tk.BooleanVar()
has_special_checkbox = tk.Checkbutton(root, text="Include special characters", variable=has_special_var)
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
password_display_label = tk.Label(root, text="")

# Add the UI elements to the window
min_length_label.pack()
min_length_entry.pack()
has_number_checkbox.pack()
has_special_checkbox.pack()
generate_button.pack()
password_display_label.pack()

# Start the event loop
root.mainloop()
