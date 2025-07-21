import tkinter as tk

# Function to handle button press
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to handle equal press
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle clear press
def button_clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget for displaying the current calculation
entry = tk.Entry(window, width=30, borderwidth=5, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), command=button_equal)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)


clear_button = tk.Button(window, text='C', width=5, height=2, font=('Arial', 14), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4)


window.mainloop()
