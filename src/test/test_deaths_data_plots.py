import sys
sys.path.append("..")

import unittest
import pandas as pd
from main.deaths_data_plots import DeathsDataPlots


class TestDeathsDataPlots(unittest.TestCase):

    def setUp(self):
        self.deaths_data_plots = DeathsDataPlots("test_plots.py", "test title", "test y label", range(10),
                                                 "test y values", ["bar", "box", "histogram", "kde", "line", "pie",
                                                                   "violin"], 3)
        self.expected_plots_info = {
            "Cumulative Deaths": ["../../covid deaths data week 30/Figure 1 data.csv",
                                  "Cumulative number of deaths involving COVID-19 by date of registration, Scotland, 2020",
                                  "Cumulative number of deaths", [y * 500 for y in range(1, 10)], "Count",
                                  ["default", "kde", "box", "violin", "histogram"], "Count"],

            "Cumulative Deaths Different Data": ["../../covid deaths data week 30/Figure 2 data.csv",
                                                 "Cumulative number of deaths involving COVID-19 in Scotland using different data sources 2020",
                                                 "Cumulative number of deaths", [y * 500 for y in range(1, 10)],
                                                 "Cumulative Count",
                                                 ["default", "kde", "box", "violin", "histogram"], "Cumulative Count"],

            "COVID Deaths By Age": ["../../covid deaths data week 30/Figure 3a and 3b data.csv",
                                    "COVID-19 deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                    "Number of deaths", [y * 200 for y in range(1, 11)], "Covid deaths to date",
                                    ["default", "kde", "box", "violin", "histogram", "pie"], "Covid deaths to date"],

            "All Deaths By Age": ["../../covid deaths data week 30/Figure 3a and 3b data.csv",
                                  "All deaths registered between weeks 1 and 30, 2020 by age group, Scotland",
                                  "Number of deaths", [y * 2000 for y in range(1, 8)], "Total deaths to date",
                                  ["default", "kde", "box", "violin", "histogram", "pie"], "Total deaths to date"],

            "Deaths By Board": ["../../covid deaths data week 30/Figure 4 data.csv",
                                "COVID-19 deaths registered between weeks 1 and 30 of 2020, by health board of residence, Scotland",
                                "Number of deaths", [y * 200 for y in range(1, 8)], "COVID-19 deaths to date",
                                ["default", "kde", "box", "violin", "histogram", "pie"], "COVID-19 deaths to date"],

            "Deaths By Week": ["../../covid deaths data week 30/Figure 5 data.csv",
                               "Deaths by week of registration, Scotland, 2020",
                               "Number of deaths", [y * 500 for y in range(1, 6)],
                               ["Total deaths 2020", "Average for previous 5 years", "COVID-19 deaths 2020"],
                               ["default", "kde", "box", "violin", "histogram"], "COVID-19 deaths 2020"],

            "Deaths By Cause": ["../../covid deaths data week 30/Figure 6 data.csv",
                                "Excess Deaths by underlying cause of death and location, week 12 to 30, 2020",
                                "Number of deaths", [y * 5000 for y in range(1, 6)], "",
                                ["default", "pie"], "Hospital"],

            "Deaths By Location": ["../../covid deaths data week 30/Figure 7 data.csv",
                                   "Deaths involving COVID-19 by location of death, weeks 12 to 30, 2020",
                                   "Number of deaths", [y * 50 for y in range(1, 9)], "",
                                   ["default", "kde", "box", "violin", "histogram", "pie"], "week 30"],

            "Deaths By Date Of Death vs Date Of Registration": ["../../covid deaths data week 30/Figure 8 data.csv",
                                                                "Deaths involving COVID-19, date of death vs date of registration",
                                                                "Cumulative number of deaths",
                                                                [y * 500 for y in range(1, 10)],
                                                                ["Cumulative deaths by date of death",
                                                                 "Cumulative deaths by date of registration"],
                                                                ["default", "kde", "box", "violin", "histogram"],
                                                                "Cumulative deaths by date of registration"]
        }

    # Check that method passes when class is initialised correctly.
    def test_init(self):
        self.assertIs(type(self.deaths_data_plots), DeathsDataPlots)
        self.assertEqual(self.deaths_data_plots.plots_path, "test_plots.py")
        self.assertEqual(self.deaths_data_plots.plots_title, "test title")
        self.assertEqual(self.deaths_data_plots.plots_ylabel, "test y label")
        self.assertEqual(self.deaths_data_plots.plots_yticks, range(10))
        self.assertEqual(self.deaths_data_plots.plots_y_values, "test y values")
        self.assertEqual(self.deaths_data_plots.plots_types_list, ["bar", "box", "histogram", "kde", "line", "pie",
                                                                   "violin"])
        self.assertEqual(self.deaths_data_plots.plots_axis_column_index, 3)

    # Check that method passes when return value equals the expected value.
    def test_get_plots_info(self):
        self.assertEqual(self.deaths_data_plots.get_plots_info(), self.expected_plots_info)

    # Check that method fails when styling values of arguments are incorrect or if there is an error tokenizing data.
    def test_create_visualization(self):
        with self.assertRaises(ValueError):
            self.deaths_data_plots.create_visualization("test type", "ticks", "test context", "text palette")
        with self.assertRaises(ValueError):
            self.deaths_data_plots.create_visualization("test type", "test style", "poster", "text palette")
        with self.assertRaises(ValueError):
            self.deaths_data_plots.create_visualization("test type", "test style", "test context", "colorblind")
        with self.assertRaises(pd.errors.ParserError):
            self.deaths_data_plots.create_visualization("test type", "ticks", "poster", "colorblind")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_cumulative_deaths_plot(self):
        with self.assertRaises(TypeError):
            self.deaths_data_plots.create_cumulative_deaths_plot(range(10), "test type")

    # Check that method fails when argument object has no Pandas attributes.
    def test_create_cumulative_deaths_different_data_plot(self):
        with self.assertRaises(AttributeError):
            self.deaths_data_plots.create_cumulative_deaths_different_data_plot(range(10), "test type")

    # Check that method fails when argument object has no Pandas attributes.
    def test_create_deaths_by_age_plot(self):
        with self.assertRaises(AttributeError):
            self.deaths_data_plots.create_deaths_by_age_plot(range(10), "test type")

    # Check that method fails when argument object has no Pandas attributes.
    def test_create_deaths_by_board_plot(self):
        with self.assertRaises(AttributeError):
            self.deaths_data_plots.create_deaths_by_board_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_deaths_by_week_plot(self):
        with self.assertRaises(TypeError):
            self.deaths_data_plots.create_deaths_by_week_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_deaths_by_cause_plot(self):
        with self.assertRaises(TypeError):
            self.deaths_data_plots.create_deaths_by_cause_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_format_deaths_by_cause_data(self):
        with self.assertRaises(TypeError):
            self.deaths_data_plots.format_deaths_by_cause_data(range(10))

    # Check that method fails when argument object has no Pandas attributes.
    def test_format_deaths_by_cause_plot(self):
        with self.assertRaises(AttributeError):
            self.deaths_data_plots.format_deaths_by_cause_plot(1, range(10), range(20), range(30), "test title",
                                                               "test type", range(100))

    # Check that method fails when argument object has no Pandas attributes.
    def test_create_deaths_by_location_plot(self):
        with self.assertRaises(AttributeError):
            self.deaths_data_plots.create_deaths_by_location_plot(range(10), "test type")

    # Check that method fails when argument object range indices are not integers or slices i.e. a string.
    def test_create_deaths_by_dates_plot(self):
        with self.assertRaises(TypeError):
            self.deaths_data_plots.create_deaths_by_dates_plot(range(10), "test type")


if __name__ == "__main__":
    unittest.main()
