import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class DeathsDataPlots(object):

    def __init__(self, plots_path, plots_title, plots_ylabel, plots_yticks):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks

    def create_plots(self):
        plots_data = pd.read_csv(self.plots_path)
        boards = plots_data.columns.tolist()
        dates = plots_data["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            ax = sns.lineplot(data=plots_data, x="Date", y=board)
            ax.set_title(board)
            x_values = dates[::7]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_yticks(self.plots_yticks)
            ax.set_ylabel(self.plots_ylabel)
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle(self.plots_title)
        plt.show()
