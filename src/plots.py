import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from plots_statistics import PlotsStatistics


class Plots(object):

    def __init__(self, plots_path, plots_title, plots_types_list, plots_axis_column_index, plots_ylabel):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_types_list = plots_types_list
        self.plots_axis_column_index = plots_axis_column_index
        self.plots_ylabel = plots_ylabel

    @staticmethod
    def set_plots_styling(plots_style, plots_context, plots_palette):
        plt.close("all")
        sns.set_style(plots_style)
        sns.set_context(plots_context)
        sns.set_palette(plots_palette)

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

    @staticmethod
    def get_plots_contexts_list():
        PLOTS_CONTEXTS = [
            ("default", "notebook"),
            ("paper", "paper"),
            ("talk", "talk"),
            ("poster", "poster"),
        ]
        return PLOTS_CONTEXTS

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
