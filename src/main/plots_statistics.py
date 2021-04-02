import sys
sys.path.append(".")

import numpy as np

"""PlotsStatistics is a small utility class with a static method to calculate numerous statistical metrics for a given 
plot dataset.
"""


class PlotsStatistics(object):

    def __init__(self, plot_data, plot_axis_column_index, plot_ylabel):
        self.plot_data = plot_data
        self.plot_axis_column_index = plot_axis_column_index
        self.plot_ylabel = plot_ylabel

    # Calculate an array of 6 different statistics for a plot dataset: minimum, maximum, median, mean, standard
    # deviation and variance
    def get_plots_statistics(self):
        # get column with plot data from dataset
        plot_axis_column = self.plot_data.iloc[:, self.plot_axis_column_index].tolist()
        plots_statistics = []
        # calculate each statistic and add it to list of statistics in the right format
        min_value = np.nanmin(plot_axis_column)
        plots_statistics.append("Minimum value of " + self.plot_ylabel + ": " + str(min_value))
        max_value = np.nanmax(plot_axis_column)
        plots_statistics.append("Maximum value of " + self.plot_ylabel + ": " + str(max_value))
        median_value = np.nanmedian(plot_axis_column)
        plots_statistics.append("Median value of " + self.plot_ylabel + ": " + str(median_value))
        mean_value = np.nanmean(plot_axis_column)
        plots_statistics.append("Mean value of " + self.plot_ylabel + ": " + str(mean_value))
        standard_deviation_value = np.nanstd(plot_axis_column)
        plots_statistics.append(
            "Standard Deviation value of " + self.plot_ylabel + ": " + str(standard_deviation_value))
        variance_value = np.nanvar(plot_axis_column)
        plots_statistics.append("Variance value of " + self.plot_ylabel + ": " + str(variance_value))
        return plots_statistics
