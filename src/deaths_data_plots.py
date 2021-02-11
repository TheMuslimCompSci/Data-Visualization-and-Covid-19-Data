import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


class DeathsDataPlots(object):

    def __init__(self, plot_path=None, plot_title=None, plot_ylabel=None, plot_yticks=None, plot_y_values=None):
        self.plot_path = plot_path
        self.plot_title = plot_title
        self.plot_ylabel = plot_ylabel
        self.plot_yticks = plot_yticks
        self.plot_y_values = plot_y_values

    def get_plots_info(self):
        plots_info = {
            "Cumulative Deaths": ["../covid deaths data week 30/Figure 1 data.csv",
                                  "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
                                  "Cumulative number of deaths", [y * 500 for y in range(1, 10)], "Count"],

            "Cumulative Deaths Different Data": ["../covid deaths data week 30/Figure 2 data.csv",
                                                 "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
                                                 "Cumulative number of deaths", [y * 500 for y in range(1, 10)], "Cumulative Count"],

            "COVID Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                    "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                    "Number of deaths", [y * 200 for y in range(1, 11)], "Covid deaths to date"],

            "All Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                  "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                  "Number of deaths", [y * 2000 for y in range(1, 8)], "Total deaths to date"],

            "Deaths By Board": ["../covid deaths data week 30/Figure 4 data.csv",
                                "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
                                "Number of deaths", [y * 200 for y in range(1, 8)], "COVID-19 deaths to date"],

            "Deaths By Week": ["../covid deaths data week 30/Figure 5 data.csv",
                               "Deaths by week of registration, Scotland, 2020",
                               "Number of deaths", [y * 500 for y in range(1, 6)], ["Total deaths 2020", "Average for previous 5 years", "COVID-19 deaths 2020"]],

            "Deaths By Cause": ["../covid deaths data week 30/Figure 6 data.csv",
                                "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                "Number of deaths", [y * 5000 for y in range(1, 6)], ""],

            "Deaths By Location": ["../covid deaths data week 30/Figure 7 data.csv",
                                   "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
                                   "Number of deaths", [y * 50 for y in range(1, 9)], ""],

            "Deaths By Date Of Death vs Date Of Registration": ["../covid deaths data week 30/Figure 8 data.csv",
                                                                "Deaths involving COVID-19, date of death vs date of registration",
                                                                "Cumulative number of deaths", [y * 500 for y in range(1, 10)], ["Cumulative deaths by date of death", "Cumulative deaths by date of registration"]]
        }
        return plots_info

    def create_visualization(self, plot_type):
        plt.close("all")
        plot_data = pd.read_csv(self.plot_path)
        plot_titles = self.get_plots_info()
        if self.plot_title == plot_titles["Deaths By Cause"][1]:
            plot = self.create_death_by_cause_plot(plot_data, plot_type)
        else:
            if self.plot_ylabel == "Cumulative number of deaths":
                if self.plot_title == plot_titles["Cumulative Deaths"][1]:
                    plot = self.create_cumulative_deaths_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plot_title == plot_titles["Cumulative Deaths Different Data"][1]:
                    plot = self.create_cumulative_deaths_different_data_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plot_title == plot_titles["Deaths By Date Of Death vs Date Of Registration"][1]:
                    plot = self.create_deaths_by_dates_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                weekly_dates = dates[::7]
                if plot_type == "default":
                    ax.set_xticks(weekly_dates)
                    ax.set_xticklabels(weekly_dates, rotation="vertical")
            elif self.plot_ylabel == "Number of deaths":
                if self.plot_title == plot_titles["COVID Deaths By Age"][1] or self.plot_title == plot_titles["All Deaths By Age"][1]:
                    ax = self.create_deaths_by_age_plot(plot_data, plot_type)
                elif self.plot_title == plot_titles["Deaths By Board"][1]:
                    ax = self.create_deaths_by_board_plot(plot_data, plot_type)
                elif self.plot_title == plot_titles["Deaths By Week"][1]:
                    ax = self.create_death_by_week_plot(plot_data, plot_type)
                elif self.plot_title == plot_titles["Deaths By Location"][1]:
                    ax = self.create_death_by_location_plot(plot_data, plot_type)
            ax.set_yticks(self.plot_yticks)
            ax.set_ylabel(self.plot_ylabel)
            ax.set_title(self.plot_title)
            sns.despine(top=True, right=True)
        plt.show()

    def create_cumulative_deaths_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        if plot_type == "default":
            ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values)
        elif plot_type == "kde":
            ax = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.violinplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        plot = [ax, dates]
        return plot

    def create_cumulative_deaths_different_data_plot(self, plot_data, plot_type):
        hps_source_data = plot_data.iloc[:int(len(plot_data) / 2)]
        nrs_source_data = plot_data.iloc[int(len(plot_data) / 2):]
        dates = hps_source_data["Date"].tolist()
        if plot_type == "default":
            ax = sns.lineplot(data=hps_source_data, x="Date", y=self.plot_y_values)
            ax = sns.lineplot(data=nrs_source_data, x="Date", y=self.plot_y_values)
        elif plot_type == "kde":
            ax = sns.kdeplot(data=hps_source_data[self.plot_y_values], shade=True)
            ax = sns.kdeplot(data=nrs_source_data[self.plot_y_values], shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=hps_source_data[self.plot_y_values])
            ax = sns.boxplot(data=nrs_source_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.boxplot(data=hps_source_data[self.plot_y_values])
            ax = sns.boxplot(data=nrs_source_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        ax.legend(["HPS", "NRS"])
        plot = [ax, dates]
        return plot

    def create_deaths_by_age_plot(self, plot_data, plot_type):
        if plot_type == "default":
            plot = sns.barplot(data=plot_data, x="Age group", y=self.plot_y_values)
        elif plot_type == "kde":
            ax = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.violinplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        return plot

    def create_deaths_by_board_plot(self, plot_data, plot_type):
        if plot_type == "default":
            plot = sns.barplot(data=plot_data, x="Health board", y=self.plot_y_values)
            health_boards = plot_data["Health board"].tolist()
            plot.set_xticks(range(len(health_boards)))
            plot.set_xticklabels(health_boards, rotation="45")
        elif plot_type == "kde":
            ax = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.violinplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        return plot

    def create_death_by_week_plot(self, plot_data, plot_type):
        week_numbers = plot_data["Week number"].tolist()
        if plot_type == "default":
            plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[0])
            plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[1])
            plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[2])
            plot.set_xticks(range(len(week_numbers)))
            plot.set_xticklabels(week_numbers, rotation="vertical")
        elif plot_type == "kde":
            ax = sns.kdeplot(data=plot_data[self.plot_y_values[0]], shade=True)
            ax = sns.kdeplot(data=plot_data[self.plot_y_values[1]], shade=True)
            ax = sns.kdeplot(data=plot_data[self.plot_y_values[2]], shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=plot_data[self.plot_y_values[0]])
            ax = sns.boxplot(data=plot_data[self.plot_y_values[1]])
            ax = sns.boxplot(data=plot_data[self.plot_y_values[2]])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.violinplot(data=plot_data[self.plot_y_values[0]])
            ax = sns.violinplot(data=plot_data[self.plot_y_values[1]])
            ax = sns.violinplot(data=plot_data[self.plot_y_values[2]])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        plot.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
        return plot

    def create_death_by_cause_plot(self, plot_data, plot_type):
        plot_values = self.format_death_by_cause_data(plot_data, plot_type)
        registered_deaths_2020_list = plot_values[0]
        registered_deaths_five_year_avg_list = plot_values[1]
        location_of_death_list = plot_values[2]
        cause_of_death_list = plot_values[3]
        plot = self.format_death_by_cause_plot(1, registered_deaths_2020_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, week 12 to 30, 2020")
        plot = self.format_death_by_cause_plot(2, registered_deaths_five_year_avg_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, five year average")
        plt.subplots_adjust(wspace=1, hspace=1)
        return plot

    def format_death_by_cause_data(self, plot_data, plot_type):
        cause_of_death_column = plot_data["Location of death"]
        cause_of_death_column = cause_of_death_column.iloc[6:13]
        cause_of_death_column_list = cause_of_death_column.tolist()
        cause_of_death_list = []
        for cause in cause_of_death_column_list:
            cause_of_death_list.append([cause] * 4)
        cause_of_death_list = [item for sublist in cause_of_death_list for item in sublist]
        location_of_death_data = plot_data.drop(columns=["Location of death"])
        location_of_death_columns = location_of_death_data.columns.tolist()
        location_of_death_list = location_of_death_columns * 7
        registered_deaths_five_year_avg_covid_19_row = pd.DataFrame([[0, 0, 0, 0]], columns=location_of_death_columns)
        registered_deaths_five_year_avg_data = location_of_death_data.iloc[0:6]
        registered_deaths_five_year_avg_data = registered_deaths_five_year_avg_data.append(registered_deaths_five_year_avg_covid_19_row, ignore_index=True)
        registered_deaths_five_year_avg_list = registered_deaths_five_year_avg_data.values.tolist()
        registered_deaths_five_year_avg_list = [item for sublist in registered_deaths_five_year_avg_list for item in sublist]
        registered_deaths_2020_data = location_of_death_data.iloc[6:13]
        registered_deaths_2020_list = registered_deaths_2020_data.values.tolist()
        registered_deaths_2020_list = [item for sublist in registered_deaths_2020_list for item in sublist]
        plot_values = [registered_deaths_2020_list, registered_deaths_five_year_avg_list, location_of_death_list, cause_of_death_list]
        return plot_values

    def format_death_by_cause_plot(self, subplot_index, plot_x_values, plot_y_values, plot_hue, plot_title, plot_type):
        plt.subplot(1, 2, subplot_index)
        if plot_type == "default":
            ax = sns.barplot(x=plot_x_values, y=plot_y_values, hue=plot_hue)
        ax.set_title(plot_title)
        x_values = [y * 500 for y in range(1, 21)]
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_xlabel("Number of deaths")
        sns.despine(top=True, right=True)
        return ax

    def create_death_by_location_plot(self, plot_data, plot_type):
        week_numbers = plot_data.columns.tolist()
        week_numbers = week_numbers[1:]
        care_home_deaths = plot_data.loc[0].values.tolist()
        care_home_deaths = care_home_deaths[1:]
        home_deaths = plot_data.loc[1].values.tolist()
        home_deaths = home_deaths[1:]
        hospital_deaths = plot_data.loc[2].values.tolist()
        hospital_deaths = hospital_deaths[1:]
        if plot_type == "default":
            plot = sns.lineplot(x=week_numbers, y=care_home_deaths)
            plot = sns.lineplot(x=week_numbers, y=home_deaths)
            plot = sns.lineplot(x=week_numbers, y=hospital_deaths)
            plot.set_xticks(range(len(week_numbers)))
            plot.set_xticklabels(week_numbers, rotation="vertical")
        elif plot_type == "kde":
            ax = sns.kdeplot(data=care_home_deaths, shade=True)
            ax = sns.kdeplot(data=home_deaths, shade=True)
            ax = sns.kdeplot(data=hospital_deaths, shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=care_home_deaths)
            ax = sns.boxplot(data=home_deaths)
            ax = sns.boxplot(data=hospital_deaths)
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.violinplot(data=care_home_deaths)
            ax = sns.violinplot(data=home_deaths)
            ax = sns.violinplot(data=hospital_deaths)
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        plot.legend(["Care Home", "Home / Non-institution", "Hospital"])
        return plot

    def create_deaths_by_dates_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        if plot_type == "default":
            ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[0])
            ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[1])
        elif plot_type == "kde":
            ax = sns.kdeplot(data=plot_data[self.plot_y_values[0]], shade=True)
            ax = sns.kdeplot(data=plot_data[self.plot_y_values[1]], shade=True)
        elif plot_type == "box":
            ax = sns.boxplot(data=plot_data[self.plot_y_values[0]])
            ax = sns.boxplot(data=plot_data[self.plot_y_values[1]])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        elif plot_type == "violin":
            ax = sns.violinplot(data=plot_data[self.plot_y_values[0]])
            ax = sns.violinplot(data=plot_data[self.plot_y_values[1]])
            ax.axes.xaxis.set_ticks([])
            ax.set_xlabel(self.plot_ylabel)
        ax.legend(self.plot_y_values)
        ax.xaxis.grid(True)
        plot = [ax, dates]
        return plot

    def get_plots_title(self):
        return self.plot_title

    def get_plots_data(self):
        plots_data = pd.read_csv(self.plot_path)
        return plots_data

    def get_plots_axis_column_index(self):
        plots_data = pd.read_csv(self.plot_path)
        plots_info = self.get_plots_info()
        if self.plot_path == plots_info["Cumulative Deaths"][0]:
            return plots_data.columns.get_loc("Count")
        elif self.plot_path == plots_info["Cumulative Deaths Different Data"][0]:
            return plots_data.columns.get_loc("Cumulative Count")
        elif self.plot_path == plots_info["COVID Deaths By Age"][0]:
            if self.plot_y_values == plots_info["COVID Deaths By Age"][4]:
                return plots_data.columns.get_loc("Covid deaths to date")
            elif self.plot_y_values == plots_info["All Deaths By Age"][4]:
                return plots_data.columns.get_loc("Total deaths to date")
        elif self.plot_path == plots_info["Deaths By Board"][0]:
            return plots_data.columns.get_loc("COVID-19 deaths to date")
        elif self.plot_path == plots_info["Deaths By Week"][0]:
            return plots_data.columns.get_loc("COVID-19 deaths 2020")
        elif self.plot_path == plots_info["Deaths By Cause"][0]:
            return plots_data.columns.get_loc("Hospital")
        elif self.plot_path == plots_info["Deaths By Location"][0]:
            return plots_data.columns.get_loc("week 30")
        elif self.plot_path == plots_info["Deaths By Date Of Death vs Date Of Registration"][0]:
            return plots_data.columns.get_loc("Cumulative deaths by date of registration")

    def get_plots_statistics(self):
        plots_data = self.get_plots_data()
        plot_axis_column_index = self.get_plots_axis_column_index()
        plot_axis_column = plots_data.iloc[:, plot_axis_column_index].tolist()
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
