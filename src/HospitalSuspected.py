import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""Represents plots from Table 3b: Daily Number of suspected COVID-19 Inpatients in Hospital at Midnight
- as reported from dates 26/03/20 to 21/07/20 on SG website"""


class HospitalSuspected(object):

    def __init__(self):
        self.create_plots()

    def create_plots(self):
        hospital_suspected = pd.read_csv("../COVID-19 data by NHS Board 22 July 2020/Table 3b- Hospital Suspected.csv")
        boards = hospital_suspected.columns.tolist()
        dates = hospital_suspected["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            ax = sns.barplot(data=hospital_suspected, x="Date", y=board)
            ax.set_title(board)
            x_values = dates[::5]
            #ax.set_xticks(x_values)
            #ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_yticks([y * 50 for y in range(1, 11)])
            ax.set_ylabel("Hospital Patients")
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle("The daily number of suspected COVID-19 inpatients in hospital at midnight, by board in Scotland")
        plt.show()

#change classes, csv variables, subplot size somtimes, plot sometimes, xticks sometimes,
# yticks sometimes, ylabels sometimes and title
HospitalSuspected()
