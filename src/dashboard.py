import tkinter as tk
from data_by_board_plots import DataByBoardPlots
from deaths_data_plots import DeathsDataPlots
from trends_in_daily_data_plots import TrendsInDailyDataPlots
from functools import partial


class Dashboard(object):

    def __init__(self, master, button_plots):
        master.title("COVID-19 Data Visualization App")
        master.state("zoomed")
        self.create_frames(master)
        self.dashboard_buttons_info = self.get_main_dashboard_buttons_info()
        self.create_main_dashboard(self.dashboard_buttons_info)

    def create_frames(self, master):
        self.main_dashboard_frame = tk.Frame(master, bg="blue")
        self.data_by_board_dashboard_frame = tk.Frame(master, bg="blue")
        self.deaths_data_dashboard_frame = tk.Frame(master, bg="blue")
        self.trends_in_daily_data_dashboard_frame = tk.Frame(master, bg="blue")
        self.analytics_dashboard_frame = tk.Frame(master, bg="blue")

    def get_main_dashboard_buttons_info(self):
        buttons_info = {
            "Data By Board Dashboard": self.create_data_by_board_dashboard,
            "Deaths Data Dashboard": self.create_deaths_data_dashboard,
            "Trends In Daily Data Dashboard": self.create_trends_in_daily_data_dashboard,
            "QUIT": self.main_dashboard_frame.quit
        }
        return buttons_info

    def create_main_dashboard(self, buttons_info):
        self.hide_all_frames()
        self.main_dashboard_frame.pack(fill="both", expand=True)
        row_index = 0
        column_index = 0
        counter = 0
        for button_text, button_command in buttons_info.items():
            button = tk.Button(self.main_dashboard_frame, bg="white")
            button["text"] = button_text
            button["command"] = button_command
            button.grid(row=row_index, column=column_index, sticky="nesw")
            counter += 1
            if counter % 2 == 0:
                row_index += 1
            if column_index == 1:
                column_index = 0
            else:
                column_index = 1
        self.configure_buttons_layout(self.main_dashboard_frame)

    def create_plots_dashboard(self, frame):
        self.hide_all_frames()
        frame.pack(fill="both", expand=True)
        if frame == self.data_by_board_dashboard_frame:
            plots = DataByBoardPlots()
        elif frame == self.deaths_data_dashboard_frame:
            plots = DeathsDataPlots()
        elif frame == self.trends_in_daily_data_dashboard_frame:
            plots = TrendsInDailyDataPlots()
        plots_buttons_info = plots.get_plots_info()
        self.create_plots_dashboard_buttons(frame, plots_buttons_info)

    def create_plots_dashboard_buttons(self, frame, buttons):
        row_index = 0
        column_index = 0
        counter = 0
        button_widgets = []
        for button_text in buttons.keys():
            button = tk.Button(frame, bg="white")
            button["text"] = button_text
            button.grid(row=row_index, column=column_index, sticky="nesw")
            counter += 1
            if counter % 2 == 0:
                row_index += 1
            if column_index == 1:
                column_index = 0
            else:
                column_index = 1
        self.configure_buttons_layout(frame)
        for button_command_values in buttons.values():
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
            button["command"] = self.create_analytics_dashboard

    def create_analytics_dashboard(self):
        self.hide_all_frames()
        self.analytics_dashboard_frame.pack(fill="both", expand=True)
        plot_button = tk.Button(self.analytics_dashboard_frame, bg="white")
        plot_button["text"] = "Plot"
        #plot_button["command"] = create_visualization
        plot_button.grid(row=0, column=0, sticky="nesw")
        data_button = tk.Button(self.analytics_dashboard_frame, bg="white")
        data_button["text"] = "Data"
        #data_button["command"] = plot.create_visualization
        data_button.grid(row=0, column=1, sticky="nesw")
        statistics_button = tk.Button(self.analytics_dashboard_frame, bg="white")
        statistics_button["text"] = "Statistics"
        #statistics_button["command"] = plot.create_visualization
        statistics_button.grid(row=1, column=0, sticky="nesw")
        self.configure_buttons_layout(self.analytics_dashboard_frame)

    def hide_all_frames(self):
        frames = [self.main_dashboard_frame, self.data_by_board_dashboard_frame, self.deaths_data_dashboard_frame,
                  self.trends_in_daily_data_dashboard_frame, self.analytics_dashboard_frame]
        for frame in frames:
            frame.pack_forget()

    def configure_buttons_layout(self, frame):
        grid_size = tk.Grid.size(frame)
        for i in range(grid_size[0]):
            tk.Grid.columnconfigure(frame, index=i, weight=1)
        for i in range(grid_size[1]):
            tk.Grid.rowconfigure(frame, index=i, weight=1)

    def create_data_by_board_dashboard(self):
        self.create_plots_dashboard(self.data_by_board_dashboard_frame)

    def create_deaths_data_dashboard(self):
        self.create_plots_dashboard(self.deaths_data_dashboard_frame)

    def create_trends_in_daily_data_dashboard(self):
        self.create_plots_dashboard(self.trends_in_daily_data_dashboard_frame)


root = tk.Tk()
app = Dashboard(root, None)
root.mainloop()
