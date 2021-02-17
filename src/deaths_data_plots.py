import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


class DeathsDataPlots(object):

    def __init__(self, plot_path=None, plot_title=None, plot_ylabel=None, plot_yticks=None, plot_y_values=None, plot_types_list=None):
        self.plot_path = plot_path
        self.plot_title = plot_title
        self.plot_ylabel = plot_ylabel
        self.plot_yticks = plot_yticks
        self.plot_y_values = plot_y_values
        self.plot_types_list = plot_types_list

    def get_plots_info(self):
        plots_info = {
            "Cumulative Deaths": ["../covid deaths data week 30/Figure 1 data.csv",
                                  "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
                                  "Cumulative number of deaths", [y * 500 for y in range(1, 10)], "Count",
                                  ["default", "kde", "box", "violin", "histogram"]],

            "Cumulative Deaths Different Data": ["../covid deaths data week 30/Figure 2 data.csv",
                                                 "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
                                                 "Cumulative number of deaths", [y * 500 for y in range(1, 10)], "Cumulative Count",
                                                 ["default", "kde", "box", "violin", "histogram"]],

            "COVID Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                    "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                    "Number of deaths", [y * 200 for y in range(1, 11)], "Covid deaths to date",
                                    ["default", "kde", "box", "violin", "histogram", "pie"]],

            "All Deaths By Age": ["../covid deaths data week 30/Figure 3a and 3b data.csv",
                                  "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                  "Number of deaths", [y * 2000 for y in range(1, 8)], "Total deaths to date",
                                  ["default", "kde", "box", "violin", "histogram", "pie"]],

            "Deaths By Board": ["../covid deaths data week 30/Figure 4 data.csv",
                                "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
                                "Number of deaths", [y * 200 for y in range(1, 8)], "COVID-19 deaths to date",
                                ["default", "kde", "box", "violin", "histogram", "pie"]],

            "Deaths By Week": ["../covid deaths data week 30/Figure 5 data.csv",
                               "Deaths by week of registration, Scotland, 2020",
                               "Number of deaths", [y * 500 for y in range(1, 6)], ["Total deaths 2020", "Average for previous 5 years", "COVID-19 deaths 2020"],
                               ["default", "kde", "box", "violin", "histogram"]],

            "Deaths By Cause": ["../covid deaths data week 30/Figure 6 data.csv",
                                "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                "Number of deaths", [y * 5000 for y in range(1, 6)], "",
                                ["default", "pie"]],

            "Deaths By Location": ["../covid deaths data week 30/Figure 7 data.csv",
                                   "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
                                   "Number of deaths", [y * 50 for y in range(1, 9)], "",
                                   ["default", "kde", "box", "violin", "histogram", "pie"]],

            "Deaths By Date Of Death vs Date Of Registration": ["../covid deaths data week 30/Figure 8 data.csv",
                                                                "Deaths involving COVID-19, date of death vs date of registration",
                                                                "Cumulative number of deaths", [y * 500 for y in range(1, 10)], ["Cumulative deaths by date of death", "Cumulative deaths by date of registration"],
                                                                ["default", "kde", "box", "violin", "histogram"]]
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
            if plot_type == "default":
                ax.set_yticks(self.plot_yticks)
                ax.set_ylabel(self.plot_ylabel)
            plt.title(self.plot_title)
            sns.despine(top=True, right=True)
        plt.show()

    def create_cumulative_deaths_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        if plot_type == "default":
            ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values)
        elif plot_type == "kde" or plot_type == "histogram":
            if plot_type == "kde":
                ax = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
            elif plot_type == "histogram":
                ax = sns.histplot(data=plot_data[self.plot_y_values])
            ax.set_xlabel(self.plot_ylabel)
        else:
            if plot_type == "box":
                ax = sns.boxplot(data=plot_data[self.plot_y_values])
            elif plot_type == "violin":
                ax = sns.violinplot(data=plot_data[self.plot_y_values])
            ax.axes.xaxis.set_ticks([])
            ax.set_ylabel(self.plot_ylabel)
        plot = [ax, dates]
        return plot

    def create_cumulative_deaths_different_data_plot(self, plot_data, plot_type):
        hps_source_data = plot_data.iloc[:int(len(plot_data) / 2)]
        nrs_source_data = plot_data.iloc[int(len(plot_data) / 2):]
        print(hps_source_data)
        dates = hps_source_data["Date"].tolist()
        if plot_type == "default" or plot_type == "kde" or plot_type == "histogram":
            if plot_type == "default":
                ax = sns.lineplot(data=hps_source_data, x="Date", y=self.plot_y_values)
                ax = sns.lineplot(data=nrs_source_data, x="Date", y=self.plot_y_values)
            elif plot_type == "kde":
                ax = sns.kdeplot(data=hps_source_data, shade=True)
                ax = sns.kdeplot(data=nrs_source_data, shade=True)
                ax.set_xlabel(self.plot_ylabel)
            elif plot_type == "histogram":
                ax = sns.histplot(data=hps_source_data)
                ax = sns.histplot(data=nrs_source_data)
                ax.set_xlabel(self.plot_ylabel)
            ax.legend(["HPS", "NRS"])
        else:
            rows = len(hps_source_data)
            sources_data = pd.DataFrame({
                "label": ["HPS"] * rows + ["NRS"] * rows,
                "value": np.concatenate([hps_source_data[self.plot_y_values], nrs_source_data[self.plot_y_values]])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=sources_data, x="label", y="value")
            elif plot_type == "violin":
                ax = sns.violinplot(data=sources_data, x="label", y="value")
            ax.set_ylabel(self.plot_ylabel)
            ax.set_xlabel("Sources")
        plot = [ax, dates]
        return plot

    def create_deaths_by_age_plot(self, plot_data, plot_type):
        if plot_type == "default":
            plot = sns.barplot(data=plot_data, x="Age group", y=self.plot_y_values)
        elif plot_type == "kde":
            plot = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
        elif plot_type == "histogram":
            plot = sns.histplot(data=plot_data[self.plot_y_values])
        elif plot_type == "pie":
            plot = plt.pie(x=plot_data[self.plot_y_values], labels=plot_data["Age group"], autopct="%1d%%")
            plt.axis("equal")
        else:
            if plot_type == "box":
                plot = sns.boxplot(data=plot_data[self.plot_y_values])
            elif plot_type == "violin":
                plot = sns.violinplot(data=plot_data[self.plot_y_values])
            plot.axes.xaxis.set_ticks([])
            plot.set_ylabel(self.plot_ylabel)
        return plot

    def create_deaths_by_board_plot(self, plot_data, plot_type):
        if plot_type == "default":
            plot = sns.barplot(data=plot_data, x="Health board", y=self.plot_y_values)
            health_boards = plot_data["Health board"].tolist()
            plot.set_xticks(range(len(health_boards)))
            plot.set_xticklabels(health_boards, rotation="45")
        elif plot_type == "kde":
            plot = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
        elif plot_type == "histogram":
            plot = sns.histplot(data=plot_data[self.plot_y_values])
        elif plot_type == "pie":
            plot = plt.pie(x=plot_data[self.plot_y_values], labels=plot_data["Health board"], autopct="%1d%%")
            plt.axis("equal")
        else:
            if plot_type == "box":
                plot = sns.boxplot(data=plot_data[self.plot_y_values])
            elif plot_type == "violin":
                plot = sns.violinplot(data=plot_data[self.plot_y_values])
            plot.axes.xaxis.set_ticks([])
            plot.set_ylabel(self.plot_ylabel)
        return plot

    def create_death_by_week_plot(self, plot_data, plot_type):
        week_numbers = plot_data["Week number"].tolist()
        if plot_type == "default" or plot_type == "kde" or plot_type == "histogram":
            if plot_type == "default":
                plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[0])
                plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[1])
                plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[2])
                plot.set_xticks(range(len(week_numbers)))
                plot.set_xticklabels(week_numbers, rotation="vertical")
            elif plot_type == "kde":
                plot = sns.kdeplot(data=plot_data[self.plot_y_values[0]], shade=True)
                plot = sns.kdeplot(data=plot_data[self.plot_y_values[1]], shade=True)
                plot = sns.kdeplot(data=plot_data[self.plot_y_values[2]], shade=True)
                plot.set_xlabel(self.plot_ylabel)
            elif plot_type == "histogram":
                plot = sns.histplot(data=plot_data[self.plot_y_values[0]])
                plot = sns.histplot(data=plot_data[self.plot_y_values[1]])
                plot = sns.histplot(data=plot_data[self.plot_y_values[2]])
                plot.set_xlabel(self.plot_ylabel)
            plot.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
        else:
            rows = len(week_numbers)
            deaths_data = pd.DataFrame({
                "label": [self.plot_y_values[0]] * rows + [self.plot_y_values[1]] * rows + [self.plot_y_values[2]] * rows,
                "value": np.concatenate([plot_data[self.plot_y_values[0]], plot_data[self.plot_y_values[1]], plot_data[self.plot_y_values[2]]])
            })
            if plot_type == "box":
                plot = sns.boxplot(data=deaths_data, x="label", y="value")
            elif plot_type == "violin":
                plot = sns.violinplot(data=deaths_data, x="label", y="value")
            plot.set_xlabel("")
            plot.set_ylabel(self.plot_ylabel)
        return plot

    def create_death_by_cause_plot(self, plot_data, plot_type):
        plot_values = self.format_death_by_cause_data(plot_data, plot_type)
        registered_deaths_2020_list = plot_values[0]
        registered_deaths_five_year_avg_list = plot_values[1]
        location_of_death_list = plot_values[2]
        cause_of_death_list = plot_values[3]
        if plot_type == "default":
            plot = self.format_death_by_cause_plot(1, registered_deaths_2020_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, week 12 to 30, 2020", plot_type, plot_data)
            plot = self.format_death_by_cause_plot(2, registered_deaths_five_year_avg_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, five year average", plot_type, plot_data)
        else:
            plot = self.format_death_by_cause_plot(1, registered_deaths_2020_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, week 12 to 30, 2020", plot_type, plot_data)
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

    def format_death_by_cause_plot(self, subplot_index, plot_x_values, plot_y_values, plot_hue, plot_title, plot_type, plot_data):
        if plot_type == "default":
            plt.subplot(1, 2, subplot_index)
            ax = sns.barplot(x=plot_x_values, y=plot_y_values, hue=plot_hue)
            x_values = [y * 500 for y in range(1, 21)]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_xlabel("Number of deaths")
            ax.set_title(plot_title)
        else:
            f, ax = plt.subplots(figsize=(25, 15))
            locations = plot_data.columns.tolist()
            locations_totals = []
            causes_labels = plot_data["Location of death"].iloc[6:13]
            causes_labels.drop([11], inplace=True)
            locations_causes_labels = causes_labels.values.tolist()
            counter = 1
            for i in range(1, len(locations)):
                location = locations[i]
                causes = plot_data[location].iloc[6:13]
                causes.drop([11], inplace=True)
                locations_causes = causes.values.tolist()
                plt.subplot(2, 2, counter)
                ax = plt.pie(x=locations_causes, labels=locations_causes_labels, autopct="%1d%%")
                plt.axis("equal")
                plt.title(location)
                counter += 1
            f.suptitle(self.plot_title)

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
        if plot_type == "default" or plot_type == "kde" or plot_type == "histogram":
            if plot_type == "default":
                plot = sns.lineplot(x=week_numbers, y=care_home_deaths)
                plot = sns.lineplot(x=week_numbers, y=home_deaths)
                plot = sns.lineplot(x=week_numbers, y=hospital_deaths)
                plot.set_xticks(range(len(week_numbers)))
                plot.set_xticklabels(week_numbers, rotation="vertical")
            elif plot_type == "kde":
                plot = sns.kdeplot(data=care_home_deaths, shade=True)
                plot = sns.kdeplot(data=home_deaths, shade=True)
                plot = sns.kdeplot(data=hospital_deaths, shade=True)
                plot.set_xlabel(self.plot_ylabel)
            elif plot_type == "histogram":
                plot = sns.histplot(data=care_home_deaths)
                plot = sns.histplot(data=home_deaths)
                plot = sns.histplot(data=hospital_deaths)
                plot.set_xlabel(self.plot_ylabel)
            plot.legend(["Care Home", "Home / Non-institution", "Hospital"])
        elif plot_type == "pie":
            location_totals = [sum(care_home_deaths), sum(home_deaths), sum(hospital_deaths)]
            location_labels = plot_data["Week number"].iloc[0:3]
            plot = plt.pie(x=location_totals, labels=location_labels, autopct="%1d%%")
            plt.axis("equal")
        else:
            rows = len(week_numbers)
            locations_data = pd.DataFrame({
                "label": ["Care Home"] * rows + ["Home / Non-institution"] * rows + ["Hospital"] * rows,
                "value": np.concatenate([care_home_deaths, home_deaths, hospital_deaths])
            })
            if plot_type == "box":
                plot = sns.boxplot(data=locations_data, x="label", y="value")
            elif plot_type == "violin":
                plot = sns.violinplot(data=locations_data, x="label", y="value")
            plot.set_xlabel("Locations")
            plot.set_ylabel(self.plot_ylabel)
        return plot

    def create_deaths_by_dates_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        if plot_type == "default" or plot_type == "kde" or plot_type == "histogram":
            if plot_type == "default":
                ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[0])
                ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[1])
            elif plot_type == "kde":
                ax = sns.kdeplot(data=plot_data[self.plot_y_values[0]], shade=True)
                ax = sns.kdeplot(data=plot_data[self.plot_y_values[1]], shade=True)
                ax.set_xlabel(self.plot_ylabel)
            elif plot_type == "histogram":
                ax = sns.histplot(data=plot_data[self.plot_y_values[0]])
                ax = sns.histplot(data=plot_data[self.plot_y_values[1]])
                ax.set_xlabel(self.plot_ylabel)
            ax.legend(self.plot_y_values)
            ax.xaxis.grid(True)
        else:
            rows = len(dates)
            dates_data = pd.DataFrame({
                "label": [self.plot_y_values[0]] * rows + [self.plot_y_values[1]] * rows,
                "value": np.concatenate([plot_data[self.plot_y_values[0]], plot_data[self.plot_y_values[1]]])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=dates_data, x="label", y="value")
            elif plot_type == "violin":
                ax = sns.violinplot(data=dates_data, x="label", y="value")
            ax.set_ylabel(self.plot_ylabel)
            ax.set_xlabel("Date")
        plot = [ax, dates]
        return plot

    def get_plots_title(self):
        return self.plot_title

    def get_plots_types_list(self):
        return self.plot_types_list

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
