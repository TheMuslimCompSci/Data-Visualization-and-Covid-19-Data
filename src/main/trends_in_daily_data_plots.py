import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from src.main.plots import Plots


"""TrendsInDailyPlots is one of 3 child classes of Plots. It builds and displays the visualizations for each dataset.
"""


class TrendsInDailyDataPlots(Plots):

    def __init__(self, plots_path=None, plots_title=None, plots_ylabel=None, plots_yticks=None, plots_y_values=None,
                 plots_type=None, plots_types_list=None, plots_axis_column_index=None):
        self.plots_path = plots_path
        self.plots_title = plots_title
        self.plots_ylabel = plots_ylabel
        self.plots_yticks = plots_yticks
        self.plots_y_values = plots_y_values
        self.plots_type = plots_type
        self.plots_types_list = plots_types_list
        self.plots_axis_column_index = plots_axis_column_index

    # Get iterable with information for each plot: file path, title, y axis label, ticks and values, type, available
    # types and the column in dataset with the plot data.
    @staticmethod
    def get_plots_info():
        plots_info = {
            "NHS 24": ["../Trends in daily COVID-19 data 22 July 2020/Table 1 - NHS 24.csv",
                       "Daily number of calls to NHS24 111 and the Coronavirus helpline",
                       "Number of calls", [y * 2000 for y in range(1, 8)],
                       ["NHS24 111 Calls", "Coronavirus Helpline Calls"], "line",
                       ["default", "kde", "box", "violin", "histogram"], "Coronavirus Helpline Calls"],

            "Hospital Confirmed": ["../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                   "Daily number of confirmed COVID-19 patients in hospital",
                                   "Number of patients", [y * 200 for y in range(1, 9)],
                                   "(ii) Confirmed", "bar",
                                   ["default", "kde", "box", "violin", "histogram"], "(ii) Confirmed"],

            "Hospital Care (ICU)": ["../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                    "Daily number of confirmed COVID-19 patients in ICU or combined ICU/HDU",
                                    "Number of patients", [y * 50 for y in range(1, 6)],
                                    "(i) Confirmed", "bar",
                                    ["default", "kde", "box", "violin", "histogram"], "(i) Confirmed"],

            "Ambulance Attendances": ["../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of Attendances (total and COVID-19 suspected)",
                                      "Number of attendances", [y * 200 for y in range(1, 11)],
                                      ["Number of attendances", "Number of COVID-19 suspected attendances"], "line",
                                      ["default", "kde", "box", "violin", "histogram"],
                                      "Number of COVID-19 suspected attendances"],

            "Ambulance To Hospital": ["../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of suspected COVID-19 patients taken to hospital by ambulance",
                                      "Number of patients", [y * 50 for y in range(1, 9)],
                                      "Number of suspected COVID-19 patients taken to hospital", "line",
                                      ["default", "kde", "box", "violin", "histogram"],
                                      "Number of suspected COVID-19 patients taken to hospital"],

            "Delayed Discharges": ["../Trends in daily COVID-19 data 22 July 2020/Table 4 - Delayed Discharges.csv",
                                   "Daily Delayed Discharges",
                                   "Number of delayed discharges", [y * 200 for y in range(1, 10)],
                                   "Number of delayed discharges", "line",
                                   ["default", "kde", "box", "violin", "histogram"], "Number of delayed discharges"],

            "People Tested": ["../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                              "Number of people tested for COVID-19 in Scotland to date, by results",
                              "Number of people tested", [y * 50000 for y in range(1, 8)],
                              ["(i) Positive", "(i) Negative"], "bar",
                              ["default", "kde", "box", "violin", "histogram"], "(i) Positive"],

            "Number Of Tests": ["../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                                "Cumulative number of COVID-19 Tests carried out in Scotland",
                                "Number of tests", [y * 100000 for y in range(1, 8)],
                                ["(iii) Cumulative", "(iv) Cumulative"], "bar",
                                ["default", "kde", "box", "violin", "histogram"], "(iii) Cumulative"],

            "Daily Positive Cases": ["../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                                     "Number of daily new positive cases and 7-day rolling average",
                                     "Number of cases", [y * 50 for y in range(1, 11)],
                                     "(ii) Daily", "bar",
                                     ["default", "kde", "box", "violin", "histogram"], "(ii) Daily"],

            "Workforce": ["../Trends in daily COVID-19 data 22 July 2020/Table 6 - Workforce.csv",
                          "Number of NHS staff reporting as absent due to Covid-19",
                          "Number of staff", [y * 1000 for y in range(1, 11)],
                          "", "bar",
                          ["default", "kde", "box", "violin", "histogram"], "All staff absences"],

            "Care Homes": ["../Trends in daily COVID-19 data 22 July 2020/Table 7a - Care Homes.csv",
                           "Daily number of new suspected Covid-19 cases reported in Scottish adult care homes",
                           "Number of cases", [y * 50 for y in range(1, 6)],
                           "Daily number of new suspected COVID-19 cases in adult care homes", "bar",
                           ["default", "kde", "box", "violin", "histogram"],
                           "Daily number of new suspected COVID-19 cases in adult care homes"],

            "Deaths": ["../Trends in daily COVID-19 data 22 July 2020/Table 8 - Deaths.csv",
                       "Number of COVID-19 confirmed deaths registered to date",
                       "Number of deaths", [y * 500 for y in range(1, 7)],
                       "Number of COVID-19 confirmed deaths registered to date", "line",
                       ["default", "kde", "box", "violin", "histogram"],
                       "Number of COVID-19 confirmed deaths registered to date"],
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
        # Invoke plotting method corresponding to given plot information.
        if self.plots_ylabel == plots_titles["Care Homes"][2]:
            if self.plots_title == plots_titles["Daily Positive Cases"][1]:
                ax = self.create_daily_positive_cases_plot(plots_data, plots_type)
            elif self.plots_title == plots_titles["Care Homes"][1]:
                ax = self.create_care_homes_plot(plots_data, plots_type)
        else:
            if self.plots_ylabel == plots_titles["People Tested"][2] \
                    or self.plots_ylabel == plots_titles["Workforce"][2]:
                if self.plots_title == plots_titles["People Tested"][1]:
                    ax = self.create_people_tested_plot(plots_data, plots_type)
                elif self.plots_title == plots_titles["Workforce"][1]:
                    ax = self.create_workforce_plot(plots_data, plots_type)
            else:
                if self.plots_title == plots_titles["NHS 24"][1] \
                        or self.plots_title == plots_titles["Ambulance Attendances"][1]:
                    plot = self.create_double_variable_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                if self.plots_title == plots_titles["Hospital Confirmed"][1] \
                        or self.plots_title == plots_titles["Hospital Care (ICU)"][1]:
                    plot = self.create_hospital_care_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plots_title == plots_titles["Ambulance To Hospital"][1] \
                        or self.plots_title == plots_titles["Delayed Discharges"][1] \
                        or self.plots_title == plots_titles["Deaths"][1]:
                    plot = self.create_single_variable_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                elif self.plots_title == plots_titles["Number Of Tests"][1]:
                    plot = self.create_number_of_tests_plot(plots_data, plots_type)
                    ax = plot[0]
                    dates = plot[1]
                if self.plots_type == "line":
                    weekly_dates = dates[::7]
                    if plots_type == "default":
                        ax.set_xticks(weekly_dates)
                        ax.set_xticklabels(weekly_dates, rotation="vertical")
                        pass
                elif self.plots_type == "bar":
                    weekly_dates = [""] * len(dates)
                    weekly_dates[::7] = dates[::7]
                    if plots_type == "default":
                        ax.set_xticks(range(len(weekly_dates)))
                        ax.set_xticklabels(weekly_dates, rotation="45")
            ax.set_title(self.plots_title)
            if plots_type == "default":
                self.format_plots_axis(ax)
            ax.yaxis.grid(True)
            sns.despine(top=True, right=True)
        plt.show()

    # Configure labels, ticks, grid and spine of plot axis.
    def format_plots_axis(self, plot):
        plot.set_yticks(self.plots_yticks)
        plot.set_ylabel(self.plots_ylabel)
        plot.yaxis.grid(True)
        sns.despine(top=True, right=True)

    # Build visualization for univariate data.
    def create_single_variable_plot(self, plots_data, plots_type):
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

    # Build visualization for bivariate data.
    def create_double_variable_plot(self, plots_data, plots_type):
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
            ax.legend([self.plots_y_values[0], self.plots_y_values[1]])
        else:
            rows = len(dates)
            data = pd.DataFrame({
                "label": [self.plots_y_values[0]] * rows + [self.plots_y_values[1]] * rows,
                "value": np.concatenate([plots_data[self.plots_y_values[0]], plots_data[self.plots_y_values[1]]])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=data, x="label", y="value")
            elif plots_type == "violin":
                ax = sns.violinplot(data=data, x="label", y="value")
            ax.set_ylabel(self.plots_ylabel)
            ax.set_xlabel("Calls")
        plot = [ax, dates]
        return plot

    # Build visualization for Hospital Care datasets.
    def create_hospital_care_plot(self, plots_data, plots_type):
        confirmed_patients = plots_data.iloc[9:]
        dates = confirmed_patients["Date"].tolist()
        ax = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            ax = sns.barplot(data=confirmed_patients, x="Date", y=self.plots_y_values)
        elif plots_type == "kde" or plots_type == "histogram":
            if plots_type == "kde":
                ax = sns.kdeplot(data=confirmed_patients[self.plots_y_values], shade=True)
            if plots_type == "histogram":
                ax = sns.histplot(data=confirmed_patients[self.plots_y_values])
            ax.set_xlabel(self.plots_ylabel)
        else:
            rows = len(confirmed_patients)
            hospital_care_data = pd.DataFrame({
                "label": [self.plots_y_values] * rows,
                "value": np.concatenate([confirmed_patients[self.plots_y_values]])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=hospital_care_data, x="value", y="label")
            elif plots_type == "violin":
                ax = sns.violinplot(data=hospital_care_data, x="value", y="label")
            ax.set_xlabel(self.plots_ylabel)
            ax.set_ylabel("")
            ax.axes.yaxis.set_ticks([])
        plot = [ax, dates]
        return plot

    # Build visualization for People Tested dataset.
    def create_people_tested_plot(self, plots_data, plots_type):
        dates = plots_data["Date notified"].tolist()
        dates[1::2] = ["" for date in dates[1::2]]
        people_tested_positive = plots_data[self.plots_y_values[0]].tolist()
        people_tested_negative = plots_data[self.plots_y_values[1]].tolist()
        plot = plt.subplot()
        ax = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                plt.bar(range(len(dates)), people_tested_positive)
                plt.bar(range(len(dates)), people_tested_negative, bottom=people_tested_positive)
                plot.set_xticks(range(len(dates)))
                plot.set_xticklabels(dates, rotation="vertical")
            elif plots_type == "kde":
                ax = sns.kdeplot(data=people_tested_positive, shade=True)
                ax = sns.kdeplot(data=people_tested_negative, shade=True)
                ax.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                ax = sns.histplot(data=people_tested_positive)
                ax = sns.histplot(data=people_tested_negative)
                ax.set_xlabel(self.plots_ylabel)
            plt.legend(["Positive", "Negative"])
        else:
            rows = len(dates)
            people_tested_data = pd.DataFrame({
                "label": ["Positive"] * rows + ["Negative"] * rows,
                "value": np.concatenate([people_tested_positive, people_tested_negative])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=people_tested_data, x="label", y="value")
            elif plots_type == "violin":
                ax = sns.violinplot(data=people_tested_data, x="label", y="value")
            ax.set_ylabel(self.plots_ylabel)
            ax.set_xlabel("Result")
        return plot

    # Build visualization for Number Of Tests dataset.
    def create_number_of_tests_plot(self, plots_data, plots_type):
        number_of_tests = plots_data.iloc[30:]
        dates = number_of_tests["Date notified"].tolist()
        number_of_tests_nhs_labs = number_of_tests[self.plots_y_values[0]].tolist()
        number_of_tests_regional_testing_centres = number_of_tests[self.plots_y_values[1]].tolist()
        ax = plt.subplot()
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                plt.bar(range(len(dates)), number_of_tests_nhs_labs)
                plt.bar(range(len(dates)), number_of_tests_regional_testing_centres, bottom=number_of_tests_nhs_labs)
            elif plots_type == "kde":
                ax = sns.kdeplot(data=number_of_tests_nhs_labs, shade=True)
                ax = sns.kdeplot(data=number_of_tests_regional_testing_centres, shade=True)
                ax.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                ax = sns.histplot(data=number_of_tests_nhs_labs)
                ax = sns.histplot(data=number_of_tests_regional_testing_centres)
                ax.set_xlabel(self.plots_ylabel)
            plt.legend(["NHS Labs", "Regional Testing Centres"])
        else:
            rows = len(dates)
            number_of_tests_data = pd.DataFrame({
                "label": ["NHS Labs"] * rows + ["Regional Testing Centres"] * rows,
                "value": np.concatenate([number_of_tests_nhs_labs, number_of_tests_regional_testing_centres])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=number_of_tests_data, x="label", y="value")
            elif plots_type == "violin":
                ax = sns.violinplot(data=number_of_tests_data, x="label", y="value")
            ax.set_ylabel(self.plots_ylabel)
            ax.set_xlabel("Location")
        plot = [ax, dates]
        return plot

    # Build visualization for Daily Positive Cases dataset.
    def create_daily_positive_cases_plot(self, plots_data, plots_type):
        dates = plots_data["Date notified"].tolist()
        weekly_dates = [""] * len(dates)
        weekly_dates[::7] = dates[::7]
        daily_positive_cases = plots_data[self.plots_y_values].tolist()
        weekly_positive_cases = [daily_positive_cases[x:x + 7] for x in range(0, len(daily_positive_cases), 7)]
        weekly_positive_cases_average = [np.average(x) for x in weekly_positive_cases]
        plot = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            f, ax = plt.subplots(figsize=(25, 15))
            plt.subplot(1, 2, 1)
            plot = sns.barplot(data=plots_data, x="Date notified", y=self.plots_y_values)
            plot.set_xticks(range(len(weekly_dates)))
            plot.set_xticklabels(weekly_dates, rotation="45")
            self.format_plots_axis(plot)
            plt.subplot(1, 2, 2)
            plot = sns.lineplot(x=dates[::7], y=weekly_positive_cases_average)
            plot.legend(["7 day average"])
            plot.set_xticks(dates[::7])
            plot.set_xticklabels(dates[::7], rotation="45")
            self.format_plots_axis(plot)
            f.suptitle(self.plots_title)
        else:
            if plots_type == "kde" or plots_type == "histogram":
                if plots_type == "kde":
                    plot = sns.kdeplot(data=plots_data[self.plots_y_values], shade=True)
                elif plots_type == "histogram":
                    plot = sns.histplot(data=plots_data[self.plots_y_values])
                plot.set_xlabel(self.plots_ylabel)
            else:
                if plots_type == "box":
                    plot = sns.boxplot(data=plots_data[self.plots_y_values])
                elif plots_type == "violin":
                    plot = sns.violinplot(data=plots_data[self.plots_y_values])
                plot.axes.xaxis.set_ticks([])
                plot.set_ylabel(self.plots_ylabel)
            plot.set_title("Number of daily new positive cases")
            plot.yaxis.grid(True)
            sns.despine(top=True, right=True)
        return plot

    # Build visualization for Workforce dataset.
    def create_workforce_plot(self, plots_data, plots_type):
        dates = plots_data["Date"].tolist()
        weekly_dates = dates[::7]
        absences = plots_data.columns.tolist()
        workforce_absences_average = []
        # Calculate weekly averages for all staff absences data.
        for i in range(1, len(absences)):
            staff_absences = plots_data[absences[i]].tolist()
            weekly_staff_absences = [staff_absences[x:x + 7] for x in range(0, len(staff_absences), 7)]
            weekly_staff_absences_average = [np.average(x) for x in weekly_staff_absences]
            workforce_absences_average.append(weekly_staff_absences_average)
        nursing_and_midwifery_absences_average = workforce_absences_average[0]
        medical_and_dental_staff_absences_average = workforce_absences_average[1]
        other_staff_absences_average = workforce_absences_average[2]
        other_staff_absences_average_bottom = np.add(nursing_and_midwifery_absences_average,
                                                     medical_and_dental_staff_absences_average)
        plot = plt.subplot()
        ax = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default" or plots_type == "kde" or plots_type == "histogram":
            if plots_type == "default":
                plt.bar(range(len(weekly_dates)), nursing_and_midwifery_absences_average)
                plt.bar(range(len(weekly_dates)), medical_and_dental_staff_absences_average,
                        bottom=nursing_and_midwifery_absences_average)
                plt.bar(range(len(weekly_dates)), other_staff_absences_average,
                        bottom=other_staff_absences_average_bottom)
                plot.set_xticks(range(len(weekly_dates)))
                plot.set_xticklabels(weekly_dates, rotation="45")
            elif plots_type == "kde":
                ax = sns.kdeplot(data=nursing_and_midwifery_absences_average, shade=True)
                ax = sns.kdeplot(data=medical_and_dental_staff_absences_average, shade=True)
                ax = sns.kdeplot(data=other_staff_absences_average, shade=True)
                ax.set_xlabel(self.plots_ylabel)
            elif plots_type == "histogram":
                ax = sns.histplot(data=nursing_and_midwifery_absences_average)
                ax = sns.histplot(data=medical_and_dental_staff_absences_average)
                ax = sns.histplot(data=other_staff_absences_average)
                ax.set_xlabel(self.plots_ylabel)
            plt.legend([absences[1], absences[2], absences[3]])
        else:
            rows = len(nursing_and_midwifery_absences_average)
            workforce_data = pd.DataFrame({
                "label": [absences[1]] * rows + [absences[2]] * rows + [absences[3]] * rows,
                "value": np.concatenate([nursing_and_midwifery_absences_average,
                                         medical_and_dental_staff_absences_average,
                                         other_staff_absences_average])
            })
            if plots_type == "box":
                ax = sns.boxplot(data=workforce_data, x="label", y="value")
            elif plots_type == "violin":
                ax = sns.violinplot(data=workforce_data, x="label", y="value")
            ax.set_ylabel(self.plots_ylabel)
            ax.set_xlabel("Staff")
        return plot

    # Build visualization for Care Homes dataset.
    def create_care_homes_plot(self, plots_data, plots_type):
        dates = plots_data["Date"].tolist()
        x_values = [""] * len(dates)
        x_values[::2] = dates[::2]
        care_homes_key = "Daily number of new suspected COVID-19 cases in adult care homes"
        care_homes_cases = plots_data[care_homes_key].tolist()
        weekly_care_home_cases = [care_homes_cases[x:x + 7] for x in range(0, len(care_homes_cases), 7)]
        weekly_care_home_cases_average = [np.average(x) for x in weekly_care_home_cases]
        plot = None
        # Invoke plotting method corresponding to given plot type.
        if plots_type == "default":
            f, ax = plt.subplots(figsize=(25, 15))
            plt.subplot(1, 2, 1)
            plot = sns.barplot(data=plots_data, x="Date", y=care_homes_key)
            plot.set_xticks(range(len(x_values)))
            plot.set_xticklabels(x_values, rotation="45")
            self.format_plots_axis(plot)
            plt.subplot(1, 2, 2)
            plot = sns.lineplot(x=dates[::7], y=weekly_care_home_cases_average)
            plot.legend(["7 day average"])
            plot.set_xticks(dates[::7])
            plot.set_xticklabels(dates[::7], rotation="45")
            self.format_plots_axis(plot)
            f.suptitle(self.plots_title)
        else:
            if plots_type == "kde" or plots_type == "histogram":
                if plots_type == "kde":
                    plot = sns.kdeplot(data=plots_data[self.plots_y_values], shade=True)
                elif plots_type == "histogram":
                    plot = sns.histplot(data=plots_data[self.plots_y_values])
                plot.set_xlabel(self.plots_ylabel)
            else:
                if plots_type == "box":
                    plot = sns.boxplot(data=plots_data[self.plots_y_values])
                elif plots_type == "violin":
                    plot = sns.violinplot(data=plots_data[self.plots_y_values])
                plot.axes.xaxis.set_ticks([])
                plot.set_ylabel(self.plots_ylabel)
            plot.set_title("Daily number of new suspected Covid-19 cases reported in Scottish adult care homes")
            plot.yaxis.grid(True)
            sns.despine(top=True, right=True)
        return plot
