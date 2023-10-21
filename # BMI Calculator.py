import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("BMI Calculator")

# Create function(s)
def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"

    # Determine BMI category and display a message
    if 18.5 <= bmi < 24.9:
        message = "Normal Weight"
    elif bmi < 18.5:
        message = "Underweight"
    else:
        message = "Overweight"

    label_message['text'] = message

# Create GUI
style = ttk.Style()
style.configure("TLabel", font=('Helvetica', 14))
style.configure("TEntry", font=('Helvetica', 14))
style.configure("TButton", font=('Helvetica', 14))

label_kg = ttk.Label(root, text="Weight (KG):")
label_kg.grid(column=0, row=0, pady=(20, 10))

entry_kg = ttk.Entry(root)
entry_kg.grid(column=1, row=0, pady=(20, 10))

label_height = ttk.Label(root, text="Height (M):")
label_height.grid(column=0, row=1, pady=(10, 10))

entry_height = ttk.Entry(root)
entry_height.grid(column=1, row=1, pady=(10, 10))

button_calculate = ttk.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=2, columnspan=2, pady=(20, 10))

label_result = ttk.Label(root, text="BMI:", font=('Helvetica', 14))
label_result.grid(column=0, row=3, columnspan=2, pady=(10, 10))

label_message = ttk.Label(root, text="", font=('Helvetica', 16), foreground="blue")
label_message.grid(column=0, row=4, columnspan=2, pady=(10, 20))

# Make the window responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()
