import numpy as np
import matplotlib.pyplot as plt
import time
from preprocessing import *

def tic():
  return time.time()
def toc(tstart, name="Operation"):
  print('%s took: %s sec.\n' % (name,(time.time() - tstart)))

def filter_energy(data,filtered_eng = 0, filtered_rad_range = 99):
    '''
    The function for filter the solar event by energy_kev and radial

    '''
    try:
        assert isinstance(filtered_eng,int)
        assert isinstance(filtered_rad_range,int or float)
        assert filtered_eng>=0 and filtered_eng<= 8
        assert filtered_rad_range >= 0 and filtered_rad_range<=100

        #filter the data with energy
        lenght1 = len(data)
        data = data[data['energy_kev']!= filtered_eng]
        lenght2 = len(data)
    

        #filter the data with radial
        radial = data['radial'].values
        lenght1 = len(data)
        data = data[data['radial']<=np.percentile(radial,filtered_rad_range)]
        lenght2 = len(data)
        print('Filtering successful!')
        return data

    except(AssertionError):
        print('Filtering failed! range is wrong!')


def filter_month(data,start_month,end_month):
    '''
    This is the function for filtering the month to plot the sunspot
    '''
    data = data[data['month']<= end_month]
    data = data[data['month']>= start_month]

    return data

def ploting_sunspot(data,start_month,end_month):
    '''
    The function for sunspot plotting using the filtered data
    
    '''
    ts = tic()
    assert isinstance(start_month,int)
    assert isinstance(end_month,int)
    assert start_month>=1 and end_month<=12
    assert start_month<=end_month

    colors = plt.cm.turbo(np.linspace(-0.2,1,9))
    plt.style.use('dark_background')
    plt.rcParams.update({'font.size':12})
   
    data = filter_month(data,start_month,end_month)

    # build figure object
    fig, ax = plt.subplots(figsize=(10,10))
    # loop over energy ranges
    label_eng = ['3-6', '6-12','12-25','25-50','50-100','100-300','300-800','800-7000','7000-20000']
    month_map = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    for i,irange in enumerate(np.arange(0,9)):
        
        AUX_data = data[data['energy_kev']==irange][['x_pos','y_pos']]
        # scatter plot to plot flare
        plt.scatter(AUX_data['x_pos'].values,AUX_data['y_pos'].values,color=colors[i],label='%s Kev'%label_eng[i],s=15)
        plt.legend(loc='lower right',fontsize=10,shadow=True)
        
    # set title to plot
    plt.grid( linestyle = '--', linewidth = 0.35)
    if end_month!=start_month:
        plt.title('Sunspots per Energy from '+month_map[start_month-1]+' to '+month_map[end_month-1]+' 2002-2018')
    else:
        plt.title('Sunspots per Energy in '+ month_map[start_month-1]+ ' 2002-2018')

    plt.xlabel('x_pos.asec')
    plt.ylabel('y_pos.asec')
    plt.xlim([-1200,1200])
    plt.ylim([-1200,1200])
    # plt.savefig( str(start_month) +'_soalr_new.jpg',dpi = 300)
    plt.savefig( 'Whole_soalr_new.jpg',dpi = 300)

    plt.show()
    
    toc(ts,"Sunspot Drawing")

if __name__ == '__main__':
    filename = 'hessi.solar.flare.UP_To_2018.csv'
    solar_data = preprocess(filename)

    # for i in range(0,12):
    #     start_month = i+1
    #     end_month = start_month
    #     ploting_sunspot(solar_data,start_month,end_month)

    ploting_sunspot(solar_data,1,12)   


    