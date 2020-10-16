import pyowm

owm=pyowm.OWM('fa8be47e49ac1dc839e726120dda317b')
mgr=owm.weather_manager()
place=(input("Enter the city name : "))
obs=mgr.weather_at_place(place)
weather=obs.weather
print(f"Weather in {place} : {weather.status}, in detail : {weather.detailed_status}")

#input:Enter the city name : Seattle, US
#Weather in Seattle, US : Clouds, in detail : overcast clouds
