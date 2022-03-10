import numpy as np
import pandas as pd
from preprocessing import preprocess_plots
from matplotlib import pyplot as plt
import seaborn as sns


def plots(solar_df):
    '''
    Takes solar data frame and generates the plots for the presentation
    :input: solar_df (DataFrame): our main dataframe before any cleaning
    '''
    assert isinstance(solar_df, pd.DataFrame)

    month_order = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    duration = solar_df['duration.s']
    energy_bands = {"100-300": 5, "12-25": 2, "25-50": 3, "3-6": 0, "300-800": 6, "50-100": 4, "6-12": 1,
                    "7000-20000": 8,
                    "800"
                    "-7000": 7}

    df = solar_df.copy(deep=True)
    df["energy.kev"] = df["energy.kev"].apply(lambda x: energy_bands[x])

    # Adjust plot styles
    plt.style.use("dark_background")
    color = (32 / 255, 100 / 255, 170 / 255, 255 / 255)
    # Mask to cover the symmetric portion of the heat map
    corr = df.corr()
    mask = np.triu(np.ones_like(corr)) - np.eye(corr.shape[0])


    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.color_palette("RdBu", as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
                square=True, linewidths=0, cbar_kws={"shrink": .5})
    plt.title("Data Correlation Heat Map", fontsize=20)
    plt.xticks(rotation=45, fontsize=15)
    plt.yticks(fontsize=15)
    plt.show()

    # Total Number of Flares grouped by duration
    df = solar_df.loc[:, ['duration.s', 'total.counts']]
    df_2 = df.groupby(pd.cut(df["duration.s"], range(0, max(duration), 500))).sum()
    ax = df_2["total.counts"].plot(kind='bar', color=color, fontsize=12)
    ax.set_xlabel("Duration (seconds)", fontsize=15)
    ax.set_ylabel("Total Number of Flares", fontsize=15)
    plt.title("Total Number of Flares Grouped by Duration", fontsize=20)
    plt.xticks(rotation=0)
    plt.show()

    # Frequency of flare events given in a particular duration
    df_2 = df.groupby(pd.cut(df["duration.s"], range(0, max(duration), 500))).count()
    ax = df_2["total.counts"].plot(kind='bar', color=color, fontsize=12)
    ax.set_xlabel("Duration (seconds)", fontsize=15)
    ax.set_ylabel("Total Number of Flares", fontsize=15)
    plt.title("Frequency of Flare Events Grouped by Duration", fontsize=20)
    plt.xticks(rotation=0)
    plt.show()

    # Mean Number of Flares in the given duration
    df_2 = df.groupby(pd.cut(df["duration.s"], range(0, max(duration), 500))).mean()
    ax = df_2["total.counts"].plot(kind='bar', color=color, fontsize=12)
    ax.set_xlabel("Duration (seconds)", fontsize=15)
    ax.set_ylabel("Mean Number of Flares", fontsize=15)
    plt.title("Mean Number of Flares per Event Grouped by Duration", fontsize=20)
    plt.xticks(rotation=0)
    plt.show()

    # Number of flare events per year
    # Correlated with the 11 year cycle of flares
    df = solar_df.loc[:, ['year', 'total.counts']]
    df = df.groupby(df["year"]).count()
    ax = df["total.counts"].plot(color=color, fontsize=12)
    ax.set_xlabel("Year", fontsize=15)
    ax.set_ylabel("Number of Flare Events", fontsize=15)
    plt.title("Number of Flare Events per Year", fontsize=20)
    plt.show()

    # Number of flare event per month for 2014
    df = solar_df[solar_df['year'] == 2014]
    df = df.loc[:, ['month', 'total.counts']]
    df = df["total.counts"].groupby(df["month"]).count()
    ax = df.plot(color=color, fontsize=12)
    ax.set_xlabel("Month", fontsize=15)
    ax.set_ylabel("Number of Flares Events", fontsize=15)
    plt.title("Number of Flare Events per Month in 2014", fontsize=20)
    plt.xticks(range(13), month_order)
    plt.show()

    # Number of flare event per month for 2008
    df = solar_df[solar_df['year'] == 2008]
    df = df.loc[:, ['month', 'total.counts']]
    df = df["total.counts"].groupby(df["month"]).count()
    ax = df.plot(color=color, fontsize=12)
    ax.set_xlabel("Month", fontsize=15)
    ax.set_ylabel("Number of Flares Events", fontsize=15)
    plt.title("Number of Flare Events per Month in 2008", fontsize=20)
    plt.xticks(range(13), month_order)
    plt.show()

    # Number of flare event per month for all years
    df = solar_df.loc[:, ['month', 'total.counts']]
    df = df["total.counts"].groupby(df["month"]).count()
    ax = df.plot(color=color, fontsize=12)
    ax.set_xlabel("Month", fontsize=15)
    ax.set_ylabel("Number of Flares Events", fontsize=15)
    plt.title("Number of Flare Events per Month from 2002-2018", fontsize=20)
    plt.xticks(range(13), month_order)
    plt.show()

    # Energy Band vs Radial Distance
    df = solar_df.loc[:, ['energy.kev', 'radial']]
    df = df[df['energy.kev'] != "800-7000"]
    df = df[df['energy.kev'] != "7000-20000"]
    df = df.groupby(['energy.kev'])['radial'].mean()
    ax = df.plot(color=color, fontsize=12)
    ax.set_xlabel("Energy Band (kev)", fontsize=15)
    ax.set_ylabel("Radial Distance (arcseconds)", fontsize=15)
    plt.title("Radial Distance vs Energy Band", fontsize=20)
    plt.show()

    # Energy Band vs Duration
    # Showing that the energy band increases with radial distance
    df = solar_df.loc[:, ['energy.kev', 'duration.s']]
    df = df[df['energy.kev'] != "800-7000"]
    df = df[df['energy.kev'] != "7000-20000"]
    df = df.groupby(['energy.kev'])['duration.s'].mean()
    ax = df.plot(color=color, fontsize=12)
    ax.set_xlabel("Energy Band (kev)", fontsize=15)
    ax.set_ylabel("Duration (in seconds)", fontsize=15)
    plt.title("Duration vs Energy Band", fontsize=20)
    plt.show()

    # Radial Distance vs Year
    df = solar_df.loc[:, ['year', 'radial']]
    df = df.groupby(['year'])['radial'].mean()
    ax = df.plot(color=color, fontsize=12)
    ax.set_xlabel("Year", fontsize=15)
    ax.set_ylabel("Radial Distance (arcseconds)", fontsize=15)
    plt.title("Radial Distance vs Year", fontsize=20)
    plt.show()


if __name__ == '__main__':
    solar_df = preprocess_plots("hessi.solar.flare.UP_To_2018.csv")
    plots(solar_df)
