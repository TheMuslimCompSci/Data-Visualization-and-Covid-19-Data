import tkinter as tk


root = tk.Tk()
TOPPINGS = [
    ("P", "P"),
    ("C", "C"),
    ("M", "M"),
    ("O", "O"),
]

pizza = tk.StringVar()
pizza.set("P")

for text, topping in TOPPINGS:
    tk.Radiobutton(root, text=text, variable=pizza, value=topping).pack()

def clicked(value):
    myLabel = tk.Label(root, text=value)
    myLabel.pack()

myButton = tk.Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
tk.mainloop()