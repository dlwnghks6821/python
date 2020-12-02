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
    print('+����=',data['name'])
    print('| ����=',data['weather'][0]['description'])
    print('| ������� =',k2c(data['main']['temp_min']))
    print('| �ְ��� =',k2c(data['main']['temp_max']))
    print('| ����=',data['main']['humidity'])
    print('| ��� =',data['main']['pressure'])
    print('| ǳ�� =',data['wind']['deg'])
    print('| ǳ�� =',data['wind']['speed'])
    print('')