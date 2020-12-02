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

    def create_cumulative_deaths_plot(self):
        plt.close("all")
        plot_data = pd.read_csv(self.plot_path)
        if self.plot_title == "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020":
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
            registered_deaths_five_year_avg_covid_19_row = pd.DataFrame([[0, 0, 0, 0]],
                                                                        columns=location_of_death_columns)
            registered_deaths_five_year_avg_data = location_of_death_data.iloc[0:6]
            registered_deaths_five_year_avg_data = registered_deaths_five_year_avg_data.append(
                registered_deaths_five_year_avg_covid_19_row, ignore_index=True)
            registered_deaths_five_year_avg_list = registered_deaths_five_year_avg_data.values.tolist()
            registered_deaths_five_year_avg_list = [item for sublist in registered_deaths_five_year_avg_list for item in
                                                    sublist]
            registered_deaths_2020_data = location_of_death_data.iloc[6:13]
            registered_deaths_2020_list = registered_deaths_2020_data.values.tolist()
            registered_deaths_2020_list = [item for sublist in registered_deaths_2020_list for item in sublist]
            plt.subplot(1, 2, 1)
            ax = sns.barplot(x=registered_deaths_2020_list, hue=cause_of_death_list, y=location_of_death_list)
            ax.set_title("Deaths by underlying cause of death and location, week 12 to 30, 2020")
            sns.despine(top=True, right=True)
            x_values = [y * 500 for y in range(1, 21)]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_xlabel("Number of deaths")
            plt.subplot(1, 2, 2)
            ax = sns.barplot(x=registered_deaths_five_year_avg_list, hue=cause_of_death_list, y=location_of_death_list)
            ax.set_title("Deaths by underlying cause of death and location, five year average")
            sns.despine(top=True, right=True)
            x_values = [y * 500 for y in range(1, 21)]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_xlabel("Number of deaths")
            plt.subplots_adjust(wspace=1, hspace=1)
        else:
            if self.plot_ylabel == "Cumulative number of deaths":
                if self.plot_title == "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020":
                    dates = plot_data["Date"].tolist()
                    ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values)
                elif self.plot_title == "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020":
                    hps_source_data = plot_data.iloc[:int(len(plot_data) / 2)]
                    nrs_source_data = plot_data.iloc[int(len(plot_data) / 2):]
                    dates = hps_source_data["Date"].tolist()
                    ax = sns.lineplot(data=hps_source_data, x="Date", y=self.plot_y_values)
                    ax2 = sns.lineplot(data=nrs_source_data, x="Date", y=self.plot_y_values)
                    ax.legend(["HPS", "NRS"])
                elif self.plot_title == "Deaths involving COVID-19, date of death vs date of registration":
                    dates = plot_data["Date"].tolist()
                    ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[0])
                    ax2 = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[1])
                    ax.legend([self.plot_y_values[0], self.plot_y_values[1]])
                    ax.xaxis.grid(True)
                x_values = dates[::7]
                ax.set_xticks(x_values)
                ax.set_xticklabels(x_values, rotation="vertical")
            elif self.plot_ylabel == "Number of deaths":
                if self.plot_title == "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland" or self.plot_title == "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland":
                    ax = sns.barplot(data=plot_data, x="Age group", y=self.plot_y_values)
                elif self.plot_title == "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland":
                    ax = sns.barplot(data=plot_data, x="Health board", y=self.plot_y_values)
                    health_boards = plot_data["Health board"].tolist()
                    ax.set_xticks(range(len(health_boards)))
                    ax.set_xticklabels(health_boards, rotation="45")
                elif self.plot_title == "Deaths by week of registration, Scotland, 2020":
                    week_numbers = plot_data["Week number"].tolist()
                    ax = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[0])
                    ax2 = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[1])
                    ax3 = sns.lineplot(data=plot_data, x="Week number", y=self.plot_y_values[2])
                    ax.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
                    ax.set_xticks(range(len(week_numbers)))
                    ax.set_xticklabels(week_numbers, rotation="vertical")
                elif self.plot_title == "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020":
                    week_numbers = plot_data.columns.tolist()
                    week_numbers = week_numbers[1:]
                    care_home_deaths = plot_data.loc[0].values.tolist()
                    care_home_deaths = care_home_deaths[1:]
                    home_deaths = plot_data.loc[1].values.tolist()
                    home_deaths = home_deaths[1:]
                    hospital_deaths = plot_data.loc[2].values.tolist()
                    hospital_deaths = hospital_deaths[1:]
                    ax = sns.lineplot(x=week_numbers, y=care_home_deaths)
                    ax2 = sns.lineplot(x=week_numbers, y=home_deaths)
                    ax3 = sns.lineplot(x=week_numbers, y=hospital_deaths)
                    ax.legend(["Care Home", "Home / Non-institution", "Hospital"])
                    ax.set_xticks(range(len(week_numbers)))
                    ax.set_xticklabels(week_numbers, rotation="vertical")
            ax.set_yticks(self.plot_yticks)
            ax.set_ylabel(self.plot_ylabel)
            ax.set_title(self.plot_title)
            sns.despine(top=True, right=True)
        plt.show()

    def create_deaths_by_cause_plot(self):
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 6 data.csv")

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
        plt.subplot(1, 2, 1)
        ax = sns.barplot(x=registered_deaths_2020_list, hue=cause_of_death_list, y=location_of_death_list)
        ax.set_title("Deaths by underlying cause of death and location, week 12 to 30, 2020")
        sns.despine(top=True, right=True)
        x_values = [y * 500 for y in range(1, 21)]
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_xlabel("Number of deaths")
        plt.subplot(1, 2, 2)
        ax = sns.barplot(x=registered_deaths_five_year_avg_list, hue=cause_of_death_list, y=location_of_death_list)
        ax.set_title("Deaths by underlying cause of death and location, five year average")
        sns.despine(top=True, right=True)
        x_values = [y * 500 for y in range(1, 21)]
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_xlabel("Number of deaths")
        plt.subplots_adjust(wspace=1, hspace=1)
        plt.show()