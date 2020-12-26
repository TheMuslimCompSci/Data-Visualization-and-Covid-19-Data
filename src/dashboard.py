import tkinter as tk
from data_by_board_plots import DataByBoardPlots
from deaths_data_plots import DeathsDataPlots
from trends_in_daily_data_plots import TrendsInDailyDataPlots


class Dashboard(object):
    
    def __init__(self, master):
        master.title("COVID-19 Data Visualization App")
        master.state("zoomed")
        self.dashboard_frame = tk.Frame(master, bg="blue")
        self.data_by_board_dashboard_frame = tk.Frame(master, bg="blue")
        self.deaths_data_dashboard_frame = tk.Frame(master, bg="blue")
        self.trends_in_daily_data_dashboard_frame = tk.Frame(master, bg="blue")
        self.create_dashboard()

    def create_dashboard(self):
        self.hide_all_frames()
        self.dashboard_frame.pack(fill="both", expand=True)

        plots_dashboard_buttons = {
            "Data By Board Dashboard": [self.data_by_board_dashboard_frame, [0, 0]],
            "Deaths Data Dashboard": [self.deaths_data_dashboard_frame, [0, 1]],
            "Trends In Daily Data Dashboard": [self.trends_in_daily_data_dashboard_frame, [1, 0]],
        }

        for button_text, button_info in plots_dashboard_buttons.items():
            button = tk.Button(self.dashboard_frame, bg="white")
            button["text"] = button_text
            button["command"] = self.create_plots_dashboard(button_info[0])
            button.grid(row=button_info[1][0], column=button_info[1][1], sticky="nesw")
        quit_button = tk.Button(self.dashboard_frame, text="QUIT", fg="red", command=self.dashboard_frame.quit)
        quit_button.grid(row=1, column=1, sticky="nesw")


        tk.Grid.rowconfigure(self.dashboard_frame, index=0, weight=1)
        tk.Grid.rowconfigure(self.dashboard_frame, index=1, weight=1)
        tk.Grid.columnconfigure(self.dashboard_frame, index=0, weight=1)
        tk.Grid.columnconfigure(self.dashboard_frame, index=1, weight=1)

    def create_plots_dashboard(self, frame):
        self.hide_all_frames()
        frame.pack(fill="both", expand=True)
        if frame == self.data_by_board_dashboard_frame:
            plots = DataByBoardPlots()
        elif frame == self.deaths_data_dashboard_frame:
            plots = DeathsDataPlots()
        elif frame == self.trends_in_daily_data_dashboard_frame:
            plots = TrendsInDailyDataPlots()
        plots_buttons = plots.get_plots_info()
        self.create_widgets(frame, plots_buttons)

    def create_data_by_board_dashboard(self):
        self.hide_all_frames()
        self.data_by_board_dashboard_frame.pack(fill="both", expand=True)
        data_by_board_plots = DataByBoardPlots()
        data_by_board_plots_buttons = data_by_board_plots.get_plots_info()
        self.create_widgets(self.data_by_board_dashboard_frame, data_by_board_plots_buttons)

    def create_deaths_data_dashboard(self):
        self.hide_all_frames()
        self.deaths_data_dashboard_frame.pack(fill="both", expand=True)
        deaths_data_plots = DeathsDataPlots()
        deaths_data_plots_buttons = deaths_data_plots.get_plots_info()
        self.create_widgets(self.deaths_data_dashboard_frame, deaths_data_plots_buttons)

    def create_trends_in_daily_data_dashboard(self):
        self.hide_all_frames()
        self.trends_in_daily_data_dashboard_frame.pack(fill="both", expand=True)
        trends_in_daily_data_plots = TrendsInDailyDataPlots()
        trends_in_daily_data_plots_buttons = trends_in_daily_data_plots.get_plots_info()
        self.create_widgets(self.trends_in_daily_data_dashboard_frame, trends_in_daily_data_plots_buttons)
    
    def create_widgets(self, frame, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(frame, bg="white")
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

    def hide_all_frames(self):
        self.dashboard_frame.pack_forget()
        self.data_by_board_dashboard_frame.pack_forget()
        self.deaths_data_dashboard_frame.pack_forget()
        self.trends_in_daily_data_dashboard_frame.pack_forget()


root = tk.Tk()
app = Dashboard(root)
root.mainloop()
