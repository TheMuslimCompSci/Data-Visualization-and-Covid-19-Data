import tkinter as tk
from trends_in_daily_data_plots import TrendsInDailyDataPlots


class TrendsInDailyDataDashboard(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buttons_dict = self.create_buttons_dict()
        self.create_widgets(self.buttons_dict)

    def create_buttons_dict(self):
        self.buttons = {
            "NHS 24": ["../Trends in daily COVID-19 data 22 July 2020/Table 1 - NHS 24.csv",
                       "Daily number of calls to NHS24 111 and the Coronavirus helpline",
                       "Number of calls", [y * 2000 for y in range(1, 8)]],

            "Hospital Confirmed": ["../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                   "Daily number of confirmed COVID-19 patients in hospital",
                                   "Number of patients", [y * 200 for y in range(1, 9)]],

            "Hospital Care (ICU)": ["../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                    "Daily number of confirmed COVID-19 patients in ICU or combined ICU/HDU",
                                    "Number of patients", [y * 50 for y in range(1, 6)]],

            "Ambulance Attendances": ["../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of Attendances (total and COVID-19 suspected)",
                                      "Number of attendances", [y * 200 for y in range(1, 11)]],

            "Ambulance To Hospital": ["../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of suspected COVID-19 patients taken to hospital by ambulance",
                                      "Number of patients", [y * 50 for y in range(1, 9)]],

            "Delayed Discharges": ["../COVID-19 data by NHS Board 22 July 2020/Table 4 - Delayed Discharges.csv",
                                   "Daily Delayed Discharges",
                                   "Number of delayed discharges", [y * 200 for y in range(1, 10)]],

            "People Tested": ["../COVID-19 data by NHS Board 22 July 2020/Table 5 - Testing.csv",
                              "Number of people tested for COVID-19 in Scotland to date, by results",
                              "Number of people tested", [y * 50000 for y in range(1, 8)]],

            "Number Of Tests": ["../COVID-19 data by NHS Board 22 July 2020/Table 5 - Testing.csv",
                                "Cumulative number of COVID-19 Tests carried out in Scotland",
                                "Number of tests", [y * 100000 for y in range(1, 8)]],

            "Daily Positive Cases": ["../COVID-19 data by NHS Board 22 July 2020/Table 5 - Testing.csv",
                                     "Number of daily new positive cases and 7-day rolling average",
                                     "Number of cases", [y * 50 for y in range(1, 11)]],

            "Workforce": ["../COVID-19 data by NHS Board 22 July 2020/Table 6 - Workforce.csv",
                          "Number of NHS staff reporting as absent due to Covid-19",
                          "Number of staff", [y * 1000 for y in range(1, 11)]],

            "Care Homes": ["../COVID-19 data by NHS Board 22 July 2020/Table 7a - Care Homes.csv",
                           "Daily number of new suspected Covid-19 cases reported in Scottish adult care homes",
                           "Number of cases", [y * 50 for y in range(1, 6)]],

            "Deaths": ["../COVID-19 data by NHS Board 22 July 2020/Table 8 - Deaths.csv",
                       "Number of COVID-19 confirmed deaths registered to date",
                       "Number of deaths", [y * 500 for y in range(1, 7)]],
        }
        return self.buttons

    def create_widgets(self, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(self)
            button["text"] = button_text
            button_plots = TrendsInDailyDataPlots(
                button_command_values[0], button_command_values[1],
                button_command_values[2], button_command_values[3])
            button["command"] = button_plots.create_visualiztion
            button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = TrendsInDailyDataDashboard(master=root)
app.mainloop()
