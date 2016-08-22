import urllib2, urllib, json

city_names = ['Nairobi', 'Lagos', 'London']
app_key = '2bc3e79bb974a007818864813f53fd35'


def get_weather():
	for city in city_names:
		url = "http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}&units=metric".format(city, app_key)
		result = urllib2.urlopen(url).read()
		data = json.loads(result)
		return "City: ", city,"\n", "Temperature: ", data['main']['temp'], "\n", "Description: ", data['weather'][0]['description']

get_weather()







