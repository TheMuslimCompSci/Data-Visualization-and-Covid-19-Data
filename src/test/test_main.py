# This is the main test Python script for the program.


import unittest
from src.test.test_dashboard import TestDashboard
from src.test.test_data_by_board_plots import TestDataByBoardPlots
from src.test.test_deaths_data_plots import TestDeathsDataPlots
from src.test.test_plots import TestPlots
from src.test.test_plots_statistics import TestPlotsStatistics
from src.test.test_trends_in_daily_data_plots import TestTrendsInDailyDataPlots


# Launch the COVID-19 Data Visualization App Tests
def launch_app_tests():
    unittest.main(TestDashboard)


# Gets run after Shift+F10 is pressed to execute code
if __name__ == '__main__':
    launch_app_tests()
