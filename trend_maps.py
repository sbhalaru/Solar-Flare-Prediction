import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def duration_vs_counts(solar_df):
    '''
    Takes data frame of duration and peaks then returns a organized
    trend map. (peaks vs duration, should be a clear correlations)
    :param p (list(int)): list of ints, no repeats   
    intput: solar_df (DataFrame): our main dataframe before any cleaning                                             
    '''
    solar_df = solar_df.drop(["flag.1", "flag.2", "flag.3", "flag.4", "flag.5"], axis=1)

    duration = solar_df['duration.s']
    df = solar_df.loc[:, ['duration.s', 'total.counts']]
    ax = df.plot(x="duration.s", y="total.counts", kind="scatter", title='Kevins Plot')
    ax.set_xlabel("Duration (seconds)")
    ax.set_ylabel("Number of Flares")
    plt.show()

    # Count of number of flare events given in a particular duration
    step_size = 500
    df_2 = df.groupby(pd.cut(df["duration.s"], range(0, max(duration), step_size))).count()

    # Total Number of Flares grouped by duration
    df_2 = df.groupby(pd.cut(df["duration.s"], range(0, max(duration), step_size))).sum()
    ax = df_2["total.counts"].plot(kind='bar', title="Total Number of Flares grouped by duration")
    ax.set_xlabel("Duration (seconds)")
    ax.set_ylabel("Total Number of Flares")
    plt.show()

    # Mean Number of Flares in the given duration
    df_2 = df.groupby(pd.cut(df["duration.s"], range(0, max(duration), step_size))).mean()
    ax = df_2["total.counts"].plot(kind='bar', title="Mean Number of Flares in the given duration")
    ax.set_xlabel("Duration (seconds)")
    ax.set_ylabel("Mean Number of Flares")
    plt.show()

    # Number of flare events per year
    # Correlated with the 11 year cycle of flares
    df = solar_df.loc[:, ['start.date', 'total.counts']]
    df = df.groupby(df["start.date"].dt.year).count()
    ax = df["total.counts"].plot(title="Number of Flare Events per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Flare Events")
    plt.show()

    ## Number of flare event across all years per month
    df = solar_df.loc[:, ['start.date', 'total.counts']]
    df["start.date"] = df["start.date"].dt.month_name()
    month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                   "November", "December"]
    df['start.date'] = pd.Categorical(df['start.date'], categories=month_order, ordered=True)
    df = df["total.counts"].groupby(df["start.date"]).count()
    ax = df.plot(title="Number of Flare Events per Month Across All Years")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Flares Events")
    plt.show()

    # Showing that the energy band increases with radial distance
    # Drop last two energy bands since no values
    df = solar_df.loc[:, ['energy.kev', 'radial']]
    df = df.groupby(['energy.kev'])['radial'].mean()
    print(df)
    df = solar_df.loc[:, ['energy.kev', 'radial']]
    df = df.groupby(['energy.kev'])['radial'].count()
    print(df)
    df.plot()
    plt.show()

    ## Lower duration flares events are more in number, but less in the total counts/energy output


solar_df = pd.read_csv("hessi.solar.flare.UP_To_2018.csv", parse_dates=["start.date", "start.time", "peak", "end"],
                       dayfirst=True, infer_datetime_format=True)
duration_vs_counts(solar_df)
