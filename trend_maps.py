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
    duration = solar_df['duration.s'].to_list()
    counts = solar_df['total.counts'].to_list()
    assert isinstance(duration, list)
    assert isinstance(counts, list)
    assert [isinstance(i, int) for i in duration]
    assert [isinstance(i, int) for i in counts]
    #Start with this plot, then start peeling away really high
    #counts
    plt.figure()
    _ = sns.lmplot(x='duration.s', y='total.counts', data=solar_df, ci=None)
    plt.xlabel('duration (s)')
    plt.ylabel('Count in energy range (keV)')

    #maybe it would be better
    #to limit this trend map somehow
    #the large outliers
    #make this plot useless in portraying
    #any desired information
    i=0
    while i < len(counts):
        if counts[i] > 1000000:
            counts.pop(i)
            duration.pop(i)
            i=i-1
        i = i+1
    #plt.clf()
    plt.figure()
    plt.scatter(duration, counts)
    plt.xlabel('duration (s)')
    plt.ylabel('Count in energy range (keV)')
    plt.show()
    
duration_vs_peak(solar_data)