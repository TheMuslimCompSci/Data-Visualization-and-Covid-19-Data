import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""Represents plots from Table 2a: Daily Number of COVID-19 Inpatients (Confirmed) in ICU at Midnight
- as reported from dates 26/03/20 to 22/07/20 on SG website"""


class ICUPatientsConfirmed(object):

    def __init__(self):
        self.create_plots()

    def create_plots(self):
        icu_patients_confirmed = pd.read_csv("../COVID-19 data by NHS Board 22 July 2020/Table 2a - ICU patients.csv")
        boards = icu_patients_confirmed.columns.tolist()
        dates = icu_patients_confirmed["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            ax = sns.barplot(data=icu_patients_confirmed, x="Date", y=board)
            ax.set_title(board)
            x_values = dates[::5]
            #ax.set_xticks(x_values)
            #ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_yticks([y * 20 for y in range(1, 12)])
            ax.set_ylabel("ICU Patients")
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle("The daily number of COVID-19 inpatients (confirmed) in ICU at midnight, by board in Scotland")
        plt.show()


ICUPatientsConfirmed()
