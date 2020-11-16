import tkinter as tk
from data_by_board_plots import DataByBoardPlots


class DataByBoardDashboard(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buttons_dict = self.create_buttons_dict()
        self.create_widgets(self.buttons_dict)

    def create_buttons_dict(self):
        self.buttons = {
            "Cumulative Cases": ["../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv",
                                 "The cumulative number of cases with positive tests for COVID-19, by board in Scotland",
                                 "Cumulative Cases", [y * 2000 for y in range(1, 10)]],

            "ICU Patients Confirmed": ["../COVID-19 data by NHS Board 22 July 2020/Table 2a - ICU patients.csv",
                                       "The daily number of COVID-19 inpatients (confirmed) in ICU at midnight, by board in Scotland",
                                       "ICU Patients", [y * 20 for y in range(1, 12)]],

            "ICU Patients Suspected": ["../COVID-19 data by NHS Board 22 July 2020/Table 2b - ICU patients (Hist.).csv",
                                       "The daily number of COVID-19 inpatients (suspected) in ICU at midnight, by board in Scotland",
                                       "ICU Patients", [y * 20 for y in range(1, 12)]],

            "Hospital Confirmed": ["../COVID-19 data by NHS Board 22 July 2020/Table 3a - Hospital Confirmed.csv",
                                   "The daily number of confirmed COVID-19 inpatients in hospital at midnight, by board in Scotland",
                                   "Hospital Patients", [y * 200 for y in range(1, 9)]],

            "Hospital Suspected": ["../COVID-19 data by NHS Board 22 July 2020/Table 3b- Hospital Suspected.csv",
                                   "The daily number of suspected COVID-19 inpatients in hospital at midnight, by board in Scotland",
                                   "Hospital Patients", [y * 50 for y in range(1, 11)]]
        }
        return self.buttons

    def create_widgets(self, buttons):
        for button_text, button_command_values in buttons.items():
            button = tk.Button(self)
            button["text"] = button_text
            button_plots = DataByBoardPlots(
                button_command_values[0], button_command_values[1],
                button_command_values[2], button_command_values[3])
            button["command"] = button_plots.create_plots
            button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = DataByBoardDashboard(master=root)
app.mainloop()
