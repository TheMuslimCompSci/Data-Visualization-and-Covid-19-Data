import tkinter as tk
from deaths_data_plots import DeathsDataPlots


class DeathsDataDashboard(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buttons_dict = self.create_buttons_dict()
        self.create_widgets(self.buttons_dict)

    def create_buttons_dict(self):
        self.buttons = {
            "Cumulative Deaths": ["../covid deaths data week 30/Figure 1 data.csv",
                                  "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
                                  "Cumulative number of deaths", [y * 500 for y in range(1, 10)]],

            "Cumulative Deaths Different Data": ["../covid deaths data week 30/Figure 2 data.csv",
                                                 "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
                                                 "Cumulative number of deaths", [y * 500 for y in range(1, 10)]],

            "COVID Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                    "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                    "Number of deaths", [y * 200 for y in range(1, 11)]],

            "All Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                  "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                  "Number of deaths", [y * 2000 for y in range(1, 8)]],

            "Deaths By Board": ["../covid deaths data week 30/Figure 4 data.csv",
                                "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
                                "Number of deaths", [y * 2000 for y in range(1, 8)]],

            "Deaths By Week": ["../covid deaths data week 30/Figure 5 data.csv",
                               "Deaths by week of registration, Scotland, 2020",
                               "Number of deaths", [y * 500 for y in range(1, 6)]],

            "Deaths By Cause": ["../covid deaths data week 30/Figure 6 data.csv",
                                "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                "Number of deaths", [y * 5000 for y in range(1, 6)]],

            "Deaths By Location": ["../covid deaths data week 30/Figure 7 data.csv",
                                   "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
                                   "Number of deaths", [y * 50 for y in range(1, 9)]],

            "Deaths By Date Of Death vs Date Of Registration": ["../covid deaths data week 30/Figure 8 data.csv",
                                                                "Deaths involving COVID-19, date of death vs date of registration",
                                                                "Number of deaths", [y * 500 for y in range(1, 10)]]
        }
        return self.buttons

    def create_widgets(self, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(self)
            button["text"] = button_text
            button_plots = DeathsDataPlots()
            if button_text == "Cumulative Deaths":
                button["command"] = button_plots.create_cumulative_deaths_plot
            elif button_text == "Cumulative Deaths Different Data":
                button["command"] = button_plots.create_cumulative_deaths_different_data_plot
            elif button_text == "COVID Deaths By Age":
                button["command"] = button_plots.create_covid_deaths_by_age_plot
            elif button_text == "All Deaths By Age":
                button["command"] = button_plots.create_all_deaths_by_age_plot
            elif button_text == "Deaths By Board":
                button["command"] = button_plots.create_deaths_by_board_plot
            elif button_text == "Deaths By Week":
                button["command"] = button_plots.create_deaths_by_week_plot
            elif button_text == "Deaths By Cause":
                button["command"] = button_plots.create_deaths_by_cause_plot
            elif button_text == "Deaths By Location":
                button["command"] = button_plots.create_deaths_by_location_plot
            elif button_text == "Deaths By Date Of Death vs Date Of Registration":
                button["command"] = button_plots.create_deaths_by_dates_plot
            button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = DeathsDataDashboard(master=root)
app.mainloop()
