import random   
import string   
import tkinter as tk  
import pyperclip  

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
    copy_button = tk.Button(root, text="Copy Password", command=lambda: pyperclip.copy(pwd), font=("Helvetica", 14), background="#4CAF50", foreground="#FFFFFF", activebackground="#3E8E41", activeforeground="#FFFFFF", padx=10, pady=5) 
    copy_button.pack(pady=10) 

# Create the main window
root = tk.Tk() 
root.title("Password Generator") 
root.configure(background="#F9F9F9") 

# Create the UI elements
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18), background="#F9F9F9")
min_length_label = tk.Label(root, text="Minimum Length:", font=("Helvetica", 12), background="#F9F9F9")
min_length_entry = tk.Entry(root, font=("Helvetica", 12))
has_number_var = tk.BooleanVar() 
has_number_checkbox = tk.Checkbutton(root, text="Include numbers", variable=has_number_var, font=("Helvetica", 12), background="#F9F9F9") 
has_special_var = tk.BooleanVar()
has_special_checkbox = tk.Checkbutton(root, text="Include special characters", variable=has_special_var, font=("Helvetica", 12), background="#F9F9F9")
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, font=("Helvetica", 14), background="#4CAF50", foreground="#FFFFFF", activebackground="#3E8E41", activeforeground="#FFFFFF", padx=10, pady=5) 
password_display_label = tk.Label(root, text="", font=("Helvetica", 14), background="#F9F9F9") 

# Add the UI elements to the window
title_label.pack(pady=10) 
min_length_label.pack(pady=5) 
min_length_entry.pack(pady=5) 
has_number_checkbox.pack(pady=5) 
has_special_checkbox.pack(pady=5) 
generate_button.pack(pady=10) 
password_display_label.pack(pady=10) 

# Start the event loop
root.mainloop() 
