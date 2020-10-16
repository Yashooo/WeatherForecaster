import pyowm

owm=pyowm.OWM('fa8be47e49ac1dc839e726120dda317b')
mgr=owm.weather_manager()
place=input("Enter the name of the city : ")
obs=mgr.weather_at_place(place)
weather=obs.weather
temp=weather.temperature(unit='fahrenheit')['temp']

print(f'The Temperature of {place} is {temp} Fahrenheit')


#input : Enter the name of the city : Sydney, AU
#output : The Temperature of Sydney, AU is 61.34 Fahrenheit