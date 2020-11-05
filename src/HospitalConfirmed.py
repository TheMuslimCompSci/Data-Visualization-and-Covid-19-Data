import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""Represents plots from Table 3a: Daily Number of confirmed COVID-19 Inpatients in Hospital at Midnight
- as reported from dates 26/03/20 to 22/07/20 on SG website"""


class HospitalConfirmed(object):

    def __init__(self):
        self.create_plots()

    def create_plots(self):
        hospital_confirmed = pd.read_csv("../COVID-19 data by NHS Board 22 July 2020/Table 3a - Hospital Confirmed.csv")
        boards = hospital_confirmed.columns.tolist()
        dates = hospital_confirmed["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            ax = sns.barplot(data=hospital_confirmed, x="Date", y=board)
            ax.set_title(board)
            x_values = dates[::5]
            #ax.set_xticks(x_values)
            #ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_yticks([y * 200 for y in range(1, 9)])
            ax.set_ylabel("Hospital Patients")
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle("The daily number of confirmed COVID-19 inpatients in hospital at midnight, by board in Scotland")
        plt.show()

#change classes, csv variables, subplot size somtimes, plot sometimes, xticks sometimes,
# yticks sometimes, ylabels sometimes and title
HospitalConfirmed()
