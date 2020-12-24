import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plot_data = pd.read_csv("GMFM_reduced.csv")
gmfm_tot_t0 = plot_data["GMFM tot T0"].tolist()
gmfm_tot_t1 = plot_data["GMFM tot T1"].tolist()
gmfm_tot_t2 = plot_data["GMFM tot T2"].tolist()
gmfm_tot_t0_to_t2 = gmfm_tot_t0 + gmfm_tot_t1 + gmfm_tot_t2
x_values = ([0] * len(gmfm_tot_t0)) + ([1] * len(gmfm_tot_t1)) + ([2] * len(gmfm_tot_t2))
ax = sns.boxplot(x=x_values, y=gmfm_tot_t0_to_t2)
ax.set_xticks(range(0, 3))
x_ticklabels = ["GMFM tot T0", "GMFM tot T1", "GMFM tot T2"]
ax.set_xticklabels(x_ticklabels)
plt.show()