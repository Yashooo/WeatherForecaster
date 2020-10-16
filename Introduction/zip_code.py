import pyowm

owm=pyowm.OWM('fa8be47e49ac1dc839e726120dda317b')
mgr=owm.weather_manager()
zip1=str(input("Enter the zip-code : "))
country=input("Enter the country-name : ")
obs=mgr.weather_at_zip_code(zip1,country)
weather=obs.weather
temp=weather.temperature(unit='fahrenheit')['temp']

print(f'The Temperature of {zip1},{country} is {temp} Fahrenheit')

#input-Enter the zip-code : 98101    Enter the country-name : US
#output-The Temperature of 98101,US is 55.13 Fahrenheit