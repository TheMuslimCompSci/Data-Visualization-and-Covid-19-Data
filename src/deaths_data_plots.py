import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class DeathsDataPlots(object):

    def __init__(self):
        self.create_deaths_by_cause_plot()

    def create_plots(self):
        plot_data = pd.read_csv(self.plots_path)
        boards = plot_data.columns.tolist()
        dates = plot_data["Date"].tolist()
        f, ax = plt.subplots(figsize=(25, 15))
        for i in range(1, len(boards)):
            board = boards[i]
            plt.subplot(4, 4, i)
            ax = sns.lineplot(data=plot_data, x="Date", y=board)
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
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 1 data.csv")
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y="Count", marker="o")
        ax.set_title("Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020")
        sns.despine(top=True, right=True)
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 500 for y in range(1, 10)])
        ax.set_ylabel("Cumulative number of deaths")
        plt.show()

    def create_cumulative_deaths_different_data_plot(self):
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 2 data.csv")
        hps_source_data = plot_data.iloc[:int(len(plot_data)/2)]
        nrs_source_data = plot_data.iloc[int(len(plot_data)/2):]
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
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 3a and 3b data.csv")
        ax = sns.barplot(data=plot_data, x="Age group", y="Covid deaths to date")
        ax.set_title("COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 200 for y in range(1, 11)])
        ax.set_ylabel("Number of deaths")
        plt.show()

    def create_all_deaths_by_age_plot(self):
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 3a and 3b data.csv")
        ax = sns.barplot(data=plot_data, x="Age group", y="Total deaths to date")
        ax.set_title("All deaths registered between weeks 1 and 30, 2020 by age group, Scotland")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 2000 for y in range(1, 8)])
        ax.set_ylabel("Number of deaths")
        plt.show()

    def create_deaths_by_board_plot(self):
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 4 data.csv")
        ax = sns.barplot(data=plot_data, x="Health board", y="COVID-19 deaths to date")
        ax.set_title("COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland")
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 200 for y in range(1, 8)])
        ax.set_ylabel("Number of deaths")
        health_boards = plot_data["Health board"].tolist()
        ax.set_xticks(range(len(health_boards)))
        ax.set_xticklabels(health_boards, rotation="45")
        plt.show()

    def create_deaths_by_week_plot(self):
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 5 data.csv")
        ax = sns.lineplot(data=plot_data, x="Week number", y="Total deaths 2020")
        ax2 = sns.lineplot(data=plot_data, x="Week number", y="Average for previous 5 years")
        ax3 = sns.lineplot(data=plot_data, x="Week number", y="COVID-19 deaths 2020")
        ax.set_title("Deaths by week of registration, Scotland, 2020")
        ax.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 500 for y in range(1, 6)])
        ax.set_ylabel("Number of deaths")
        week_numbers = plot_data["Week number"].tolist()
        ax.set_xticks(range(len(week_numbers)))
        ax.set_xticklabels(week_numbers, rotation="vertical")
        plt.show()

    def create_deaths_by_cause_plot(self):
        plot_data = pd.read_csv("../covid deaths data week 30/Figure 6 data.csv")
        registered_deaths_2020 = plot_data.iloc[6:13]
        registered_deaths_five_year_avg = plot_data.iloc[0:6]
        columns
        ax = sns.barplot(data=registered_deaths_2020, x="Location of death", y="Hospital")
        ax.set_title("Deaths by underlying cause of death and location, week 12 to 30, 2020")
        #ax.legend(["All deaths 2020", "All deaths, average of previous 5 years", "COVID-19 deaths 2020"])
        sns.despine(top=True, right=True)
        ax.set_yticks([y * 500 for y in range(1, 21)])
        ax.set_ylabel("Number of deaths")
        #week_numbers = plot_data["Week number"].tolist()
        #ax.set_xticks(range(len(week_numbers)))
        #ax.set_xticklabels(week_numbers, rotation="vertical")
        plt.show()

DeathsDataPlots()
