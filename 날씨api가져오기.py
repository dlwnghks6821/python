import requests
import json
apikey='a1cef388f04115b09ccdc2be6adc0ad4'
cities=['Seuol,KR','New York,US','Beijing,CN']
api='http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={Key}'
k2c = lambda k: k-273.15
for name in cities:
    url=api.format(city=name,key=apikey)
    r=requests.get(url)
    data=json.load(r.text)
    print('+도시=',data['name'])
    print('| 날씨=',data['weather'][0]['description'])
    print('| 최저기온 =',k2c(data['main']['temp_min']))
    print('| 최고기온 =',k2c(data['main']['temp_max']))
    print('| 습도=',data['main']['humidity'])
    print('| 기압 =',data['main']['pressure'])
    print('| 풍향 =',data['wind']['deg'])
    print('| 풍속 =',data['wind']['speed'])
    print('')