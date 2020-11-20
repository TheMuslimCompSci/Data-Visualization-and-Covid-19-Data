import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class DeathsDataPlots(object):

    def __init__(self):
        self.create_deaths_by_week_plot()

    def create_plots(self):
        plots_data = pd.read_csv(self.plots_path)
        boards = plots_data.columns.tolist()
        dates = plots_data["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            ax = sns.lineplot(data=plots_data, x="Date", y=board)
            ax.set_title(board)
            x_values = dates[::7]
            ax.set_xticks(x_values)
            ax.set_xticklabels(x_values, rotation="vertical")
            ax.set_yticks(self.plots_yticks)
            ax.set_ylabel(self.plots_ylabel)
        plt.subplots_adjust(wspace=1, hspace=1)
        f.suptitle(self.plots_title)
        plt.show()

    def create_cumulative_deaths_plot(self):
        plots_data = pd.read_csv("../covid deaths data week 30/Figure 1 data.csv")
        dates = plots_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=plots_data, x="Date", y="Count", marker="o")
        ax.set_title("Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020")
        sns.despine(top=True, right=True)
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 500 for y in range(1, 10)])
        ax.set_ylabel("Cumulative number of deaths")
        plt.show()

    def create_cumulative_deaths_different_data_plot(self):
        plots_data = pd.read_csv("../covid deaths data week 30/Figure 2 data.csv")
        hps_source_data = plots_data.iloc[:int(len(plots_data)/2)]
        nrs_source_data = plots_data.iloc[int(len(plots_data)/2):]
        dates = hps_source_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=hps_source_data, x="Date", y="Cumulative Count")
        ax2 = sns.lineplot(data=nrs_source_data, x="Date", y="Cumulative Count")
        ax.set_title("Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020")
        ax.legend(["HPS", "NRS"])
        sns.despine(top=True, right=True)
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 500 for y in range(1, 10)])
        ax.set_ylabel("Cumulative number of deaths")
        plt.show()

    def create_covid_deaths_by_age_plot(self):
        plots_data = pd.read_csv("../covid deaths data week 30/Figure 3a and 3b data.csv")
        ax = sns.barplot(data=plots_data, x="Age group", y="Covid deaths to date")
        ax.set_title("COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 200 for y in range(1, 11)])
        ax.set_ylabel("Number of deaths")
        plt.show()

    def create_all_deaths_by_age_plot(self):
        plots_data = pd.read_csv("../covid deaths data week 30/Figure 3a and 3b data.csv")
        ax = sns.barplot(data=plots_data, x="Age group", y="Total deaths to date")
        ax.set_title("All deaths registered between weeks 1 and 30, 2020 by age group, Scotland")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 2000 for y in range(1, 8)])
        ax.set_ylabel("Number of deaths")
        plt.show()

    def create_deaths_by_board_plot(self):
        plots_data = pd.read_csv("../covid deaths data week 30/Figure 4 data.csv")
        ax = sns.barplot(data=plots_data, x="Health board", y="COVID-19 deaths to date")
        ax.set_title("COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 200 for y in range(1, 8)])
        ax.set_ylabel("Number of deaths")
        health_boards = plots_data["Health board"].tolist()
        ax.set_xticks(range(len(health_boards)))
        ax.set_xticklabels(health_boards, rotation="45")
        plt.show()

    def create_deaths_by_week_plot(self):
        plots_data = pd.read_csv("../covid deaths data week 30/Figure 5 data.csv")
        print(plots_data)
        columns = plots_data.columns.tolist()
        weeks = columns[1:]
        all_deaths_row = plots_data.iloc[[0]]
        all_deaths_avg_previous_years_row = plots_data.iloc[[1]]
        covid_deaths_row = plots_data.iloc[[2]]
        all_deaths = all_deaths_row[1:]
        all_deaths_avg_previous_years = all_deaths_avg_previous_years_row[1:]
        covid_deaths = covid_deaths_row[1:]
        ax = sns.lineplot(data=plots_data, x=weeks, y=all_deaths)
        ax2 = sns.lineplot(data=plots_data, x=weeks, y=all_deaths_avg_previous_years)
        ax3 = sns.lineplot(data=plots_data, x=weeks, y=covid_deaths)
        ax.set_title("Deaths by week of registration, Scotland, 2020")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 500 for y in range(1, 6)])
        ax.set_ylabel("Number of deaths")
        plt.show()

DeathsDataPlots()
