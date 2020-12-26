import tkinter as tk
from data_by_board_plots import DataByBoardPlots
from deaths_data_plots import DeathsDataPlots
from trends_in_daily_data_plots import TrendsInDailyDataPlots


class Dashboard(object):
    
    def __init__(self, master):
        master.title("COVID-19 Data Visualization App")
        self.dashboard_frame = tk.Frame(master, bg="green")
        self.data_by_board_dashboard_frame = tk.Frame(master, bg="red")
        self.deaths_data_dashboard_frame = tk.Frame(master, bg="blue")
        self.trends_in_daily_data_dashboard_frame = tk.Frame(master, bg="yellow")
        self.create_dashboard()

    def create_data_by_board_dashboard(self):
        self.hide_all_frames()
        self.data_by_board_dashboard_frame.pack(fill="both", expand=1)
        data_by_board_plots = DataByBoardPlots()
        data_by_board_plots_buttons = data_by_board_plots.get_plots_info()
        self.create_widgets(self.data_by_board_dashboard_frame, data_by_board_plots_buttons)
    
    
    def create_deaths_data_dashboard(self):
        self.hide_all_frames()
        self.deaths_data_dashboard_frame.pack(fill="both", expand=1)
        deaths_data_plots = DeathsDataPlots()
        deaths_data_plots_buttons = deaths_data_plots.get_plots_info()
        self.create_widgets(self.deaths_data_dashboard_frame, deaths_data_plots_buttons)
    
    def create_trends_in_daily_data_dashboard(self):
        self.hide_all_frames()
        self.trends_in_daily_data_dashboard_frame.pack(fill="both", expand=1)
        trends_in_daily_data_plots = TrendsInDailyDataPlots()
        trends_in_daily_data_plots_buttons = trends_in_daily_data_plots.get_plots_info()
        self.create_widgets(self.trends_in_daily_data_dashboard_frame, trends_in_daily_data_plots_buttons)
    
    def create_dashboard(self):
        self.hide_all_frames()
        self.dashboard_frame.pack(fill="both", expand=1)
    
        data_by_board_dashboard_button = tk.Button(self.dashboard_frame)
        data_by_board_dashboard_button["text"] = "Data By Board Dashboard"
        data_by_board_dashboard_button["command"] = self.create_data_by_board_dashboard
        data_by_board_dashboard_button.pack(side="top")
    
        deaths_data_dashboard_button = tk.Button(self.dashboard_frame)
        deaths_data_dashboard_button["text"] = "Deaths Data Dashboard"
        deaths_data_dashboard_button["command"] = self.create_deaths_data_dashboard
        deaths_data_dashboard_button.pack(side="top")
    
        trends_in_daily_data_dashboard_button = tk.Button(self.dashboard_frame)
        trends_in_daily_data_dashboard_button["text"] = "Trends In Daily Data Dashboard"
        trends_in_daily_data_dashboard_button["command"] = self.create_trends_in_daily_data_dashboard
        trends_in_daily_data_dashboard_button.pack(side="top")

        quit_button = tk.Button(self.dashboard_frame, text="QUIT", fg="red", command=self.dashboard_frame.quit)
        quit_button.pack(side="bottom")
    
    def hide_all_frames(self):
        self.dashboard_frame.pack_forget()
        self.data_by_board_dashboard_frame.pack_forget()
        self.deaths_data_dashboard_frame.pack_forget()
        self.trends_in_daily_data_dashboard_frame.pack_forget()
    
    def create_widgets(self, frame, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(frame)
            button["text"] = button_text
            if len(buttons) == 5:
                button_plots = DataByBoardPlots(button_command_values[0], button_command_values[1],
                                                button_command_values[2], button_command_values[3])
            elif len(buttons) == 9:
                button_plots = DeathsDataPlots(button_command_values[0], button_command_values[1],
                                               button_command_values[2], button_command_values[3],
                                               button_command_values[4])
            elif len(buttons) == 12:
                button_plots = TrendsInDailyDataPlots(button_command_values[0], button_command_values[1],
                                                      button_command_values[2], button_command_values[3],
                                                      button_command_values[4], button_command_values[5])
            button["command"] = button_plots.create_visualization
            button.pack(side="top")


root = tk.Tk()
app = Dashboard(root)
root.mainloop()
