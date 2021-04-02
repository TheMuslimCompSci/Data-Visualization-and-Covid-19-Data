import sys
sys.path.append("..")

import unittest
import pandas as pd
from main.plots import Plots


class TestPlots(unittest.TestCase):

    def setUp(self):
        self.plots = Plots("test_plots.py", "test title", ["bar", "box", "histogram", "kde", "line", "pie", "violin"],
                           1, "test y label")
        self.expected_plots_styles = [
            ("default", "None"),
            ("dark grid", "darkgrid"),
            ("white grid", "whitegrid"),
            ("dark", "dark"),
            ("white", "white"),
            ("ticks", "ticks")
        ]
        self.expected_plots_contexts = [
            ("default", "notebook"),
            ("paper", "paper"),
            ("talk", "talk"),
            ("poster", "poster"),
        ]
        self.expected_plots_palettes = [
            ("default", "None"),
            ("deep", "deep"),
            ("muted", "muted"),
            ("pastel", "pastel"),
            ("bright", "bright"),
            ("dark", "dark"),
            ("colour blind", "colorblind"),
        ]

    # Check that method passes when class is initialised correctly.
    def test_init(self):
        self.assertIs(type(self.plots), Plots)
        self.assertEqual(self.plots.plots_path, "test_plots.py")
        self.assertEqual(self.plots.plots_title, "test title")
        self.assertEqual(self.plots.plots_types_list, ["bar", "box", "histogram", "kde", "line", "pie", "violin"])
        self.assertEqual(self.plots.plots_axis_column_index, 1)
        self.assertEqual(self.plots.plots_ylabel, "test y label")

    # Check that method fails when there is an error tokenizing data.
    def test_get_plots_data(self):
        with self.assertRaises(pd.errors.ParserError):
            self.plots.get_plots_data()

    # Check that method fails when there is an error tokenizing data.
    def test_get_plots_axis_column_index(self):
        with self.assertRaises(pd.errors.ParserError):
            self.plots.get_plots_axis_column_index()

    # Check that method fails when there is an error tokenizing data.
    def test_get_plots_statistics(self):
        with self.assertRaises(pd.errors.ParserError):
            self.plots.get_plots_statistics()

    # Check that method fails when styling values of arguments are incorrect.
    def test_set_plots_styling(self):
        with self.assertRaises(ValueError):
            self.plots.set_plots_styling("test style", "test context", "text palette")

    # Check that method passes when return value equals the expected value.
    def test_get_plots_styles_list(self):
        self.assertEqual(self.plots.get_plots_styles_list(), self.expected_plots_styles)

    # Check that method passes when return value equals the expected value.
    def test_get_plots_contexts_list(self):
        self.assertEqual(self.plots.get_plots_contexts_list(), self.expected_plots_contexts)

    # Check that method passes when return value equals the expected value.
    def test_get_plots_palettes_list(self):
        self.assertEqual(self.plots.get_plots_palettes_list(), self.expected_plots_palettes)


if __name__ == "__main__":
    unittest.main()
