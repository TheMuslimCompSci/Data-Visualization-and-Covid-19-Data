import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


class DataByBoardPlots(object):

    def __init__(self, plots_path=None, plots_title=None, plots_ylabel=None, plots_yticks=None, plots_types_list=None):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks
        self.plots_types_list = plots_types_list

    def get_plots_info(self):
        plots_info = {
            "Cumulative Cases": ["../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv",
                                 "The cumulative number of cases with positive tests for COVID-19, by board in Scotland, 07/03/2020-22/07/2020",
                                 "Cumulative Cases", [y * 2000 for y in range(1, 10)], ["default", "kde", "box", "violin", "histogram", "pie"]],

            "ICU Patients Confirmed": ["../COVID-19 data by NHS Board 22 July 2020/Table 2a - ICU patients.csv",
                                       "The daily number of COVID-19 inpatients (confirmed) in ICU at midnight, by board in Scotland, 26/03/2020-22/07/2020",
                                       "ICU Patients", [y * 20 for y in range(1, 12)], ["default", "kde", "box", "violin", "histogram", "pie"]],

            "ICU Patients Suspected": ["../COVID-19 data by NHS Board 22 July 2020/Table 2b - ICU patients (Hist.).csv",
                                       "The daily number of COVID-19 inpatients (suspected) in ICU at midnight, by board in Scotland, 18/03/2020-21/07/2020",
                                       "ICU Patients", [y * 20 for y in range(1, 12)], ["default", "kde", "box", "violin", "histogram", "pie"]],

            "Hospital Confirmed": ["../COVID-19 data by NHS Board 22 July 2020/Table 3a - Hospital Confirmed.csv",
                                   "The daily number of confirmed COVID-19 inpatients in hospital at midnight, by board in Scotland, 26/03/2020-22/07/2020",
                                   "Hospital Patients", [y * 200 for y in range(1, 9)], ["default", "kde", "box", "violin", "histogram", "pie"]],

            "Hospital Suspected": ["../COVID-19 data by NHS Board 22 July 2020/Table 3b- Hospital Suspected.csv",
                                   "The daily number of suspected COVID-19 inpatients in hospital at midnight, by board in Scotland, 26/03/2020-21/07/2020",
                                   "Hospital Patients", [y * 50 for y in range(1, 11)], ["default", "kde", "box", "violin", "histogram", "pie"]]
        }
        return plots_info

    def create_visualization(self, plot_type):
        plots_data = pd.read_csv(self.plots_path)
        boards = plots_data.columns.tolist()
        dates = plots_data["Date"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        f, ax = plt.subplots(figsize=(25, 15))
        if plot_type == "pie":
            board_totals = []
            for i in range(1, len(boards) - 1):
                board = boards[i]
                if self.plots_ylabel == "Cumulative Cases":
                    board_total = plots_data[board].iloc[-1]
                else:
                    board_total = plots_data[board].sum()
                board_totals.append(board_total)
            plt.pie(x=board_totals, labels=boards[1:len(boards) - 1], autopct="%1d%%")
            plt.axis("equal")
            plt.title(self.plots_title)
        else:
            for i in range(1, len(boards)):
                board = boards[i]
                plt.subplot(4, 4, i)
                if plot_type == "default":
                    if self.plots_ylabel == "Cumulative Cases":
                        ax = sns.lineplot(data=plots_data, x="Date", y=board)
                    else:
                        ax = sns.barplot(data=plots_data, x="Date", y=board)
                    ax.axes.xaxis.set_ticklabels([])
                    ax.set_ylabel(self.plots_ylabel)
                elif plot_type == "kde" or plot_type == "histogram":
                    if plot_type == "kde":
                        ax = sns.kdeplot(data=plots_data[board], shade=True)
                    elif plot_type == "histogram":
                        ax = sns.histplot(data=plots_data[board])
                    ax.set_xlabel(self.plots_ylabel)
                else:
                    if plot_type == "box":
                        ax = sns.boxplot(data=plots_data[board])
                    elif plot_type == "violin":
                        ax = sns.violinplot(data=plots_data[board])
                    ax.axes.xaxis.set_ticks([])
                    ax.set_ylabel(self.plots_ylabel)
                ax.set_title(board)
            plt.subplots_adjust(wspace=1, hspace=1)
            f.suptitle(self.plots_title)
        plt.show()

    def get_plots_title(self):
        return self.plots_title

    def get_plots_types_list(self):
        return self.plot_types_list

    def get_plots_data(self):
        plots_data = pd.read_csv(self.plots_path)
        return plots_data

    def get_plots_axis_column_index(self):
        plots_data = self.get_plots_data()
        return plots_data.columns.get_loc("Scotland")

    def get_plots_statistics(self):
        plots_data = self.get_plots_data()
        plot_axis_column_index = self.get_plots_axis_column_index()
        plot_axis_column = plots_data.iloc[:, plot_axis_column_index].tolist()
        plots_statistics = []
        min_value = np.nanmin(plot_axis_column)
        plots_statistics.append("Minimum value of " + self.plots_ylabel + ": " + str(min_value))
        max_value = np.nanmax(plot_axis_column)
        plots_statistics.append("Maximum value of " + self.plots_ylabel + ": " + str(max_value))
        median_value = np.nanmedian(plot_axis_column)
        plots_statistics.append("Median value of " + self.plots_ylabel + ": " + str(median_value))
        mean_value = np.nanmean(plot_axis_column)
        plots_statistics.append("Mean value of " + self.plots_ylabel + ": " + str(mean_value))
        standard_deviation_value = np.nanstd(plot_axis_column)
        plots_statistics.append("Standard Deviation value of " + self.plots_ylabel + ": " + str(standard_deviation_value))
        variance_value = np.nanvar(plot_axis_column)
        plots_statistics.append("Variance value of " + self.plots_ylabel + ": " + str(variance_value))
        return plots_statistics
