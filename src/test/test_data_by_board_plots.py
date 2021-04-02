import sys
sys.path.append("..")

import unittest
import pandas as pd
from main.data_by_board_plots import DataByBoardPlots


class TestDataByBoardPlots(unittest.TestCase):

    def setUp(self):
        self.data_by_board_plots = DataByBoardPlots("test_plots.py", "test title", "test y label", range(10),
                                                    ["bar", "box", "histogram", "kde", "line", "pie", "violin"], 2)
        self.expected_plots_info = {
            "Cumulative Cases": ["../../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv",
                                 "The cumulative number of cases with positive tests for COVID-19, by board in Scotland, 07/03/2020-22/07/2020",
                                 "Cumulative Cases", [y * 2000 for y in range(1, 10)],
                                 ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "ICU Patients Confirmed": ["../../COVID-19 data by NHS Board 22 July 2020/Table 2a - ICU patients.csv",
                                       "The daily number of COVID-19 inpatients (confirmed) in ICU at midnight, by board in Scotland, 26/03/2020-22/07/2020",
                                       "ICU Patients", [y * 20 for y in range(1, 12)],
                                       ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "ICU Patients Suspected": ["../../COVID-19 data by NHS Board 22 July 2020/Table 2b - ICU patients (Hist.).csv",
                                       "The daily number of COVID-19 inpatients (suspected) in ICU at midnight, by board in Scotland, 18/03/2020-21/07/2020",
                                       "ICU Patients", [y * 20 for y in range(1, 12)],
                                       ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "Hospital Confirmed": ["../../COVID-19 data by NHS Board 22 July 2020/Table 3a - Hospital Confirmed.csv",
                                   "The daily number of confirmed COVID-19 inpatients in hospital at midnight, by board in Scotland, 26/03/2020-22/07/2020",
                                   "Hospital Patients", [y * 200 for y in range(1, 9)],
                                   ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"],

            "Hospital Suspected": ["../../COVID-19 data by NHS Board 22 July 2020/Table 3b- Hospital Suspected.csv",
                                   "The daily number of suspected COVID-19 inpatients in hospital at midnight, by board in Scotland, 26/03/2020-21/07/2020",
                                   "Hospital Patients", [y * 50 for y in range(1, 11)],
                                   ["default", "kde", "box", "violin", "histogram", "pie"], "Scotland"]
        }

    # Check that method passes when class is initialised correctly.
    def test_init(self):
        self.assertIs(type(self.data_by_board_plots), DataByBoardPlots)
        self.assertEqual(self.data_by_board_plots.plots_path, "test_plots.py")
        self.assertEqual(self.data_by_board_plots.plots_title, "test title")
        self.assertEqual(self.data_by_board_plots.plots_ylabel, "test y label")
        self.assertEqual(self.data_by_board_plots.plots_yticks, range(10))
        self.assertEqual(self.data_by_board_plots.plots_types_list, ["bar", "box", "histogram", "kde", "line", "pie",
                                                                     "violin"])
        self.assertEqual(self.data_by_board_plots.plots_axis_column_index, 2)

    # Check that method passes when return value equals the expected value.
    def test_get_plots_info(self):
        self.assertEqual(self.data_by_board_plots.get_plots_info(), self.expected_plots_info)

    # Check that method fails when styling values of arguments are incorrect or if there is an error tokenizing data.
    def test_create_visualization(self):
        with self.assertRaises(ValueError):
            self.data_by_board_plots.create_visualization("test type", "ticks", "test context", "text palette")
        with self.assertRaises(ValueError):
            self.data_by_board_plots.create_visualization("test type", "test style", "poster", "text palette")
        with self.assertRaises(ValueError):
            self.data_by_board_plots.create_visualization("test type", "test style", "test context", "colorblind")
        with self.assertRaises(pd.errors.ParserError):
            self.data_by_board_plots.create_visualization("test type", "ticks", "poster", "colorblind")


if __name__ == "__main__":
    unittest.main()
