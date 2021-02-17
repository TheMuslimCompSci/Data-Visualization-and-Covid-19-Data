import numpy as np


class PlotStatistics(object):

    def __init__(self, plot_data, plot_axis_column_index, plot_ylabel):
        self.plot_data = plot_data
        self.plot_axis_column_index = plot_axis_column_index
        self.plot_ylabel = plot_ylabel

    def get_plots_statistics(self):
        plot_axis_column = self.plot_data.iloc[:, self.plot_axis_column_index].tolist()
        plots_statistics = []
        min_value = np.nanmin(plot_axis_column)
        plots_statistics.append("Minimum value of " + self.plot_ylabel + ": " + str(min_value))
        max_value = np.nanmax(plot_axis_column)
        plots_statistics.append("Maximum value of " + self.plot_ylabel + ": " + str(max_value))
        median_value = np.nanmedian(plot_axis_column)
        plots_statistics.append("Median value of " + self.plot_ylabel + ": " + str(median_value))
        mean_value = np.nanmean(plot_axis_column)
        plots_statistics.append("Mean value of " + self.plot_ylabel + ": " + str(mean_value))
        standard_deviation_value = np.nanstd(plot_axis_column)
        plots_statistics.append("Standard Deviation value of " + self.plot_ylabel + ": " + str(standard_deviation_value))
        variance_value = np.nanvar(plot_axis_column)
        plots_statistics.append("Variance value of " + self.plot_ylabel + ": " + str(variance_value))
        return plots_statistics
