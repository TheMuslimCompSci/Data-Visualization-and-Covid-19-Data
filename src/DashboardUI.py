import tkinter as tk
from cumulative import CumulativeCases

class DashboardUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.cumulative_cases = tk.Button(self)
        self.cumulative_cases["text"] = "Cumulative Cases"
        self.cumulative_cases["command"] = CumulativeCases
        self.cumulative_cases.pack(side="top")

        self.icu_patients_confirmed = tk.Button(self)
        self.icu_patients_confirmed["text"] = "ICU Patients Confirmed"
        self.icu_patients_confirmed["command"] = CumulativeCases
        self.icu_patients_confirmed.pack(side="top")

        self.icu_patients_suspected = tk.Button(self)
        self.icu_patients_suspected["text"] = "ICU Patients Suspected"
        self.icu_patients_suspected["command"] = CumulativeCases
        self.icu_patients_suspected.pack(side="top")

        self.hospital_confirmed = tk.Button(self)
        self.hospital_confirmed["text"] = "Hospital Confirmed"
        self.hospital_confirmed["command"] = CumulativeCases
        self.hospital_confirmed.pack(side="top")

        self.hospital_suspected = tk.Button(self)
        self.hospital_suspected["text"] = "Hospital Suspected"
        self.hospital_suspected["command"] = CumulativeCases
        self.hospital_suspected.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = DashboardUI(master=root)
app.mainloop()
