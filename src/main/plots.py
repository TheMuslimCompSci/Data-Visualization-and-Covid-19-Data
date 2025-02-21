import sys
sys.path.append(".")

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from plots_statistics import PlotsStatistics


"""Plots is the parent class of the 3 plots classes with static methods to set the styling of plots and accessor methods
to get various plot parameters. 
"""


class Plots(object):

    def __init__(self, plots_path, plots_title, plots_types_list, plots_axis_column_index, plots_ylabel):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_types_list = plots_types_list
        self.plots_axis_column_index = plots_axis_column_index
        self.plots_ylabel = plots_ylabel

    # Get DataFrame from plots dataset.
    def get_plots_data(self):
        plots_data = pd.read_csv(self.plots_path)
        return plots_data

    # Get plots title.
    def get_plots_title(self):
        return self.plots_title

    # Get all plots types for a dataset.
    def get_plots_types_list(self):
        return self.plots_types_list

    # Get column with plots data from dataset.
    def get_plots_axis_column_index(self):
        plots_data = pd.read_csv(self.plots_path)
        return plots_data.columns.get_loc(self.plots_axis_column_index)

    # Get statistics for plots data.
    def get_plots_statistics(self):
        plots_data = self.get_plots_data()
        plot_axis_column_index = self.get_plots_axis_column_index()
        plots_statistics = PlotsStatistics(plots_data, plot_axis_column_index, self.plots_ylabel)
        return plots_statistics.get_plots_statistics()

    # Set style, context and palette for plots.
    @staticmethod
    def set_plots_styling(plots_style, plots_context, plots_palette):
        plt.close("all")
        sns.set_style(plots_style)
        sns.set_context(plots_context)
        sns.set_palette(plots_palette)

    # Get all plots styles.
    @staticmethod
    def get_plots_styles_list():
        PLOTS_STYLES = [
            ("default", "None"),
            ("dark grid", "darkgrid"),
            ("white grid", "whitegrid"),
            ("dark", "dark"),
            ("white", "white"),
            ("ticks", "ticks")
        ]
        return PLOTS_STYLES

    # Get all plots contexts.
    @staticmethod
    def get_plots_contexts_list():
        PLOTS_CONTEXTS = [
            ("default", "notebook"),
            ("paper", "paper"),
            ("talk", "talk"),
            ("poster", "poster"),
        ]
        return PLOTS_CONTEXTS

    # Get all plots palettes.
    @staticmethod
    def get_plots_palettes_list():
        PLOTS_PALETTES = [
            ("default", "None"),
            ("deep", "deep"),
            ("muted", "muted"),
            ("pastel", "pastel"),
            ("bright", "bright"),
            ("dark", "dark"),
            ("colour blind", "colorblind"),
        ]
        return PLOTS_PALETTES
