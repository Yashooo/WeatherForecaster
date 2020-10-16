
import pyowm

owm=pyowm.OWM('fa8be47e49ac1dc839e726120dda317b')
mgr=owm.weather_manager()
lat=float(input("Enter the city latitude : "))
lon=float(input("Enter the city longitude : "))
obs=mgr.weather_at_coords(lat,lon)
weather=obs.weather
temp=weather.temperature(unit='fahrenheit')['temp']

print(f'The Temperature of {lat},{lon} is {temp} Fahrenheit')

#input-Enter the city latitude : 48.853409   Enter the city longitude : 2.3488
#output-The Temperature of 48.853409,2.3488 is 69.75 Fahrenheit