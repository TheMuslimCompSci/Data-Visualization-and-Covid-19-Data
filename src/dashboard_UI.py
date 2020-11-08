import tkinter as tk
from data_by_board_plots import DataByBoardPlots


class DashboardUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.cumulative_cases = tk.Button(self)
        self.cumulative_cases["text"] = "Cumulative Cases"
        self.cumulative_cases_plots = DataByBoardPlots(
            "../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv",
            "The cumulative number of cases with positive tests for COVID-19, by board in Scotland",
            "Cumulative Cases", [y * 2000 for y in range(1, 10)])
        self.cumulative_cases["command"] = self.cumulative_cases_plots.create_plots
        self.cumulative_cases.pack(side="top")

        self.icu_patients_confirmed = tk.Button(self)
        self.icu_patients_confirmed["text"] = "ICU Patients Confirmed"
        self.icu_patients_confirmed_plots = DataByBoardPlots(
            "../COVID-19 data by NHS Board 22 July 2020/Table 2a - ICU patients.csv",
            "The daily number of COVID-19 inpatients (confirmed) in ICU at midnight, by board in Scotland",
            "ICU Patients", [y * 20 for y in range(1, 12)])
        self.icu_patients_confirmed["command"] = self.icu_patients_confirmed_plots.create_plots
        self.icu_patients_confirmed.pack(side="top")

        self.icu_patients_suspected = tk.Button(self)
        self.icu_patients_suspected["text"] = "ICU Patients Suspected"
        self.icu_patients_suspected_plots = DataByBoardPlots(
            "../COVID-19 data by NHS Board 22 July 2020/Table 2b - ICU patients (Hist.).csv",
            "The daily number of COVID-19 inpatients (suspected) in ICU at midnight, by board in Scotland",
            "ICU Patients", [y * 20 for y in range(1, 12)])
        self.icu_patients_suspected["command"] = self.icu_patients_suspected_plots.create_plots
        self.icu_patients_suspected.pack(side="top")

        self.hospital_confirmed = tk.Button(self)
        self.hospital_confirmed["text"] = "Hospital Confirmed"
        self.hospital_confirmed_plots = DataByBoardPlots(
            "../COVID-19 data by NHS Board 22 July 2020/Table 3a - Hospital Confirmed.csv",
            "The daily number of confirmed COVID-19 inpatients in hospital at midnight, by board in Scotland",
            "Hospital Patients", [y * 200 for y in range(1, 9)])
        self.hospital_confirmed["command"] = self.hospital_confirmed_plots.create_plots
        self.hospital_confirmed.pack(side="top")

        self.hospital_suspected = tk.Button(self)
        self.hospital_suspected["text"] = "Hospital Suspected"
        self.hospital_suspected_plots = DataByBoardPlots(
            "../COVID-19 data by NHS Board 22 July 2020/Table 3b- Hospital Suspected.csv",
            "The daily number of suspected COVID-19 inpatients in hospital at midnight, by board in Scotland",
            "Hospital Patients", [y * 50 for y in range(1, 11)])
        self.hospital_suspected["command"] = self.hospital_suspected_plots.create_plots
        self.hospital_suspected.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = DashboardUI(master=root)
app.mainloop()
