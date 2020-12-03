import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


class TrendsInDailyDataPlots(object):

    def __init__(self, plots_path, plots_title, plots_ylabel, plots_yticks):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks
        self.create_deaths_plot()

    def create_nhs_24_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 1 - NHS 24.csv")
        dates = plot_data["Date"].tolist()
        x_values = dates[::4]
        ax = sns.lineplot(data=plot_data, x="Date", y="NHS24 111 Calls")
        ax = sns.lineplot(data=plot_data, x="Date", y="Coronavirus Helpline Calls")
        ax.set_title("Daily number of calls to NHS24 111 and the Coronavirus helpline")
        ax.yaxis.grid(True)
        ax.legend(["NHS 111 Calls", "Coronavirus Helpline Calls"])
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 2000 for y in range(1, 8)])
        ax.set_ylabel("Number of calls")
        sns.despine(top=True, right=True)
        plt.show()

    def create_hospital_confirmed_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv")
        plot_data = plot_data.iloc[9:]
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.barplot(data=plot_data, x="Date", y="(ii) Confirmed")
        ax.set_title("Daily number of confirmed COVID-19 patients in hospital")
        ax.yaxis.grid(True)
        ax.set_xticks(range(len(x_values)))
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 200 for y in range(1, 9)])
        ax.set_ylabel("Number of patients")
        sns.despine(top=True, right=True)
        plt.show()

    def create_hospital_care_icu_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv")
        plot_data = plot_data.iloc[9:]
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.barplot(data=plot_data, x="Date", y="(i) Confirmed")
        ax.set_title("Daily number of confirmed COVID-19 patients in ICU or combined ICU/HDU")
        ax.yaxis.grid(True)
        ax.set_xticks(range(len(x_values)))
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 50 for y in range(1, 6)])
        ax.set_ylabel("Number of patients")
        sns.despine(top=True, right=True)
        plt.show()

    def create_ambulance_attendances_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv")
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y="Number of attendances")
        ax = sns.lineplot(data=plot_data, x="Date", y="Number of COVID-19 suspected attendances")
        ax.set_title("Number of Attendances (total and COVID-19 suspected)")
        ax.yaxis.grid(True)
        ax.legend(["Number of attendances", "Number of COVID-19 suspected attendances"])
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 200 for y in range(1, 11)])
        ax.set_ylabel("Number of attendances")
        sns.despine(top=True, right=True)
        plt.show()

    def create_ambulance_to_hospital_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv")
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y="Number of suspected COVID-19 patients taken to hospital")
        ax.set_title("Number of suspected COVID-19 patients taken to hospital by ambulance")
        ax.yaxis.grid(True)
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 50 for y in range(1, 9)])
        ax.set_ylabel("Number of patients")
        sns.despine(top=True, right=True)
        plt.show()

    def create_delayed_discharges_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 4 - Delayed Discharges.csv")
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y="Number of delayed discharges")
        ax.set_title("Daily Delayed Discharges")
        ax.yaxis.grid(True)
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="vertical")
        ax.set_yticks([y * 200 for y in range(1, 10)])
        ax.set_ylabel("Number of discharges")
        sns.despine(top=True, right=True)
        plt.show()

    def create_people_tested_plot(self):

    def create_deaths_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 8 - Deaths.csv")
        dates = plot_data["Date"].tolist()
        x_values = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y="Number of COVID-19 confirmed deaths registered to date")
        ax.set_title("Number of COVID-19 confirmed deaths registered to date")
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_values, rotation="45")
        ax.set_yticks([y * 500 for y in range(1, 7)])
        ax.set_ylabel("Number of deaths")
        sns.despine(top=True, right=True)
        plt.show()

TrendsInDailyDataPlots(1,2,3,4)