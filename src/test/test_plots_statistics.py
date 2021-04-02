import sys
sys.path.append("..")

import unittest
import pandas as pd
import numpy as np
from main.plots_statistics import PlotsStatistics


class TestPlotsStatistics(unittest.TestCase):

    def setUp(self):
        self.plot_data = pd.DataFrame(np.array([[1, 1.23, -4, 0, np.nan], [2, 4.56, -5, 0, np.nan],
                                                [3, 7.89, -6, 0, np.nan]]),
                                      columns=["whole numbers", "decimal numbers", "negative numbers", "zeros", "NaNs"])
        self.plots_statistics = PlotsStatistics(self.plot_data, 0, "test")
        self.expected_results = [
            ["Minimum value of test: 1.0", "Maximum value of test: 3.0", "Median value of test: 2.0",
             "Mean value of test: 2.0", "Standard Deviation value of test: 0.816496580927726",
             "Variance value of test: 0.6666666666666666"],
            ["Minimum value of test: 1.23", "Maximum value of test: 7.89", "Median value of test: 4.56",
             "Mean value of test: 4.56", "Standard Deviation value of test: 2.7189336144893277",
             "Variance value of test: 7.392599999999999"],
            ["Minimum value of test: -6.0", "Maximum value of test: -4.0", "Median value of test: -5.0",
             "Mean value of test: -5.0", "Standard Deviation value of test: 0.816496580927726",
             "Variance value of test: 0.6666666666666666"],
            ["Minimum value of test: 0.0", "Maximum value of test: 0.0", "Median value of test: 0.0",
             "Mean value of test: 0.0", "Standard Deviation value of test: 0.0",
             "Variance value of test: 0.0"],
            ["Minimum value of test: nan", "Maximum value of test: nan", "Median value of test: nan",
             "Mean value of test: nan", "Standard Deviation value of test: nan",
             "Variance value of test: nan"]]

    # Check that method passes when class is initialised correctly.
    def test_init(self):
        self.assertIs(type(self.plots_statistics), PlotsStatistics)
        self.assertIs(self.plots_statistics.plot_data, self.plot_data)
        self.assertEqual(self.plots_statistics.plot_axis_column_index, 0)
        self.assertEqual(self.plots_statistics.plot_ylabel, "test")

    # Check that method passes when returned values equals expected values.
    def test_get_plots_statistics(self):
        for i in range(5):
            expected_result = self.expected_results[i]
            test_statistics = PlotsStatistics(self.plot_data, i, "test")
            result = test_statistics.get_plots_statistics()
            self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
