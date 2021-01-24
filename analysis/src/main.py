import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

ozoneData = pd.read_csv("../resources/data", names=["ppb"]).reset_index()

# Plot all data
ozoneData.plot.scatter(x='index', y='ppb', s=2)

# Plot grouped by 3600 points (1h worth of data)
ozoneData.groupby(ozoneData.index // 3600).mean().plot.scatter(x='index', y='ppb')

plt.show()
