import tkinter as tk

# Function to update the label with the button's text
def button_click(value):
    current_text = display_label["text"]
    display_label.config(text=current_text + str(value))

# Function to evaluate the expression in the label
def evaluate():
    try:
        result = eval(display_label["text"])
        display_label.config(text=str(result))
    except Exception as e:
        display_label.config(text="Error")

# Function to clear the display
def clear_display():
    display_label.config(text="")

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Create a label to display the input and result
display_label = tk.Label(app,width=20,text="", anchor="e", bg="white", fg="black", font=("Arial", 24), relief="sunken", height=2)
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Add buttons to the grid
for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, bg="green", command=evaluate)
    else:
        button = tk.Button(app, text=text, bg="cyan" ,command=lambda t=text: button_click(t))
    button.grid(row=row, column=column,  sticky="nsew")

# Add a clear button
clear_button = tk.Button(app, text="C", bg="red" ,command=clear_display)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Make the buttons expand with the window
for i in range(6):
    app.rowconfigure(i, weight=1)
for i in range(4):
    app.columnconfigure(i, weight=1)

# Run the Tkinter event loop
app.mainloop()
