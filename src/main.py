import tkinter as tk
from dashboard import Dashboard


def launch_app():
    root = tk.Tk()
    Dashboard(root)
    root.mainloop()


if __name__ == '__main__':
    launch_app()
