import tkinter as tk
from data_by_board_dashboard import DataByBoardDashboard
from deaths_data_dashboard import DeathsDataDashboard
from trends_in_daily_data_dashboard import TrendsInDailyDataDashboard

class Dashboard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        data_by_board_dashboard_button = tk.Button(self)
        data_by_board_dashboard_button["text"] = "Data By Board Dashboard"
        data_by_board_dashboard_frame = DataByBoardDashboard(tk.Frame)
        data_by_board_dashboard_button["command"] = self.create_dashboard(data_by_board_dashboard_frame)
        data_by_board_dashboard_button.pack(side="top")

        deaths_data_dashboard_button = tk.Button(self)
        deaths_data_dashboard_button["text"] = "Deaths Data Dashboard"
        deaths_data_dashboard_frame = DeathsDataDashboard(tk.Frame)
        deaths_data_dashboard_button["command"] = self.create_dashboard(deaths_data_dashboard_frame)
        deaths_data_dashboard_button.pack(side="top")

        trends_in_daily_data_dashboard_button = tk.Button(self)
        trends_in_daily_data_dashboard_button["text"] = "Trends In Daily Data Dashboard"
        trends_in_daily_data_frame = TrendsInDailyDataDashboard(tk.Frame)
        trends_in_daily_data_dashboard_button["command"] = self.create_dashboard(trends_in_daily_data_frame)
        trends_in_daily_data_dashboard_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_dashboard(self, dashboard):
        root = tk.Tk()
        app = dashboard(master=root)
        app.mainloop()

root = tk.Tk()
app = Dashboard(master=root)
app.mainloop()
