import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

solar_df = pd.read_csv("hessi.solar.flare.UP_To_2018.csv", parse_dates=["start.date", "start.time", "peak", "end"],
                       dayfirst=True, infer_datetime_format=True)

''' Drop the flag columns'''
solar_df = solar_df.drop(["flag.1","flag.2", "flag.3", "flag.4", "flag.5"], axis=1)

''' Get the average value in the energy.kev column'''
for i in range(solar_df.shape[0]):
    energy = solar_df.loc[i, "energy.kev"]
    x = energy.split("-")
    mean = (int(x[0]) + int(x[1])) / 2
    solar_df.loc[i, "energy.kev"] = mean
solar_df = solar_df.astype({"energy.kev": 'float64'})



solar_df["start.time"] = solar_df["start.time"].dt.time
solar_df["peak"] = solar_df["peak"].dt.time
solar_df["end"] = solar_df["end"].dt.time

''' Mask to cover the symmetric portion of the heat map'''
corr = solar_df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

''' Set up the matplotlib figure '''
f, ax = plt.subplots(figsize=(11, 9))

''' Generate a custom diverging colormap '''
cmap = sns.diverging_palette(230, 20, as_cmap=True)

''' Draw the heatmap with the mask and correct aspect ratio'''
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()
