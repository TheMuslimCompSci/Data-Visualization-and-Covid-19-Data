import tkinter as tk
from data_by_board_plots import DataByBoardPlots


class DataByBoardDashboard(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.plots = DataByBoardPlots()
        self.plots_info = self.plots.get_plots_info()
        self.create_widgets(self.plots_info)

    def create_widgets(self, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(self)
            button["text"] = button_text
            button_plots = DataByBoardPlots(
                button_command_values[0], button_command_values[1],
                button_command_values[2], button_command_values[3])
            button["command"] = button_plots.create_visualization
            button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = DataByBoardDashboard(master=root)
app.mainloop()
