import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""Represents plots from Table 1: Cumulative Number of Cases Tested Positive for COVID-19 
- as reported from dates 07/03/20 to 22/07/20 on SG website"""


class CumulativeCases(object):

    def __init__(self):
        self.create_plots()

    def create_plots(self):
        cumulative_cases = pd.read_csv("../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv")
        boards = cumulative_cases.columns.tolist()
        dates = cumulative_cases["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(5, 3, i)
            ax = sns.lineplot(data=cumulative_cases, x="Date", y=board)
            ax.set_title(board)
            x_values = dates[::7]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_yticks([y * 2000 for y in range(1, 10)])
            ax.set_ylabel("Cumulative Cases")
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle("The cumulative number of cases with positive tests for COVID-19, by board in Scotland")
        plt.show()