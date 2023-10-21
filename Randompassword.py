import tkinter as tk
from tkinter import ttk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text=f"Generated Password: {password}")

app = tk.Tk()
app.title("Random Password Generator")

# Create a custom style
style = ttk.Style()

# Configure the style for the title label
style.configure("Title.TLabel", font=("Helvetica", 16), foreground="navy", padding=(10, 10))

# Configure the style for the result label
style.configure("Result.TLabel", font=("Helvetica", 12), background="lightgreen", foreground="blue", padding=(5, 5))

# Create the main frame
mainframe = ttk.Frame(app, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Create and style the title label
title_label = ttk.Label(mainframe, text="Random Password Generator", style="Title.TLabel")
title_label.grid(column=1, row=0, columnspan=2, sticky=(tk.W, tk.E))

# Create the input elements
length_label = ttk.Label(mainframe, text="Password Length:")
length_label.grid(column=1, row=1, sticky=tk.W)

length_entry = ttk.Entry(mainframe)
length_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

digits_var = tk.BooleanVar()
digits_check = ttk.Checkbutton(mainframe, text="Include Digits", variable=digits_var)
digits_check.grid(column=2, row=2, sticky=tk.W)

symbols_var = tk.BooleanVar()
symbols_check = ttk.Checkbutton(mainframe, text="Include Symbols", variable=symbols_var)
symbols_check.grid(column=2, row=3, sticky=tk.W)

# Create and style the Generate Password button
generate_button = ttk.Button(mainframe, text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=4, sticky=tk.W)
style.configure("TButton", foreground="white", background="blue")

# Create and style the result label
result_label = ttk.Label(mainframe, text="Generated Password: [Password]", style="Result.TLabel")
result_label.grid(column=1, row=5, columnspan=2, sticky=(tk.W, tk.E))

# Configure padding for all children of the main frame
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Set the focus on the length entry field
length_entry.focus()

app.mainloop()
