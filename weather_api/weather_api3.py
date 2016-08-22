import urllib3, json

city_names = ['Nairobi', 'London', 'Lagos']
app_key = '2bc3e79bb974a007818864813f53fd35'




def get_weather():
	collected_data = []
	for city in city_names:
		http = urllib3.PoolManager()
		url = "http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}&units=metric".format(city, app_key)
		r = http.request('GET', url)
		json_data = json.loads(r.data)
		collected_data.append([city, json_data["main"]["temp"], json_data["weather"][0]["description"]])
	return collected_data

start_space = "".ljust(3)

print start_space, "=" * 50
print start_space, "City".ljust(10), "Temperature".ljust(20), "Description" 
print start_space, "=" * 50

for data in get_weather():
	print  start_space, data[0].ljust(10), str(data[1]).ljust(20), data[2], "\n"