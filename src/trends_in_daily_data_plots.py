import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


class TrendsInDailyDataPlots(object):

    def __init__(self, plot_path=None, plot_title=None, plot_ylabel=None, plot_yticks=None, plot_y_values=None, plot_type=None):
        self.plot_path = plot_path
        self.plot_title = plot_title
        self.plot_ylabel = plot_ylabel
        self.plot_yticks = plot_yticks
        self.plot_y_values = plot_y_values
        self.plot_type = plot_type

    def get_plots_info(self):
        plots_info = {
            "NHS 24": ["../Trends in daily COVID-19 data 22 July 2020/Table 1 - NHS 24.csv",
                       "Daily number of calls to NHS24 111 and the Coronavirus helpline",
                       "Number of calls", [y * 2000 for y in range(1, 8)],
                       ["NHS24 111 Calls", "Coronavirus Helpline Calls"], "line"],

            "Hospital Confirmed": ["../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                   "Daily number of confirmed COVID-19 patients in hospital",
                                   "Number of patients", [y * 200 for y in range(1, 9)],
                                   "(ii) Confirmed", "bar"],

            "Hospital Care (ICU)": ["../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                    "Daily number of confirmed COVID-19 patients in ICU or combined ICU/HDU",
                                    "Number of patients", [y * 50 for y in range(1, 6)],
                                    "(i) Confirmed", "bar"],

            "Ambulance Attendances": ["../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of Attendances (total and COVID-19 suspected)",
                                      "Number of attendances", [y * 200 for y in range(1, 11)],
                                      ["Number of attendances", "Number of COVID-19 suspected attendances"], "line"],

            "Ambulance To Hospital": ["../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of suspected COVID-19 patients taken to hospital by ambulance",
                                      "Number of patients", [y * 50 for y in range(1, 9)],
                                      "Number of suspected COVID-19 patients taken to hospital", "line"],

            "Delayed Discharges": ["../Trends in daily COVID-19 data 22 July 2020/Table 4 - Delayed Discharges.csv",
                                   "Daily Delayed Discharges",
                                   "Number of delayed discharges", [y * 200 for y in range(1, 10)],
                                   "Number of delayed discharges", "line"],

            "People Tested": ["../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                              "Number of people tested for COVID-19 in Scotland to date, by results",
                              "Number of people tested", [y * 50000 for y in range(1, 8)],
                              ["(i) Positive", "(i) Negative"], "bar"],

            "Number Of Tests": ["../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                                "Cumulative number of COVID-19 Tests carried out in Scotland",
                                "Number of tests", [y * 100000 for y in range(1, 8)],
                                ["(iii) Cumulative", "(iv) Cumulative"], "bar"],

            "Daily Positive Cases": ["../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                                     "Number of daily new positive cases and 7-day rolling average",
                                     "Number of cases", [y * 50 for y in range(1, 11)],
                                     "(ii) Daily", "bar"],

            "Workforce": ["../Trends in daily COVID-19 data 22 July 2020/Table 6 - Workforce.csv",
                          "Number of NHS staff reporting as absent due to Covid-19",
                          "Number of staff", [y * 1000 for y in range(1, 11)],
                          "", "bar"],

            "Care Homes": ["../Trends in daily COVID-19 data 22 July 2020/Table 7a - Care Homes.csv",
                           "Daily number of new suspected Covid-19 cases reported in Scottish adult care homes",
                           "Number of cases", [y * 50 for y in range(1, 6)],
                           "Daily number of new suspected COVID-19 cases in adult care homes", "bar"],

            "Deaths": ["../Trends in daily COVID-19 data 22 July 2020/Table 8 - Deaths.csv",
                       "Number of COVID-19 confirmed deaths registered to date",
                       "Number of deaths", [y * 500 for y in range(1, 7)],
                       "Number of COVID-19 confirmed deaths registered to date", "line"],
        }
        return plots_info

    def create_visualization(self):
        plot_titles = self.get_plots_info()
        plt.close("all")
        plot_data = pd.read_csv(self.plot_path)


        sns.despine()
        plt.show()

    def create_nhs_24_and_ambulance_attendances_plot(self):
        plot_data = pd.read_csv(self.plot_path)
        dates = plot_data["Date"].tolist()
        weekly_dates = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[0])
        ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[1])
        ax.set_title(self.plot_title)
        ax.yaxis.grid(True)
        ax.legend([self.plot_y_values[0], self.plot_y_values[1]])
        ax.set_xticks(weekly_dates)
        ax.set_xticklabels(weekly_dates, rotation="vertical")
        ax.set_yticks(self.plot_yticks)
        ax.set_ylabel(self.plot_ylabel)
        sns.despine(top=True, right=True)
        plt.show()

    def create_hospital_care_plot(self):
        plot_data = pd.read_csv(self.plot_path)
        plot_data = plot_data.iloc[9:]
        dates = plot_data["Date"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        ax = sns.barplot(data=plot_data, x="Date", y=self.plot_y_values)
        ax.set_title(self.plot_title)
        ax.yaxis.grid(True)
        ax.set_xticks(range(len(weekly_dates)))
        ax.set_xticklabels(weekly_dates, rotation="vertical")
        ax.set_yticks(self.plot_yticks)
        ax.set_ylabel(self.plot_ylabel)
        sns.despine(top=True, right=True)
        plt.show()

    def create_ambulance_to_hospital_and_delayed_discharges_plot(self):
        plot_data = pd.read_csv(self.plot_path)
        dates = plot_data["Date"].tolist()
        weekly_dates = dates[::7]
        ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values)
        ax.set_title(self.plot_title)
        ax.yaxis.grid(True)
        ax.set_xticks(weekly_dates)
        ax.set_xticklabels(weekly_dates, rotation="vertical")
        ax.set_yticks(self.plot_yticks)
        ax.set_ylabel(self.plot_ylabel)
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
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv")
        dates = plot_data["Date notified"].tolist()
        dates[1::2] = ["" for date in dates[1::2]]
        people_tested_positive = plot_data["(i) Positive"].tolist()
        people_tested_negative = plot_data["(i) Negative"].tolist()
        ax = plt.subplot()
        plt.bar(range(len(dates)), people_tested_positive)
        plt.bar(range(len(dates)), people_tested_negative, bottom=people_tested_positive)
        plt.title("Number of people tested for COVID-19 in Scotland to date, by results")
        plt.legend(["Positive", "Negative"])
        plt.ylabel("Number of people tested")
        ax.set_xticks(range(len(dates)))
        ax.set_xticklabels(dates, rotation="vertical")
        ax.set_yticks([y * 50000 for y in range(1, 8)])
        sns.despine(top=True, right=True)
        plt.show()

    def create_number_of_tests_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv")
        plot_data = plot_data.iloc[30:]
        dates = plot_data["Date notified"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        number_of_tests_nhs_labs = plot_data["(iii) Cumulative"].tolist()
        number_of_tests_regional_testing_centres = plot_data["(iv) Cumulative"].tolist()
        ax = plt.subplot()
        plt.bar(range(len(dates)), number_of_tests_nhs_labs)
        plt.bar(range(len(dates)), number_of_tests_regional_testing_centres, bottom=number_of_tests_nhs_labs)
        plt.title("Cumulative number of COVID-19 Tests carried out in Scotland")
        plt.legend(["NHS Labs", "Regional Testing Centres"])
        plt.ylabel("Number of tests")
        ax.set_xticks(range(len(weekly_dates)))
        ax.set_xticklabels(weekly_dates, rotation="45")
        ax.set_yticks([y * 100000 for y in range(1, 8)])
        sns.despine(top=True, right=True)
        plt.show()

    def create_daily_positive_cases_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv")
        dates = plot_data["Date notified"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        daily_positive_cases = plot_data["(ii) Daily"].tolist()
        weekly_positive_cases = [daily_positive_cases[x:x + 7] for x in range(0, len(daily_positive_cases), 7)]
        weekly_positive_cases_average = [np.average(x) for x in weekly_positive_cases]
        plt.subplot(1, 2, 1)
        ax = sns.barplot(data=plot_data, x="Date notified", y="(ii) Daily")
        ax.set_title("Number of daily new positive cases and 7-day rolling average")
        ax.yaxis.grid(True)
        ax.set_xticks(range(len(weekly_dates)))
        ax.set_xticklabels(weekly_dates, rotation="45")
        ax.set_yticks([y * 50 for y in range(1, 11)])
        ax.set_ylabel("Number of cases")
        sns.despine(top=True, right=True)
        plt.subplot(1, 2, 2)
        ax = sns.lineplot(x=dates[::7], y=weekly_positive_cases_average)
        ax.set_title("Number of daily new positive cases and 7-day rolling average")
        ax.yaxis.grid(True)
        ax.legend(["7 day average"])
        ax.set_xticks(dates[::7])
        ax.set_xticklabels(dates[::7], rotation="45")
        ax.set_yticks([y * 50 for y in range(1, 11)])
        ax.set_ylabel("Number of cases")
        sns.despine(top=True, right=True)
        plt.show()

    def create_workforce_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 6 - Workforce.csv")
        dates = plot_data["Date"].tolist()
        weekly_dates = dates[::7]
        absences = plot_data.columns.tolist()
        workforce_absences_average = []
        for i in range(1, len(absences)):
            staff_absences = plot_data[absences[i]].tolist()
            weekly_staff_absences = [staff_absences[x:x + 7] for x in range(0, len(staff_absences), 7)]
            weekly_staff_absences_average = [np.average(x) for x in weekly_staff_absences]
            workforce_absences_average.append(weekly_staff_absences_average)
        nursing_and_midwifery_absences_average = workforce_absences_average[0]
        medical_and_dental_staff_absences_average = workforce_absences_average[1]
        other_staff_absences_average = workforce_absences_average[2]
        other_staff_absences_average_bottom = np.add(nursing_and_midwifery_absences_average,
                                                     medical_and_dental_staff_absences_average)
        ax = plt.subplot()
        ax.yaxis.grid(True)
        plt.bar(range(len(weekly_dates)), nursing_and_midwifery_absences_average)
        plt.bar(range(len(weekly_dates)), medical_and_dental_staff_absences_average,
                bottom=nursing_and_midwifery_absences_average)
        plt.bar(range(len(weekly_dates)), other_staff_absences_average, bottom=other_staff_absences_average_bottom)
        plt.title("Number of NHS staff reporting as absent due to Covid-19")
        plt.legend([absences[1], absences[2], absences[3]])
        plt.ylabel("Number of staff")
        ax.set_xticks(range(len(weekly_dates)))
        ax.set_xticklabels(weekly_dates, rotation="45")
        ax.set_yticks([y * 1000 for y in range(1, 11)])
        sns.despine(top=True, right=True)
        plt.show()

    def create_care_homes_plot(self):
        plot_data = pd.read_csv("../Trends in daily COVID-19 data 22 July 2020/Table 7a - Care Homes.csv")
        dates = plot_data["Date"].tolist()
        x_values = [""] * len(dates)
        x_values[::2] = dates[::2]
        care_homes_key = "Daily number of new suspected COVID-19 cases in adult care homes"
        care_homes_cases = plot_data[care_homes_key].tolist()
        weekly_care_home_cases = [care_homes_cases[x:x + 7] for x in range(0, len(care_homes_cases), 7)]
        weekly_care_home_cases_average = [np.average(x) for x in weekly_care_home_cases]
        plt.subplot(1, 2, 1)
        ax = sns.barplot(data=plot_data, x="Date", y=care_homes_key)
        ax.set_title("Daily number of new suspected Covid-19 cases reported in Scottish adult care homes")
        ax.yaxis.grid(True)
        ax.set_xticks(range(len(x_values)))
        ax.set_xticklabels(x_values, rotation="45")
        ax.set_yticks([y * 50 for y in range(1, 6)])
        ax.set_ylabel("Number of cases")
        sns.despine(top=True, right=True)
        plt.subplot(1, 2, 2)
        ax = sns.lineplot(x=dates[::7], y=weekly_care_home_cases_average)
        ax.set_title("Daily number of new suspected Covid-19 cases reported in Scottish adult care homes")
        ax.yaxis.grid(True)
        ax.legend(["7 day average"])
        ax.set_xticks(dates[::7])
        ax.set_xticklabels(dates[::7], rotation="45")
        ax.set_yticks([y * 50 for y in range(1, 6)])
        ax.set_ylabel("Number of cases")
        sns.despine(top=True, right=True)
        plt.show()

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


TrendsInDailyDataPlots(1,2,3,4,5,6)














