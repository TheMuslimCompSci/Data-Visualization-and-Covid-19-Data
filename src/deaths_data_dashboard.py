import tkinter as tk
from deaths_data_plots import DeathsDataPlots


class DeathsDataDashboard(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.cumulative_deaths = tk.Button(self)
        self.cumulative_deaths["text"] = "Cumulative Deaths"
        self.cumulative_deaths_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 1 data.csv",
            "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
            "Cumulative number of deaths", [y * 500 for y in range(1, 10)])
        self.cumulative_deaths["command"] = self.cumulative_deaths_plots.create_plots
        self.cumulative_deaths.pack(side="top")

        self.cumulative_deaths_different_data = tk.Button(self)
        self.cumulative_deaths_different_data["text"] = "Cumulative Deaths Different Data"
        self.cumulative_deaths_different_data_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 2 data.csv",
            "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
            "Cumulative number of deaths", [y * 500 for y in range(1, 10)])
        self.cumulative_deaths_different_data["command"] = self.cumulative_deaths_different_data_plots.create_plots
        self.cumulative_deaths_different_data.pack(side="top")

        self.covid_deaths_by_age = tk.Button(self)
        self.covid_deaths_by_age["text"] = "COVID Deaths By Age"
        self.covid_deaths_by_age_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 3a and 3b data.csv",
            "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
            "Number of deaths", [y * 200 for y in range(1, 11)])
        self.covid_deaths_by_age["command"] = self.covid_deaths_by_age_plots.create_plots
        self.covid_deaths_by_age.pack(side="top")

        self.all_deaths_by_age = tk.Button(self)
        self.all_deaths_by_age["text"] = "All Deaths By Age"
        self.all_deaths_by_age_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 3a and 3b data.csv",
            "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
            "Number of deaths", [y * 2000 for y in range(1, 8)])
        self.all_deaths_by_age["command"] = self.all_deaths_by_age_plots.create_plots
        self.all_deaths_by_age.pack(side="top")

        self.deaths_by_board = tk.Button(self)
        self.deaths_by_board["text"] = "Deaths By Board"
        self.deaths_by_board_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 4 data.csv",
            "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
            "Number of deaths", [y * 2000 for y in range(1, 8)])
        self.deaths_by_board["command"] = self.deaths_by_board_plots.create_plots
        self.deaths_by_board.pack(side="top")

        self.deaths_by_week = tk.Button(self)
        self.deaths_by_week["text"] = "Deaths By Week"
        self.deaths_by_week_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 5 data.csv",
            "Deaths by week of registration, Scotland, 2020",
            "Number of deaths", [y * 5000 for y in range(1, 6)])
        self.deaths_by_week["command"] = self.deaths_by_week_plots.create_plots
        self.deaths_by_week.pack(side="top")

        self.deaths_by_cause = tk.Button(self)
        self.deaths_by_cause["text"] = "Deaths By Cause"
        self.deaths_by_cause_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 6 data.csv",
            "Excess Deaths by underlying cause of death1 and location, week 12 to 30, 2020",
            "Number of deaths", [y * 5000 for y in range(1, 6)])
        self.deaths_by_cause["command"] = self.deaths_by_cause_plots.create_plots
        self.deaths_by_cause.pack(side="top")

        self.deaths_by_location = tk.Button(self)
        self.deaths_by_location["text"] = "Deaths By Location"
        self.deaths_by_location_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 7 data.csv",
            "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
            "Number of deaths", [y * 50 for y in range(1, 9)])
        self.deaths_by_location["command"] = self.deaths_by_location_plots.create_plots
        self.deaths_by_location.pack(side="top")

        self.deaths_by_date_and_registration = tk.Button(self)
        self.deaths_by_date_and_registration["text"] = "Deaths By Date Of Death vs Date Of Registration"
        self.deaths_by_date_and_registration_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 8 data.csv",
            "Deaths involving COVID-19, date of death vs date of registration",
            "Number of deaths", [y * 500 for y in range(1, 10)])
        self.deaths_by_date_and_registration["command"] = self.deaths_by_date_and_registration_plots.create_plots
        self.deaths_by_date_and_registration.pack(side="top")

        self.deaths_by_date_and_registration = tk.Button(self)
        self.deaths_by_date_and_registration["text"] = "Deaths By Date Of Death vs Date Of Registration"
        self.deaths_by_date_and_registration_plots = DeathsDataPlots(
            "../covid deaths data week 30/Figure 8 data.csv",
            "Deaths involving COVID-19, date of death vs date of registration",
            "Number of deaths", [y * 500 for y in range(1, 10)])
        self.deaths_by_date_and_registration["command"] = self.deaths_by_date_and_registration_plots.create_plots
        self.deaths_by_date_and_registration.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = DeathsDataDashboard(master=root)
app.mainloop()
