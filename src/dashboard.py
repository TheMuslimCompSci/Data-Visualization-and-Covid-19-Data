import tkinter as tk
from data_by_board_plots import DataByBoardPlots
from deaths_data_plots import DeathsDataPlots
from trends_in_daily_data_plots import TrendsInDailyDataPlots

root = tk.Tk()
root.title("COVID-19 Data Visualization App")

def create_data_by_board_dashboard():
    hide_all_frames()
    data_by_board_dashboard_frame.pack(fill="both", expand=1)
    data_by_board_plots = DataByBoardPlots()
    data_by_board_plots_buttons = data_by_board_plots.get_plots_info()
    create_widgets(data_by_board_dashboard_frame, data_by_board_plots_buttons)


def create_deaths_data_dashboard():
    hide_all_frames()
    deaths_data_dashboard_frame.pack(fill="both", expand=1)
    deaths_data_plots = DeathsDataPlots()
    deaths_data_plots_buttons = deaths_data_plots.get_plots_info()
    create_widgets(deaths_data_dashboard_frame, deaths_data_plots_buttons)

def create_trends_in_daily_data_dashboard():
    hide_all_frames()
    trends_in_daily_data_dashboard_frame.pack(fill="both", expand=1)
    trends_in_daily_data_plots = TrendsInDailyDataPlots()
    trends_in_daily_data_plots_buttons = trends_in_daily_data_plots.get_plots_info()
    create_widgets(trends_in_daily_data_dashboard_frame, trends_in_daily_data_plots_buttons)

def create_dashboard():
    hide_all_frames()
    dashboard_frame.pack(fill="both", expand=1)

    data_by_board_dashboard_button = tk.Button(dashboard_frame)
    data_by_board_dashboard_button["text"] = "Data By Board Dashboard"
    data_by_board_dashboard_button["command"] = create_data_by_board_dashboard
    data_by_board_dashboard_button.pack(side="top")

    deaths_data_dashboard_button = tk.Button(dashboard_frame)
    deaths_data_dashboard_button["text"] = "Deaths Data Dashboard"
    deaths_data_dashboard_button["command"] = create_deaths_data_dashboard
    deaths_data_dashboard_button.pack(side="top")

    trends_in_daily_data_dashboard_button = tk.Button(dashboard_frame)
    trends_in_daily_data_dashboard_button["text"] = "Trends In Daily Data Dashboard"
    trends_in_daily_data_dashboard_button["command"] = create_trends_in_daily_data_dashboard
    trends_in_daily_data_dashboard_button.pack(side="top")

dashboard_frame = tk.Frame(root, bg="green")
data_by_board_dashboard_frame = tk.Frame(root, bg="red")
deaths_data_dashboard_frame = tk.Frame(root, bg="blue")
trends_in_daily_data_dashboard_frame = tk.Frame(root, bg="yellow")

def hide_all_frames():
    dashboard_frame.pack_forget()
    data_by_board_dashboard_frame.pack_forget()
    deaths_data_dashboard_frame.pack_forget()
    trends_in_daily_data_dashboard_frame.pack_forget()

def create_widgets(frame, buttons):
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

create_dashboard()



root.mainloop()









# self.quit = Button(frame, text="QUIT", fg="red",
#                      command=frame.quit)
# self.quit.pack(side="bottom")