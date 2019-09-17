import urllib.request
import json

citycode = '016010'
resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
resp = json.loads(resp.decode('utf-8'))

print(resp['location']['city'] + "の天気は")
for f in resp['forecasts']:
  print(f['dateLabel'] + "が" + f['telop'])
print("です.")
