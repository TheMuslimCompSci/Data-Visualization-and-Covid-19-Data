import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class DataByBoardPlots(object):

    def __init__(self, plots_path=None, plots_title=None, plots_ylabel=None, plots_yticks=None):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks

    def get_plots_info(self):
        plots_info = {
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
        return plots_info

    def create_visualization(self):
        plots_data = pd.read_csv(self.plots_path)
        boards = plots_data.columns.tolist()
        dates = plots_data["Date"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            if self.plots_ylabel == "Cumulative Cases":
                ax = sns.lineplot(data=plots_data, x="Date", y=board)
            else:
                ax = sns.barplot(data=plots_data, x="Date", y=board)
            ax.set_xticks(range(len(weekly_dates)))
            ax.set_title(board)
            ax.set_xticklabels(weekly_dates, rotation="vertical")
            ax.set_yticks(self.plots_yticks)
            ax.set_ylabel(self.plots_ylabel)
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle(self.plots_title)
        plt.show()
