import tkinter as tk
from dashboard import Dashboard


def launch_app():
    root = tk.Tk()
    app = Dashboard(root, None)
    root.mainloop()

if __name__ == '__main__':
    launch_app()