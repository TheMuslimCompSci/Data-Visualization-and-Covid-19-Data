import tkinter as tk
from trends_in_daily_data_plots import TrendsInDailyDataPlots


class TrendsInDailyDataDashboard(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.plots = TrendsInDailyDataPlots()
        self.plots_info = self.plots.get_plots_info()
        self.create_widgets(self.plots_info)

    def create_widgets(self, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(self)
            button["text"] = button_text
            button_plots = TrendsInDailyDataPlots(
                button_command_values[0], button_command_values[1],
                button_command_values[2], button_command_values[3],
                button_command_values[4], button_command_values[5])
            button["command"] = button_plots.create_hospital_care_plot
            button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = TrendsInDailyDataDashboard(master=root)
app.mainloop()
