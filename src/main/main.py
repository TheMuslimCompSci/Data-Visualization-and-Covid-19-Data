# This is the main Python script for the program.
import sys
import tkinter as tk
from src.main.dashboard import Dashboard

# Launch the COVID-19 Data Visualization App
def launch_app():
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()


# Gets run after Shift+F10 is pressed to execute code
if __name__ == '__main__':
    launch_app()
