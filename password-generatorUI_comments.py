import random   # This module will be used to generate random numbers
import string   # This module will be used to get all the letters, digits and special characters
import tkinter as tk  # This module will be used to create the GUI
import pyperclip  # This module will be used to copy the password to the clipboard

def generate_password(min_length, numbers=True, special_characters=True):  # This function will generate the password
    letters = string.ascii_letters # Get all the letters
    digits = string.digits # Get all the digits
    special = string.punctuation # Get all the special characters
 
    characters = letters # Start with the letters
    if numbers: # If numbers are required, add them to the list of characters
        characters += digits  # Add the digits to the list of characters
    if special_characters: # If special characters are required, add them to the list of characters
        characters += special   # Add the special characters to the list of characters
    
    pwd = ""  # Start with an empty string
    meets_criteria = False # Set the criteria to False
    has_number = False  # Set the number flag to False
    has_special = False # Set the special flag to False
    
    while not meets_criteria or len(pwd) < min_length: # Loop until the password meets the criteria
      new_char = random.choice(characters) # Choose a random character from the list of characters
      pwd += new_char # Add the character to the password
      
      if new_char in digits: # Check if the character is a digit
        has_number = True # Set the number flag to True 
      elif new_char in special: # Check if the character is a special character
        has_special = True # Set the special flag to True
        
      meets_criteria = True # Set the criteria to True
      if numbers: # Check if numbers are required
        meets_criteria = has_number # Set the criteria to the number flag
      if special_characters: # Check if special characters are required
        meets_criteria = meets_criteria and has_special # Set the criteria to the criteria and the special flag
      
    return pwd # Return the password

def generate_and_display_password():   # This function will be called when the button is clicked
    min_length = int(min_length_entry.get()) # Get the value from the entry
    has_number = has_number_var.get() # Get the value from the checkbox
    has_special = has_special_var.get() # Get the value from the checkbox
    pwd = generate_password(min_length, has_number, has_special) # Generate the password
    password_display_label.configure(text="Generated Password: " + pwd) # Display the password
    copy_button = tk.Button(root, text="Copy Password", command=lambda: pyperclip.copy(pwd), font=("Helvetica", 14), background="#4CAF50", foreground="#FFFFFF", activebackground="#3E8E41", activeforeground="#FFFFFF", padx=10, pady=5) # Create the button
    copy_button.pack(pady=10) # Add the button to the window

# Create the main window
root = tk.Tk() #
root.title("Password Generator") # Set the title of the window
root.configure(background="#F9F9F9") # Set the background color of the window

# Create the UI elements
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18), background="#F9F9F9")
min_length_label = tk.Label(root, text="Minimum Length:", font=("Helvetica", 12), background="#F9F9F9")
min_length_entry = tk.Entry(root, font=("Helvetica", 12))
has_number_var = tk.BooleanVar() # Boolean variable to store the state of the checkbox
has_number_checkbox = tk.Checkbutton(root, text="Include numbers", variable=has_number_var, font=("Helvetica", 12), background="#F9F9F9") # Create the checkbox
has_special_var = tk.BooleanVar()# Boolean variable to store the state of the checkbox
has_special_checkbox = tk.Checkbutton(root, text="Include special characters", variable=has_special_var, font=("Helvetica", 12), background="#F9F9F9")# Create the checkbox
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Helvetica", 14), background="#4CAF50", foreground="#FFFFFF", activebackground="#3E8E41", activeforeground="#FFFFFF", padx=10, pady=5) # Create the button
password_display_label = tk.Label(root, text="", font=("Helvetica", 14), background="#F9F9F9") # Create the label

# Add the UI elements to the window
title_label.pack(pady=10) # Add the label to the window
min_length_label.pack(pady=5) # Add the label to the window
min_length_entry.pack(pady=5) # Add the entry to the window
has_number_checkbox.pack(pady=5) # Add the checkbox to the window
has_special_checkbox.pack(pady=5) # Add the checkbox to the window
generate_button.pack(pady=10) # Add the button to the window
password_display_label.pack(pady=10) # Add the label to the window

# Start the event loop
root.mainloop() # Start the event loop

