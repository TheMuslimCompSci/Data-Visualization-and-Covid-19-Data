import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from src.main.plots import Plots


"""DataByBoardPlots is one of 3 child classes of Plots. It builds and displays the visualizations for each dataset.
"""


class DataByBoardPlots(Plots):

    def __init__(self, plots_path=None, plots_title=None, plots_ylabel=None, plots_yticks=None, plots_types_list=None,
                 plots_axis_column_index=None):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks
        self.plots_types_list = plots_types_list
        self.plots_axis_column_index = plots_axis_column_index

    # Get iterable with information for each plot: file path, title, y axis label and ticks, available types and the
    # column in dataset with the plot data.
    @staticmethod
    def get_plots_info():
        plots_info = {
            "Cumulative Cases": ["../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv",
                                 "The cumulative number of cases with positive tests for COVID-19, by board in Scotland, 07/03/2020-22/07/2020",
                                 "Cumulative Cases", [y * 2000 for y in range(1, 10)],
                                 ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "ICU Patients Confirmed": ["../COVID-19 data by NHS Board 22 July 2020/Table 2a - ICU patients.csv",
                                       "The daily number of COVID-19 inpatients (confirmed) in ICU at midnight, by board in Scotland, 26/03/2020-22/07/2020",
                                       "ICU Patients", [y * 20 for y in range(1, 12)],
                                       ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "ICU Patients Suspected": ["../COVID-19 data by NHS Board 22 July 2020/Table 2b - ICU patients (Hist.).csv",
                                       "The daily number of COVID-19 inpatients (suspected) in ICU at midnight, by board in Scotland, 18/03/2020-21/07/2020",
                                       "ICU Patients", [y * 20 for y in range(1, 12)],
                                       ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "Hospital Confirmed": ["../COVID-19 data by NHS Board 22 July 2020/Table 3a - Hospital Confirmed.csv",
                                   "The daily number of confirmed COVID-19 inpatients in hospital at midnight, by board in Scotland, 26/03/2020-22/07/2020",
                                   "Hospital Patients", [y * 200 for y in range(1, 9)],
                                   ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "Hospital Suspected": ["../COVID-19 data by NHS Board 22 July 2020/Table 3b- Hospital Suspected.csv",
                                   "The daily number of suspected COVID-19 inpatients in hospital at midnight, by board in Scotland, 26/03/2020-21/07/2020",
                                   "Hospital Patients", [y * 50 for y in range(1, 11)],
                                   ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"]
        }
        return plots_info

    # Build the visualization and display it on screen.
    def create_visualization(self, plots_type, plots_style, plots_context, plots_palette):
        # Configure plots style, context, palette and size
        self.set_plots_styling(plots_style, plots_context, plots_palette)
        f, ax = plt.subplots(figsize=(25, 15))
        plots_data = pd.read_csv(self.plots_path)
        boards = plots_data.columns.tolist()
        dates = plots_data["Date"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        # Implementation of pie chart.
        if plots_type == "pie":
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
                if plots_type == "default":
                    if self.plots_ylabel == "Cumulative Cases":
                        # Implementation of line plot.
                        ax = sns.lineplot(data=plots_data, x="Date", y=board)
                    else:
                        # Implementation of bar plot.
                        ax = sns.barplot(data=plots_data, x="Date", y=board)
                    ax.axes.xaxis.set_ticklabels([])
                    ax.set_ylabel(self.plots_ylabel)
                elif plots_type == "kde" or plots_type == "histogram":
                    if plots_type == "kde":
                        # Implementation of KDE plot.
                        ax = sns.kdeplot(data=plots_data[board], shade=True)
                    elif plots_type == "histogram":
                        # Implementation of histogram.
                        ax = sns.histplot(data=plots_data[board])
                    ax.set_xlabel(self.plots_ylabel)
                else:
                    if plots_type == "box":
                        # Implementation of box plot.
                        ax = sns.boxplot(data=plots_data[board])
                    elif plots_type == "violin":
                        # Implementation of violin plot.
                        ax = sns.violinplot(data=plots_data[board])
                    ax.axes.xaxis.set_ticks([])
                    ax.set_ylabel(self.plots_ylabel)
                ax.set_title(board)
            plt.subplots_adjust(wspace=1, hspace=1)
            f.suptitle(self.plots_title)
        plt.show()
