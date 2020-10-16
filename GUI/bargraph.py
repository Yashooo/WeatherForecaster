import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
import pyowm

def plot_bars(days,min_t,max_t):       
        days=dates.date2num(days)
        min_temp_bar=plt.bar(days-0.2, min_t, width=0.4, color='b')
        max_temp_bar=plt.bar(days+0.2, max_t, width=0.4, color='r')        
        plt.xticks(days)
        x_y_axis=plt.gca()
        xaxis_format=dates.DateFormatter('%m/%d')
        
        x_y_axis.xaxis.set_major_formatter(xaxis_format)
        plt.xlabel('Dates(mm/dd)') 
        plt.ylabel('Temperature') 
        plt.title('5-Day Weather Forecast')
        
        for bar_chart in [min_temp_bar,max_temp_bar]:
           for index,bar in enumerate(bar_chart):
               height=bar.get_height()
               xpos=bar.get_x()+bar.get_width()/2.0
               ypos=height 
               label_text=str(int(height))
               plt.text(xpos, ypos,label_text,
                       horizontalalignment='center',
                       verticalalignment='bottom',
                       color='black')
        
        
        plt.savefig('figure.png')
        plt.clf()
    
