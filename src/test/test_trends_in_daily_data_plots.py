import unittest
import pandas as pd
from src.main.trends_in_daily_data_plots import TrendsInDailyDataPlots


class TestTrendsInDailyDataPlots(unittest.TestCase):

    def setUp(self):
        self.trends_in_daily_data_plots = TrendsInDailyDataPlots("test_plots.py", "test title", "test y label",
                                                                 range(5), "test y values", "test type",
                                                                 ["bar", "box", "histogram", "kde", "line", "pie",
                                                                  "violin"], 5)
        self.expected_plots_info = {
            "NHS 24": ["../../Trends in daily COVID-19 data 22 July 2020/Table 1 - NHS 24.csv",
                       "Daily number of calls to NHS24 111 and the Coronavirus helpline",
                       "Number of calls", [y * 2000 for y in range(1, 8)],
                       ["NHS24 111 Calls", "Coronavirus Helpline Calls"], "line",
                       ["default", "kde", "box", "violin", "histogram"], "Coronavirus Helpline Calls"],

            "Hospital Confirmed": ["../../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                   "Daily number of confirmed COVID-19 patients in hospital",
                                   "Number of patients", [y * 200 for y in range(1, 9)],
                                   "(ii) Confirmed", "bar",
                                   ["default", "kde", "box", "violin", "histogram"], "(ii) Confirmed"],

            "Hospital Care (ICU)": ["../../Trends in daily COVID-19 data 22 July 2020/Table 2 - Hospital Care.csv",
                                    "Daily number of confirmed COVID-19 patients in ICU or combined ICU/HDU",
                                    "Number of patients", [y * 50 for y in range(1, 6)],
                                    "(i) Confirmed", "bar",
                                    ["default", "kde", "box", "violin", "histogram"], "(i) Confirmed"],

            "Ambulance Attendances": ["../../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of Attendances (total and COVID-19 suspected)",
                                      "Number of attendances", [y * 200 for y in range(1, 11)],
                                      ["Number of attendances", "Number of COVID-19 suspected attendances"], "line",
                                      ["default", "kde", "box", "violin", "histogram"],
                                      "Number of COVID-19 suspected attendances"],

            "Ambulance To Hospital": ["../../Trends in daily COVID-19 data 22 July 2020/Table 3 - Ambulance.csv",
                                      "Number of suspected COVID-19 patients taken to hospital by ambulance",
                                      "Number of patients", [y * 50 for y in range(1, 9)],
                                      "Number of suspected COVID-19 patients taken to hospital", "line",
                                      ["default", "kde", "box", "violin", "histogram"],
                                      "Number of suspected COVID-19 patients taken to hospital"],

            "Delayed Discharges": ["../../Trends in daily COVID-19 data 22 July 2020/Table 4 - Delayed Discharges.csv",
                                   "Daily Delayed Discharges",
                                   "Number of delayed discharges", [y * 200 for y in range(1, 10)],
                                   "Number of delayed discharges", "line",
                                   ["default", "kde", "box", "violin", "histogram"], "Number of delayed discharges"],

            "People Tested": ["../../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                              "Number of people tested for COVID-19 in Scotland to date, by results",
                              "Number of people tested", [y * 50000 for y in range(1, 8)],
                              ["(i) Positive", "(i) Negative"], "bar",
                              ["default", "kde", "box", "violin", "histogram"], "(i) Positive"],

            "Number Of Tests": ["../../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                                "Cumulative number of COVID-19 Tests carried out in Scotland",
                                "Number of tests", [y * 100000 for y in range(1, 8)],
                                ["(iii) Cumulative", "(iv) Cumulative"], "bar",
                                ["default", "kde", "box", "violin", "histogram"], "(iii) Cumulative"],

            "Daily Positive Cases": ["../../Trends in daily COVID-19 data 22 July 2020/Table 5 - Testing.csv",
                                     "Number of daily new positive cases and 7-day rolling average",
                                     "Number of cases", [y * 50 for y in range(1, 11)],
                                     "(ii) Daily", "bar",
                                     ["default", "kde", "box", "violin", "histogram"], "(ii) Daily"],

            "Workforce": ["../../Trends in daily COVID-19 data 22 July 2020/Table 6 - Workforce.csv",
                          "Number of NHS staff reporting as absent due to Covid-19",
                          "Number of staff", [y * 1000 for y in range(1, 11)],
                          "", "bar",
                          ["default", "kde", "box", "violin", "histogram"], "All staff absences"],

            "Care Homes": ["../../Trends in daily COVID-19 data 22 July 2020/Table 7a - Care Homes.csv",
                           "Daily number of new suspected Covid-19 cases reported in Scottish adult care homes",
                           "Number of cases", [y * 50 for y in range(1, 6)],
                           "Daily number of new suspected COVID-19 cases in adult care homes", "bar",
                           ["default", "kde", "box", "violin", "histogram"],
                           "Daily number of new suspected COVID-19 cases in adult care homes"],

            "Deaths": ["../../Trends in daily COVID-19 data 22 July 2020/Table 8 - Deaths.csv",
                       "Number of COVID-19 confirmed deaths registered to date",
                       "Number of deaths", [y * 500 for y in range(1, 7)],
                       "Number of COVID-19 confirmed deaths registered to date", "line",
                       ["default", "kde", "box", "violin", "histogram"],
                       "Number of COVID-19 confirmed deaths registered to date"],
        }

    # Check that method passes when class is initialised correctly.
    def test_init(self):
        self.assertIs(type(self.trends_in_daily_data_plots), TrendsInDailyDataPlots)
        self.assertEqual(self.trends_in_daily_data_plots.plots_path, "test_plots.py")
        self.assertEqual(self.trends_in_daily_data_plots.plots_title, "test title")
        self.assertEqual(self.trends_in_daily_data_plots.plots_ylabel, "test y label")
        self.assertEqual(self.trends_in_daily_data_plots.plots_yticks, range(5))
        self.assertEqual(self.trends_in_daily_data_plots.plots_y_values, "test y values")
        self.assertEqual(self.trends_in_daily_data_plots.plots_type, "test type")
        self.assertEqual(self.trends_in_daily_data_plots.plots_types_list, ["bar", "box", "histogram", "kde", "line",
                                                                            "pie", "violin"])
        self.assertEqual(self.trends_in_daily_data_plots.plots_axis_column_index, 5)

    # Check that method passes when return value equals the expected value.
    def test_get_plots_info(self):
        self.assertEqual(self.trends_in_daily_data_plots.get_plots_info(), self.expected_plots_info)

    # Check that method fails when styling values of arguments are incorrect or if there is an error tokenizing data.
    def test_create_visualization(self):
        with self.assertRaises(ValueError):
            self.trends_in_daily_data_plots.create_visualization("test type", "ticks", "test context", "text palette")
        with self.assertRaises(ValueError):
            self.trends_in_daily_data_plots.create_visualization("test type", "test style", "poster", "text palette")
        with self.assertRaises(ValueError):
            self.trends_in_daily_data_plots.create_visualization("test type", "test style", "test context",
                                                                 "colorblind")
        with self.assertRaises(pd.errors.ParserError):
            self.trends_in_daily_data_plots.create_visualization("test type", "ticks", "poster", "colorblind")

    # Check that method fails when argument object has no Pandas attributes.
    def test_format_plots_axis(self):
        with self.assertRaises(AttributeError):
            self.trends_in_daily_data_plots.format_plots_axis(None)

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_single_variable_plot(self):
        with self.assertRaises(TypeError):
            self.trends_in_daily_data_plots.create_single_variable_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_double_variable_plot(self):
        with self.assertRaises(TypeError):
            self.trends_in_daily_data_plots.create_double_variable_plot(range(10), "test type")

    # Check that method fails when argument object has no Pandas attributes.
    def test_create_hospital_care_plot(self):
        with self.assertRaises(AttributeError):
            self.trends_in_daily_data_plots.create_hospital_care_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_people_tested_plot(self):
        with self.assertRaises(TypeError):
            self.trends_in_daily_data_plots.create_people_tested_plot(range(10), "test type")

    # Check that method fails when argument object has no Pandas attributes.
    def test_create_number_of_tests_plot(self):
        with self.assertRaises(AttributeError):
            self.trends_in_daily_data_plots.create_number_of_tests_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_daily_positive_cases_plot(self):
        with self.assertRaises(TypeError):
            self.trends_in_daily_data_plots.create_daily_positive_cases_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_workforce_plot(self):
        with self.assertRaises(TypeError):
            self.trends_in_daily_data_plots.create_workforce_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_care_homes_plot(self):
        with self.assertRaises(TypeError):
            self.trends_in_daily_data_plots.create_care_homes_plot(range(10), "test type")


if __name__ == "__main__":
    unittest.main()
