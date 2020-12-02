import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class DeathsDataPlots(object):

    def __init__(self, plot_path, plot_title, plot_ylabel, plot_yticks, plot_y_values):
        self.plot_path = plot_path
        self.plot_title = plot_title
        self.plot_ylabel = plot_ylabel
        self.plot_yticks = plot_yticks
        self.plot_y_values = plot_y_values

    def create_plot_titles_list(self):
        plot_titles = [
            "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
            "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
            "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
            "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
            "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
            "Deaths by week of registration, Scotland, 2020",
            "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020",
            "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
            "Deaths involving COVID-19, date of death vs date of registration"
        ]
        return plot_titles

    def create_visualization(self):
        plt.close("all")
        plot_data = pd.read_csv(self.plot_path)
        plot_titles = self.create_plot_titles_list()
        if self.plot_title == plot_titles[6]:
            plot = self.create_death_by_cause_plot(plot_data)
        else:
            if self.plot_ylabel == "Cumulative number of deaths":
                if self.plot_title == plot_titles[0]:
                    plot = self.create_cumulative_deaths_plot(plot_data)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plot_title == plot_titles[1]:
                    plot = self.create_cumulative_deaths_different_data_plot(plot_data)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plot_title == plot_titles[8]:
                    plot = self.create_deaths_by_dates_plot(plot_data)
                    ax = plot[0]
                    dates = plot[1]
                x_values = dates[::7]
                ax.set_xticks(x_values)
                ax.set_xticklabels(x_values, rotation="vertical")
            elif self.plot_ylabel == "Number of deaths":
                if self.plot_title == plot_titles[2] or self.plot_title == plot_titles[3]:
                    ax = self.create_deaths_by_age_plot(plot_data)
                elif self.plot_title == plot_titles[4]:
                    ax = self.create_deaths_by_board_plot(plot_data)
                elif self.plot_title == plot_titles[5]:
                    ax = self.create_death_by_week_plot(plot_data)
                elif self.plot_title == plot_titles[7]:
                    ax = self.create_death_by_location_plot(plot_data)
            ax.set_yticks(self.plot_yticks)
            ax.set_ylabel(self.plot_ylabel)
            ax.set_title(self.plot_title)
            sns.despine(top=True, right=True)
        plt.show()

    def create_cumulative_deaths_plot(self, plot_data):
        dates = plot_data["Date"].tolist()
        ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values)
        plot = [ax, dates]
        return plot

    def create_cumulative_deaths_different_data_plot(self, plot_data):
        hps_source_data = plot_data.iloc[:int(len(plot_data) / 2)]
        nrs_source_data = plot_data.iloc[int(len(plot_data) / 2):]
        dates = hps_source_data["Date"].tolist()
        ax = sns.lineplot(data=hps_source_data, x="Date", y=self.plot_y_values)
        ax = sns.lineplot(data=nrs_source_data, x="Date", y=self.plot_y_values)
        ax.legend(["HPS", "NRS"])
        plot = [ax, dates]
        return plot

    def create_deaths_by_age_plot(self, plot_data):
        plot = sns.barplot(data=plot_data, x="Age group", y=self.plot_y_values)
        return plot

    def create_deaths_by_board_plot(self, plot_data):
        plot = sns.barplot(data=plot_data, x="Health board", y=self.plot_y_values)
        health_boards = plot_data["Health board"].tolist()
        plot.set_xticks(range(len(health_boards)))
        plot.set_xticklabels(health_boards, rotation="45")
        return plot

    def create_death_by_week_plot(self, plot_data):
        week_numbers = plot_data["Week number"].tolist()
        plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[0])
        plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[1])
        plot = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[2])
        plot.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
        plot.set_xticks(range(len(week_numbers)))
        plot.set_xticklabels(week_numbers, rotation="vertical")
        return plot

    def create_death_by_cause_plot(self, plot_data):
        plot_values = self.format_death_by_cause_data(plot_data)
        registered_deaths_2020_list = plot_values[0]
        registered_deaths_five_year_avg_list = plot_values[1]
        location_of_death_list = plot_values[2]
        cause_of_death_list = plot_values[3]
        plot = self.format_death_by_cause_plot(1, registered_deaths_2020_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, week 12 to 30, 2020")
        plot = self.format_death_by_cause_plot(2, registered_deaths_five_year_avg_list, location_of_death_list, cause_of_death_list, "Deaths by underlying cause of death and location, five year average")
        plt.subplots_adjust(wspace=1, hspace=1)
        return plot

    def format_death_by_cause_data(self, plot_data):
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
        registered_deaths_five_year_avg_data = registered_deaths_five_year_avg_data.append(
            registered_deaths_five_year_avg_covid_19_row, ignore_index=True)
        registered_deaths_five_year_avg_list = registered_deaths_five_year_avg_data.values.tolist()
        registered_deaths_five_year_avg_list = [item for sublist in registered_deaths_five_year_avg_list for item in
                                                sublist]
        registered_deaths_2020_data = location_of_death_data.iloc[6:13]
        registered_deaths_2020_list = registered_deaths_2020_data.values.tolist()
        registered_deaths_2020_list = [item for sublist in registered_deaths_2020_list for item in sublist]
        plot_values = [registered_deaths_2020_list, registered_deaths_five_year_avg_list, location_of_death_list, cause_of_death_list]
        return plot_values

    def format_death_by_cause_plot(self, subplot_index, plot_x_values, plot_y_values, plot_hue, plot_title):
        plt.subplot(1, 2, subplot_index)
        ax = sns.barplot(x=plot_x_values, y=plot_y_values, hue=plot_hue)
        ax.set_title(plot_title)
        x_values = [y * 500 for y in range(1, 21)]
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_xlabel("Number of deaths")
        sns.despine(top=True, right=True)
        return ax

    def create_death_by_location_plot(self, plot_data):
        week_numbers = plot_data.columns.tolist()
        week_numbers = week_numbers[1:]
        care_home_deaths = plot_data.loc[0].values.tolist()
        care_home_deaths = care_home_deaths[1:]
        home_deaths = plot_data.loc[1].values.tolist()
        home_deaths = home_deaths[1:]
        hospital_deaths = plot_data.loc[2].values.tolist()
        hospital_deaths = hospital_deaths[1:]
        plot = sns.lineplot(x=week_numbers, y=care_home_deaths)
        plot = sns.lineplot(x=week_numbers, y=home_deaths)
        plot = sns.lineplot(x=week_numbers, y=hospital_deaths)
        plot.legend(["Care Home", "Home / Non-institution", "Hospital"])
        plot.set_xticks(range(len(week_numbers)))
        plot.set_xticklabels(week_numbers, rotation="vertical")
        return plot

    def create_deaths_by_dates_plot(self, plot_data):
        dates = plot_data["Date"].tolist()
        ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[0])
        ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[1])
        ax.legend([self.plot_y_values[0], self.plot_y_values[1]])
        ax.xaxis.grid(True)
        plot = [ax, dates]
        return plot
