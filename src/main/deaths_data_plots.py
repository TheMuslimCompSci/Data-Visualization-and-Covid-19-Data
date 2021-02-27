import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from plots import Plots

"""DeathsDataPlots is one of 3 child classes of Plots. It builds and displays the visualizations for each dataset.
"""


class DeathsDataPlots(Plots):

    def __init__(self, plots_path=None, plots_title=None, plots_ylabel=None, plots_yticks=None, plots_y_values=None,
                 plots_types_list=None, plots_axis_column_index=None):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks
        self.plots_y_values = plots_y_values
        self.plots_types_list = plots_types_list
        self.plots_axis_column_index = plots_axis_column_index

    # Get iterable with information for each plot: file path, title, y axis label, ticks and values, available types and
    # the column in dataset with the plot data.
    @staticmethod
    def get_plots_info():
        plots_info = {
            "Cumulative Deaths": ["../covid deaths data week 30/Figure 1 data.csv",
                                  "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
                                  "Cumulative number of deaths", [y * 500 for y in range(1, 10)], "Count",
                                  ["default", "kde", "box", "violin", "histogram"], "Count"],

            "Cumulative Deaths Different Data": ["../covid deaths data week 30/Figure 2 data.csv",
                                                 "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
                                                 "Cumulative number of deaths", [y * 500 for y in range(1, 10)],
                                                 "Cumulative Count",
                                                 ["default", "kde", "box", "violin", "histogram"], "Cumulative Count"],

            "COVID Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                    "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                    "Number of deaths", [y * 200 for y in range(1, 11)], "Covid deaths to date",
                                    ["default", "kde", "box", "violin", "histogram", "pie"], "Covid deaths to date"],

            "All Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                  "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                  "Number of deaths", [y * 2000 for y in range(1, 8)], "Total deaths to date",
                                  ["default", "kde", "box", "violin", "histogram", "pie"], "Total deaths to date"],

            "Deaths By Board": ["../covid deaths data week 30/Figure 4 data.csv",
                                "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
                                "Number of deaths", [y * 200 for y in range(1, 8)], "COVID-19 deaths to date",
                                ["default", "kde", "box", "violin", "histogram", "pie"], "COVID-19 deaths to date"],

            "Deaths By Week": ["../covid deaths data week 30/Figure 5 data.csv",
                               "Deaths by week of registration, Scotland, 2020",
                               "Number of deaths", [y * 500 for y in range(1, 6)],
                               ["Total deaths 2020", "Average for previous 5 years", "COVID-19 deaths 2020"],
                               ["default", "kde", "box", "violin", "histogram"], "COVID-19 deaths 2020"],

            "Deaths By Cause": ["../covid deaths data week 30/Figure 6 data.csv",
                                "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                "Number of deaths", [y * 5000 for y in range(1, 6)], "",
                                ["default", "pie"], "Hospital"],

            "Deaths By Location": ["../covid deaths data week 30/Figure 7 data.csv",
                                   "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
                                   "Number of deaths", [y * 50 for y in range(1, 9)], "",
                                   ["default", "kde", "box", "violin", "histogram", "pie"], "week 30"],

            "Deaths By Date Of Death vs Date Of Registration": ["../covid deaths data week 30/Figure 8 data.csv",
                                                                "Deaths involving COVID-19, date of death vs date of registration",
                                                                "Cumulative number of deaths",
                                                                [y * 500 for y in range(1, 10)],
                                                                ["Cumulative deaths by date of death",
                                                                 "Cumulative deaths by date of registration"],
                                                                ["default", "kde", "box", "violin", "histogram"],
                                                                "Cumulative deaths by date of registration"]
        }
        return plots_info

    # Build the visualization and display it on screen.
    def create_visualization(self, plots_type, plots_style, plots_context, plots_palette):
        self.set_plots_styling(plots_style, plots_context, plots_palette)
        plots_data = pd.read_csv(self.plots_path)
        plots_titles = self.get_plots_info()
        # Initialize plots variables.
        ax = None
        dates = None
        plot = None
        # Invoke plotting method corresponding to given plot information.
        if self.plots_title == plots_titles["Deaths By Cause"][1]:
            plot = self.create_deaths_by_cause_plot(plots_data, plots_type)
        else:
            if self.plots_ylabel == "Cumulative number of deaths":
                if self.plots_title == plots_titles["Cumulative Deaths"][1]:
                    plot = self.create_cumulative_deaths_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plots_title == plots_titles["Cumulative Deaths Different Data"][1]:
                    plot = self.create_cumulative_deaths_different_data_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plots_title == plots_titles["Deaths By Date Of Death vs Date Of Registration"][1]:
                    plot = self.create_deaths_by_dates_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                weekly_dates = dates[::7]
                if plots_type == "default":
                    ax.set_xticks(weekly_dates)
                    ax.set_xticklabels(weekly_dates, rotation="vertical")
            elif self.plots_ylabel == "Number of deaths":
                if self.plots_title == plots_titles["COVID Deaths By Age"][1] \
                        or self.plots_title == plots_titles["All Deaths By Age"][1]:
                    ax = self.create_deaths_by_age_plot(plots_data, plots_type)
                elif self.plots_title == plots_titles["Deaths By Board"][1]:
                    ax = self.create_deaths_by_board_plot(plots_data, plots_type)
                elif self.plots_title == plots_titles["Deaths By Week"][1]:
                    ax = self.create_deaths_by_week_plot(plots_data, plots_type)
                elif self.plots_title == plots_titles["Deaths By Location"][1]:
                    ax = self.create_deaths_by_location_plot(plots_data, plots_type)
            if plots_type == "default":
                ax.set_yticks(self.plots_yticks)
                ax.set_ylabel(self.plots_ylabel)
            plt.title(self.plots_title)
            sns.despine(top=True, right=True)
        plt.show()

    # Build visualization for Cumulative Deaths dataset.
    def create_cumulative_deaths_plot(self, plots_data, plots_type):
        dates = plots_data["Date"].tolist()
        ax = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            ax = sns.lineplot(data=plots_data, x="Date", y=self.plots_y_values)
        elif plots_type == "kde" or plots_type == "histogram":
            if plots_type == "kde":
                ax = sns.kdeplot(data=plots_data[self.plots_y_values], shade=True)
            elif plots_type == "histogram":
                ax = sns.histplot(data=plots_data[self.plots_y_values])
            ax.set_xlabel(self.plots_ylabel)
        else:
            if plots_type == "box":
                ax = sns.boxplot(data=plots_data[self.plots_y_values])
            elif plots_type == "violin":
                ax = sns.violinplot(data=plots_data[self.plots_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_ylabel(self.plots_ylabel)
        plot = [ax, dates]
        return plot

    # Build visualization for Cumulative Deaths Different Data dataset.
    def create_cumulative_deaths_different_data_plot(self, plots_data, plots_type):
        hps_source_data = plots_data.iloc[:int(len(plots_data) / 2)]
        nrs_source_data = plots_data.iloc[int(len(plots_data) / 2):]
        dates = hps_source_data["Date"].tolist()
        ax = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                ax = sns.lineplot(data=hps_source_data, x="Date", y=self.plots_y_values)
                ax = sns.lineplot(data=nrs_source_data, x="Date", y=self.plots_y_values)
            elif plots_type == "kde":
                ax = sns.kdeplot(data=hps_source_data, shade=True)
                ax = sns.kdeplot(data=nrs_source_data, shade=True)
                ax.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                ax = sns.histplot(data=hps_source_data)
                ax = sns.histplot(data=nrs_source_data)
                ax.set_xlabel(self.plots_ylabel)
            ax.legend(["HPS", "NRS"])
        else:
            rows = len(hps_source_data)
            sources_data = pd.DataFrame({
                "label": ["HPS"] * rows + ["NRS"] * rows,
                "value": np.concatenate([hps_source_data[self.plots_y_values], nrs_source_data[self.plots_y_values]])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=sources_data, x="label", y="value")
            elif plots_type == "violin":
                ax = sns.violinplot(data=sources_data, x="label", y="value")
            ax.set_ylabel(self.plots_ylabel)
            ax.set_xlabel("Sources")
        plot = [ax, dates]
        return plot

    # Build visualization for Deaths By Age dataset.
    def create_deaths_by_age_plot(self, plots_data, plots_type):
        plot = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            plot = sns.barplot(data=plots_data, x="Age group", y=self.plots_y_values)
        elif plots_type == "kde":
            plot = sns.kdeplot(data=plots_data[self.plots_y_values], shade=True)
        elif plots_type == "histogram":
            plot = sns.histplot(data=plots_data[self.plots_y_values])
        elif plots_type == "pie":
            plot = plt.pie(x=plots_data[self.plots_y_values], labels=plots_data["Age group"], autopct="%1d%%")
            plt.axis("equal")
        else:
            if plots_type == "box":
                plot = sns.boxplot(data=plots_data[self.plots_y_values])
            elif plots_type == "violin":
                plot = sns.violinplot(data=plots_data[self.plots_y_values])
            plot.axes.xaxis.set_ticks([])
            plot.set_ylabel(self.plots_ylabel)
        return plot

    # Build visualization for Deaths By Board dataset.
    def create_deaths_by_board_plot(self, plots_data, plots_type):
        plot = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            plot = sns.barplot(data=plots_data, x="Health board", y=self.plots_y_values)
            health_boards = plots_data["Health board"].tolist()
            plot.set_xticks(range(len(health_boards)))
            plot.set_xticklabels(health_boards, rotation="45")
        elif plots_type == "kde":
            plot = sns.kdeplot(data=plots_data[self.plots_y_values], shade=True)
        elif plots_type == "histogram":
            plot = sns.histplot(data=plots_data[self.plots_y_values])
        elif plots_type == "pie":
            plot = plt.pie(x=plots_data[self.plots_y_values], labels=plots_data["Health board"], autopct="%1d%%")
            plt.axis("equal")
        else:
            if plots_type == "box":
                plot = sns.boxplot(data=plots_data[self.plots_y_values])
            elif plots_type == "violin":
                plot = sns.violinplot(data=plots_data[self.plots_y_values])
            plot.axes.xaxis.set_ticks([])
            plot.set_ylabel(self.plots_ylabel)
        return plot

    # Build visualization for Deaths By Week dataset.
    def create_deaths_by_week_plot(self, plots_data, plots_type):
        week_numbers = plots_data["Week number"].tolist()
        plot = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                plot = sns.lineplot(data=plots_data, x="Week number", y=self.plots_y_values[0])
                plot = sns.lineplot(data=plots_data, x="Week number", y=self.plots_y_values[1])
                plot = sns.lineplot(data=plots_data, x="Week number", y=self.plots_y_values[2])
                plot.set_xticks(range(len(week_numbers)))
                plot.set_xticklabels(week_numbers, rotation="vertical")
            elif plots_type == "kde":
                plot = sns.kdeplot(data=plots_data[self.plots_y_values[0]], shade=True)
                plot = sns.kdeplot(data=plots_data[self.plots_y_values[1]], shade=True)
                plot = sns.kdeplot(data=plots_data[self.plots_y_values[2]], shade=True)
                plot.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                plot = sns.histplot(data=plots_data[self.plots_y_values[0]])
                plot = sns.histplot(data=plots_data[self.plots_y_values[1]])
                plot = sns.histplot(data=plots_data[self.plots_y_values[2]])
                plot.set_xlabel(self.plots_ylabel)
            plot.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
        else:
            rows = len(week_numbers)
            deaths_data = pd.DataFrame({
                "label": [self.plots_y_values[0]] * rows + [self.plots_y_values[1]] * rows +
                         [self.plots_y_values[2]] * rows,
                "value": np.concatenate([plots_data[self.plots_y_values[0]], plots_data[self.plots_y_values[1]],
                                         plots_data[self.plots_y_values[2]]])
            })
            if plots_type == "box":
                plot = sns.boxplot(data=deaths_data, x="label", y="value")
            elif plots_type == "violin":
                plot = sns.violinplot(data=deaths_data, x="label", y="value")
            plot.set_xlabel("")
            plot.set_ylabel(self.plots_ylabel)
        return plot

    # Build visualization for Deaths By Cause dataset.
    def create_deaths_by_cause_plot(self, plots_data, plots_type):
        plots_values = self.format_deaths_by_cause_data(plots_data)
        registered_deaths_2020_list = plots_values[0]
        registered_deaths_five_year_avg_list = plots_values[1]
        location_of_death_list = plots_values[2]
        cause_of_death_list = plots_values[3]
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            plot = self.format_deaths_by_cause_plot(1, registered_deaths_2020_list, location_of_death_list,
                                                    cause_of_death_list,
                                                    "Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                                    plots_type, plots_data)
            plot = self.format_deaths_by_cause_plot(2, registered_deaths_five_year_avg_list, location_of_death_list,
                                                    cause_of_death_list,
                                                    "Deaths by underlying cause of death and location, five year average",
                                                    plots_type, plots_data)
        else:
            plot = self.format_deaths_by_cause_plot(1, registered_deaths_2020_list, location_of_death_list,
                                                    cause_of_death_list,
                                                    "Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                                    plots_type, plots_data)
        plt.subplots_adjust(wspace=1, hspace=1)
        return plot

    # Prepare data in Deaths By Week dataset for plotting.
    @staticmethod
    def format_deaths_by_cause_data(plots_data):
        # Format data in dataset for each variable in plot.
        cause_of_death_column = plots_data["Location of death"]
        cause_of_death_column = cause_of_death_column.iloc[6:13]
        cause_of_death_column_list = cause_of_death_column.tolist()
        cause_of_death_list = []
        for cause in cause_of_death_column_list:
            cause_of_death_list.append([cause] * 4)
        cause_of_death_list = [item for sublist in cause_of_death_list for item in sublist]
        location_of_death_data = plots_data.drop(columns=["Location of death"])
        location_of_death_columns = location_of_death_data.columns.tolist()
        location_of_death_list = location_of_death_columns * 7
        registered_deaths_five_year_avg_covid_19_row = pd.DataFrame([[0, 0, 0, 0]], columns=location_of_death_columns)
        registered_deaths_five_year_avg_data = location_of_death_data.iloc[0:6]
        registered_deaths_five_year_avg_data = registered_deaths_five_year_avg_data.append(
            registered_deaths_five_year_avg_covid_19_row, ignore_index=True)
        registered_deaths_five_year_avg_list = registered_deaths_five_year_avg_data.values.tolist()
        registered_deaths_five_year_avg_list = [item for sublist in registered_deaths_five_year_avg_list
                                                for item in sublist]
        registered_deaths_2020_data = location_of_death_data.iloc[6:13]
        registered_deaths_2020_list = registered_deaths_2020_data.values.tolist()
        registered_deaths_2020_list = [item for sublist in registered_deaths_2020_list for item in sublist]
        plots_values = [registered_deaths_2020_list, registered_deaths_five_year_avg_list, location_of_death_list,
                        cause_of_death_list]
        return plots_values

    # Prepare plots in Deaths By Week dataset.
    def format_deaths_by_cause_plot(self, subplots_index, plots_x_values, plots_y_values, plots_hue, plots_title,
                                    plots_type, plots_data):
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            plt.subplot(1, 2, subplots_index)
            ax = sns.barplot(x=plots_x_values, y=plots_y_values, hue=plots_hue)
            x_values = [y * 500 for y in range(1, 21)]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_xlabel("Number of deaths")
            ax.set_title(plots_title)
        else:
            f, ax = plt.subplots(figsize=(25, 15))
            locations = plots_data.columns.tolist()
            causes_labels = plots_data["Location of death"].iloc[6:13]
            causes_labels.drop([11], inplace=True)
            locations_causes_labels = causes_labels.values.tolist()
            counter = 1
            for i in range(1, len(locations)):
                location = locations[i]
                causes = plots_data[location].iloc[6:13]
                causes.drop([11], inplace=True)
                locations_causes = causes.values.tolist()
                plt.subplot(2, 2, counter)
                ax = plt.pie(x=locations_causes, labels=locations_causes_labels, autopct="%1d%%")
                plt.axis("equal")
                plt.title(location)
                counter += 1
            f.suptitle(self.plots_title)
        sns.despine(top=True, right=True)
        return ax

    # Build visualization for Deaths By Location dataset.
    def create_deaths_by_location_plot(self, plots_data, plots_type):
        week_numbers = plots_data.columns.tolist()
        week_numbers = week_numbers[1:]
        care_home_deaths = plots_data.loc[0].values.tolist()
        care_home_deaths = care_home_deaths[1:]
        home_deaths = plots_data.loc[1].values.tolist()
        home_deaths = home_deaths[1:]
        hospital_deaths = plots_data.loc[2].values.tolist()
        hospital_deaths = hospital_deaths[1:]
        plot = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                plot = sns.lineplot(x=week_numbers, y=care_home_deaths)
                plot = sns.lineplot(x=week_numbers, y=home_deaths)
                plot = sns.lineplot(x=week_numbers, y=hospital_deaths)
                plot.set_xticks(range(len(week_numbers)))
                plot.set_xticklabels(week_numbers, rotation="vertical")
            elif plots_type == "kde":
                plot = sns.kdeplot(data=care_home_deaths, shade=True)
                plot = sns.kdeplot(data=home_deaths, shade=True)
                plot = sns.kdeplot(data=hospital_deaths, shade=True)
                plot.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                plot = sns.histplot(data=care_home_deaths)
                plot = sns.histplot(data=home_deaths)
                plot = sns.histplot(data=hospital_deaths)
                plot.set_xlabel(self.plots_ylabel)
            plot.legend(["Care Home", "Home / Non-institution", "Hospital"])
        elif plots_type == "pie":
            location_totals = [sum(care_home_deaths), sum(home_deaths), sum(hospital_deaths)]
            location_labels = plots_data["Week number"].iloc[0:3]
            plot = plt.pie(x=location_totals, labels=location_labels, autopct="%1d%%")
            plt.axis("equal")
        else:
            rows = len(week_numbers)
            locations_data = pd.DataFrame({
                "label": ["Care Home"] * rows + ["Home / Non-institution"] * rows + ["Hospital"] * rows,
                "value": np.concatenate([care_home_deaths, home_deaths, hospital_deaths])
            })
            if plots_type == "box":
                plot = sns.boxplot(data=locations_data, x="label", y="value")
            elif plots_type == "violin":
                plot = sns.violinplot(data=locations_data, x="label", y="value")
            plot.set_xlabel("Locations")
            plot.set_ylabel(self.plots_ylabel)
        return plot

    # Build visualization for Deaths By Dates dataset.
    def create_deaths_by_dates_plot(self, plots_data, plots_type):
        dates = plots_data["Date"].tolist()
        ax = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                ax = sns.lineplot(data=plots_data, x="Date", y=self.plots_y_values[0])
                ax = sns.lineplot(data=plots_data, x="Date", y=self.plots_y_values[1])
            elif plots_type == "kde":
                ax = sns.kdeplot(data=plots_data[self.plots_y_values[0]], shade=True)
                ax = sns.kdeplot(data=plots_data[self.plots_y_values[1]], shade=True)
                ax.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                ax = sns.histplot(data=plots_data[self.plots_y_values[0]])
                ax = sns.histplot(data=plots_data[self.plots_y_values[1]])
                ax.set_xlabel(self.plots_ylabel)
            ax.legend(self.plots_y_values)
            ax.xaxis.grid(True)
        else:
            rows = len(dates)
            dates_data = pd.DataFrame({
                "label": [self.plots_y_values[0]] * rows + [self.plots_y_values[1]] * rows,
                "value": np.concatenate([plots_data[self.plots_y_values[0]], plots_data[self.plots_y_values[1]]])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=dates_data, x="label", y="value")
            elif plots_type == "violin":
                ax = sns.violinplot(data=dates_data, x="label", y="value")
            ax.set_ylabel(self.plots_ylabel)
            ax.set_xlabel("Date")
        plot = [ax, dates]
        return plot
