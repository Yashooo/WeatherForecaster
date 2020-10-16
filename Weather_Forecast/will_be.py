
import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime

owm=pyowm.OWM('fa8be47e49ac1dc839e726120dda317b')
mgr=owm.weather_manager()
place=input("Enter the name of the place : ")
forecaster = mgr.forecast_at_place(place,'3h')

date1=timestamps.tomorrow(12,0)
date2=timestamps.tomorrow(8,30)
print(forecaster.will_be_foggy_at(date1))
print(forecaster.will_be_clear_at(date2))

#input-Enter the name of the place : Los Angeles, US
#output-False  True