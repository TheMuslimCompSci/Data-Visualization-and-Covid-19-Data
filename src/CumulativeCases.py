import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""Represents plots from Table 1: Cumulative Number of Cases Tested Positive for COVID-19 
- as reported from dates 03/07/20 to 07/22/20 on SG website"""

class CumulativeCases(object):

    def __init__(self):
        self.create_plots()

    def create_plots(self):
        cumulative_cases = pd.read_csv("../COVID-19 data by NHS Board 22 July 2020/Table 1 - Cumulative cases.csv")
        sns.lineplot(data = cumulative_cases, x = "Date", y = 'Scotland')
        plt.show()
        print("hello")

CumulativeCases()
