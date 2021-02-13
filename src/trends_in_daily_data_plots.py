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

    def create_visualization(self, plot_type):
        plt.close("all")
        plot_data = pd.read_csv(self.plot_path)
        plot_titles = self.get_plots_info()
        if self.plot_ylabel == plot_titles["Care Homes"][2]:
            if self.plot_title == plot_titles["Daily Positive Cases"][1]:
                ax = self.create_daily_positive_cases_plot(plot_data, plot_type)
            elif self.plot_title == plot_titles["Care Homes"][1]:
                ax = self.create_care_homes_plot(plot_data, plot_type)
        else:
            if self.plot_ylabel == plot_titles["People Tested"][2] or self.plot_ylabel == plot_titles["Workforce"][2]:
                if self.plot_title == plot_titles["People Tested"][1]:
                    ax = self.create_people_tested_plot(plot_data, plot_type)
                elif self.plot_title == plot_titles["Workforce"][1]:
                    ax = self.create_workforce_plot(plot_data, plot_type)
            else:
                if self.plot_title == plot_titles["NHS 24"][1] or self.plot_title == plot_titles["Ambulance Attendances"][1]:
                    plot = self.create_double_line_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                if self.plot_title == plot_titles["Hospital Confirmed"][1] or self.plot_title == plot_titles["Hospital Care (ICU)"][1]:
                    plot = self.create_hospital_care_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plot_title == plot_titles["Ambulance To Hospital"][1] or self.plot_title == plot_titles["Delayed Discharges"][1] or self.plot_title == plot_titles["Deaths"][1]:
                    plot = self.create_single_line_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plot_title == plot_titles["Number Of Tests"][1]:
                    plot = self.create_number_of_tests_plot(plot_data, plot_type)
                    ax = plot[0]
                    dates = plot[1]
                if self.plot_type == "line":
                    weekly_dates = dates[::7]
                    if plot_type == "default":
                        ax.set_xticks(weekly_dates)
                        ax.set_xticklabels(weekly_dates, rotation="vertical")
                        pass
                elif self.plot_type == "bar":
                    weekly_dates = [""] * len(dates)
                    weekly_dates[::7] = dates[::7]
                    if plot_type == "default":
                        ax.set_xticks(range(len(weekly_dates)))
                        ax.set_xticklabels(weekly_dates, rotation="45")
            ax.set_title(self.plot_title)
            if plot_type == "default":
                self.format_plot_axis(ax)
            ax.yaxis.grid(True)
            sns.despine(top=True, right=True)
        plt.show()

    def format_plot_axis(self, plot):
        plot.set_yticks(self.plot_yticks)
        plot.set_ylabel(self.plot_ylabel)
        plot.yaxis.grid(True)
        sns.despine(top=True, right=True)

    def create_single_line_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        if plot_type == "default":
            ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values)
        elif plot_type == "kde":
            ax = sns.kdeplot(data=plot_data[self.plot_y_values], shade=True)
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

    def create_double_line_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        if plot_type == "default" or plot_type == "kde":
            if plot_type == "default":
                ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[0])
                ax = sns.lineplot(data=plot_data, x="Date", y=self.plot_y_values[1])
            elif plot_type == "kde":
                ax = sns.kdeplot(data=plot_data[self.plot_y_values[0]], shade=True)
                ax = sns.kdeplot(data=plot_data[self.plot_y_values[1]], shade=True)
                ax.set_xlabel(self.plot_ylabel)
            ax.legend([self.plot_y_values[0], self.plot_y_values[1]])
        else:
            rows = len(dates)
            data = pd.DataFrame({
                "label": [self.plot_y_values[0]] * rows + [self.plot_y_values[1]] * rows,
                "value": np.concatenate([plot_data[self.plot_y_values[0]], plot_data[self.plot_y_values[1]]])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=data, x="label", y="value")
            elif plot_type == "violin":
                ax = sns.violinplot(data=data, x="label", y="value")
            ax.set_ylabel(self.plot_ylabel)
            ax.set_xlabel("Calls")
        plot = [ax, dates]
        return plot

    def create_hospital_care_plot(self, plot_data, plot_type):
        confirmed_patients = plot_data.iloc[9:]
        dates = confirmed_patients["Date"].tolist()
        if plot_type == "default":
            ax = sns.barplot(data=confirmed_patients, x="Date", y=self.plot_y_values)
        elif plot_type == "kde":
            ax = sns.kdeplot(data=confirmed_patients[self.plot_y_values], shade=True)
            ax.set_xlabel(self.plot_ylabel)
        else:
            rows = len(confirmed_patients)
            hospital_care_data = pd.DataFrame({
                "label": [self.plot_y_values] * rows,
                "value": np.concatenate([confirmed_patients[self.plot_y_values]])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=hospital_care_data, x="value", y="label")
            elif plot_type == "violin":
                ax = sns.violinplot(data=hospital_care_data, x="value", y="label")
            ax.set_xlabel(self.plot_ylabel)
            ax.set_ylabel("")
            ax.axes.yaxis.set_ticks([])
        plot = [ax, dates]
        return plot

    def create_people_tested_plot(self, plot_data, plot_type):
        dates = plot_data["Date notified"].tolist()
        dates[1::2] = ["" for date in dates[1::2]]
        people_tested_positive = plot_data[self.plot_y_values[0]].tolist()
        people_tested_negative = plot_data[self.plot_y_values[1]].tolist()
        plot = plt.subplot()
        if plot_type == "default" or plot_type == "kde":
            if plot_type == "default":
                plt.bar(range(len(dates)), people_tested_positive)
                plt.bar(range(len(dates)), people_tested_negative, bottom=people_tested_positive)
                plot.set_xticks(range(len(dates)))
                plot.set_xticklabels(dates, rotation="vertical")
            elif plot_type == "kde":
                ax = sns.kdeplot(data=people_tested_positive, shade=True)
                ax = sns.kdeplot(data=people_tested_negative, shade=True)
                ax.set_xlabel(self.plot_ylabel)
            plt.legend(["Positive", "Negative"])
        else:
            rows = len(dates)
            people_tested_data = pd.DataFrame({
                "label": ["Positive"] * rows + ["Negative"] * rows,
                "value": np.concatenate([people_tested_positive, people_tested_negative])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=people_tested_data, x="label", y="value")
            elif plot_type == "violin":
                ax = sns.violinplot(data=people_tested_data, x="label", y="value")
            ax.set_ylabel(self.plot_ylabel)
            ax.set_xlabel("Result")
        return plot

    def create_number_of_tests_plot(self, plot_data, plot_type):
        number_of_tests = plot_data.iloc[30:]
        dates = number_of_tests["Date notified"].tolist()
        number_of_tests_nhs_labs = number_of_tests[self.plot_y_values[0]].tolist()
        number_of_tests_regional_testing_centres = number_of_tests[self.plot_y_values[1]].tolist()
        ax = plt.subplot()
        if plot_type == "default" or plot_type == "kde":
            if plot_type == "default":
                plt.bar(range(len(dates)), number_of_tests_nhs_labs)
                plt.bar(range(len(dates)), number_of_tests_regional_testing_centres, bottom=number_of_tests_nhs_labs)
            elif plot_type == "kde":
                ax = sns.kdeplot(data=number_of_tests_nhs_labs, shade=True)
                ax = sns.kdeplot(data=number_of_tests_regional_testing_centres, shade=True)
                ax.set_xlabel(self.plot_ylabel)
            plt.legend(["NHS Labs", "Regional Testing Centres"])
        else:
            rows = len(dates)
            number_of_tests_data = pd.DataFrame({
                "label": ["NHS Labs"] * rows + ["Regional Testing Centres"] * rows,
                "value": np.concatenate([number_of_tests_nhs_labs, number_of_tests_regional_testing_centres])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=number_of_tests_data, x="label", y="value")
            elif plot_type == "violin":
                ax = sns.violinplot(data=number_of_tests_data, x="label", y="value")
            ax.set_ylabel(self.plot_ylabel)
            ax.set_xlabel("Location")
        plot = [ax, dates]
        return plot

    def create_daily_positive_cases_plot(self, plot_data, plot_type):
        dates = plot_data["Date notified"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        daily_positive_cases = plot_data[self.plot_y_values].tolist()
        weekly_positive_cases = [daily_positive_cases[x:x + 7] for x in range(0, len(daily_positive_cases), 7)]
        weekly_positive_cases_average = [np.average(x) for x in weekly_positive_cases]
        f, ax = plt.subplots(figsize=(25, 15))
        plt.subplot(1, 2, 1)
        if plot_type == "default":
            plot = sns.barplot(data=plot_data, x="Date notified", y=self.plot_y_values)
        plot.set_xticks(range(len(weekly_dates)))
        plot.set_xticklabels(weekly_dates, rotation="45")
        self.format_plot_axis(plot)
        plt.subplot(1, 2, 2)
        if plot_type == "default":
            plot = sns.lineplot(x=dates[::7], y=weekly_positive_cases_average)
        plot.legend(["7 day average"])
        plot.set_xticks(dates[::7])
        plot.set_xticklabels(dates[::7], rotation="45")
        self.format_plot_axis(plot)
        f.suptitle(self.plot_title)
        return plot

    def create_workforce_plot(self, plot_data, plot_type):
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
        other_staff_absences_average_bottom = np.add(nursing_and_midwifery_absences_average, medical_and_dental_staff_absences_average)
        plot = plt.subplot()
        if plot_type == "default" or plot_type == "kde":
            if plot_type == "default":
                plt.bar(range(len(weekly_dates)), nursing_and_midwifery_absences_average)
                plt.bar(range(len(weekly_dates)), medical_and_dental_staff_absences_average, bottom=nursing_and_midwifery_absences_average)
                plt.bar(range(len(weekly_dates)), other_staff_absences_average, bottom=other_staff_absences_average_bottom)
                plot.set_xticks(range(len(weekly_dates)))
                plot.set_xticklabels(weekly_dates, rotation="45")
            elif plot_type == "kde":
                ax = sns.kdeplot(data=nursing_and_midwifery_absences_average, shade=True)
                ax = sns.kdeplot(data=medical_and_dental_staff_absences_average, shade=True)
                ax = sns.kdeplot(data=other_staff_absences_average, shade=True)
                ax.set_xlabel(self.plot_ylabel)
            plt.legend([absences[1], absences[2], absences[3]])
        else:
            print(len(nursing_and_midwifery_absences_average))
            print(len(medical_and_dental_staff_absences_average))
            print(len(other_staff_absences_average))
            rows = len(nursing_and_midwifery_absences_average)
            workforce_data = pd.DataFrame({
                "label": [absences[1]] * rows + [absences[2]] * rows + [absences[3]] * rows,
                "value": np.concatenate([nursing_and_midwifery_absences_average,
                                         medical_and_dental_staff_absences_average,
                                         other_staff_absences_average])
            })
            if plot_type == "box":
                ax = sns.boxplot(data=workforce_data, x="label", y="value")
            elif plot_type == "violin":
                ax = sns.violinplot(data=workforce_data, x="label", y="value")
            ax.set_ylabel(self.plot_ylabel)
            ax.set_xlabel("Staff")
        return plot

    def create_care_homes_plot(self, plot_data, plot_type):
        dates = plot_data["Date"].tolist()
        x_values = [""] * len(dates)
        x_values[::2] = dates[::2]
        care_homes_key = "Daily number of new suspected COVID-19 cases in adult care homes"
        care_homes_cases = plot_data[care_homes_key].tolist()
        weekly_care_home_cases = [care_homes_cases[x:x + 7] for x in range(0, len(care_homes_cases), 7)]
        weekly_care_home_cases_average = [np.average(x) for x in weekly_care_home_cases]
        f, ax = plt.subplots(figsize=(25, 15))
        plt.subplot(1, 2, 1)
        if plot_type == "default":
            plot = sns.barplot(data=plot_data, x="Date", y=care_homes_key)
        plot.set_xticks(range(len(x_values)))
        plot.set_xticklabels(x_values, rotation="45")
        self.format_plot_axis(plot)
        plt.subplot(1, 2, 2)
        if plot_type == "default":
            plot = sns.lineplot(x=dates[::7], y=weekly_care_home_cases_average)
        plot.legend(["7 day average"])
        plot.set_xticks(dates[::7])
        plot.set_xticklabels(dates[::7], rotation="45")
        self.format_plot_axis(plot)
        f.suptitle(self.plot_title)
        return plot

    def get_plots_title(self):
        return self.plot_title

    def get_plots_data(self):
        plots_data = pd.read_csv(self.plot_path)
        return plots_data

    def get_plots_axis_column_index(self):
        plots_data = pd.read_csv(self.plot_path)
        plots_info = self.get_plots_info()
        if self.plot_path == plots_info["NHS 24"][0]:
            return plots_data.columns.get_loc("Coronavirus Helpline Calls")
        elif self.plot_path == plots_info["Hospital Confirmed"][0]:
            if self.plot_y_values == plots_info["Hospital Confirmed"][4]:
                return plots_data.columns.get_loc("(ii) Confirmed")
            elif self.plot_y_values == plots_info["Hospital Care (ICU)"][4]:
                return plots_data.columns.get_loc("(i) Confirmed")
        elif self.plot_path == plots_info["Ambulance Attendances"][0]:
            if self.plot_y_values == plots_info["Ambulance Attendances"][4]:
                return plots_data.columns.get_loc("Number of COVID-19 suspected attendances")
            elif self.plot_y_values == plots_info["Ambulance To Hospital"][4]:
                return plots_data.columns.get_loc("Number of suspected COVID-19 patients taken to hospital")
        elif self.plot_path == plots_info["Delayed Discharges"][0]:
            return plots_data.columns.get_loc("Number of delayed discharges")
        elif self.plot_path == plots_info["People Tested"][0]:
            if self.plot_y_values == plots_info["People Tested"][4]:
                return plots_data.columns.get_loc("(i) Positive")
            elif self.plot_y_values == plots_info["Number Of Tests"][4]:
                return plots_data.columns.get_loc("(iii) Cumulative")
            elif self.plot_y_values == plots_info["Daily Positive Cases"][4]:
                return plots_data.columns.get_loc("(ii) Daily")
            return plots_data.columns.get_loc("(i) Positive")
        elif self.plot_path == plots_info["Workforce"][0]:
            return plots_data.columns.get_loc("All staff absences")
        elif self.plot_path == plots_info["Care Homes"][0]:
            return plots_data.columns.get_loc("Daily number of new suspected COVID-19 cases in adult care homes")
        elif self.plot_path == plots_info["Deaths"][0]:
            return plots_data.columns.get_loc("Number of COVID-19 confirmed deaths registered to date")

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
