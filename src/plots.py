import pandas as pd
from plots_statistics import PlotsStatistics


class Plots(object):

    def __init__(self, plots_path, plots_title, plots_types_list, plots_axis_column_index, plots_ylabel):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_types_list = plots_types_list
        self.plots_axis_column_index = plots_axis_column_index
        self.plots_ylabel = plots_ylabel

    def get_plots_data(self):
        plots_data = pd.read_csv(self.plots_path)
        return plots_data

    def get_plots_title(self):
        return self.plots_title

    def get_plots_types_list(self):
        return self.plots_types_list

    def get_plots_axis_column_index(self):
        plots_data = pd.read_csv(self.plots_path)
        return plots_data.columns.get_loc(self.plots_axis_column_index)

    def get_plots_statistics(self):
        plots_data = self.get_plots_data()
        plot_axis_column_index = self.get_plots_axis_column_index()
        plots_statistics = PlotsStatistics(plots_data, plot_axis_column_index, self.plots_ylabel)
        return plots_statistics.get_plots_statistics()
