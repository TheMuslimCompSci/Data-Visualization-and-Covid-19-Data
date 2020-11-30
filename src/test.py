# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plot_data = pd.read_csv("GMFM_reduced.csv")
sns.boxplot(data=plot_data,
            x="aetiology [1=TBI; 2=infection; 3=anoxia; 4=ictal; 5=AVM; 6=tumor; 7=other]",
            y="age at trauma [months]")
plt.show()

