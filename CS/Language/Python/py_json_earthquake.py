# http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
# past 30 days M4.5 earthquake
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson
# for python 3.x

import urllib.request
import json

geourl = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"

response = urllib.request.urlopen(geourl)
content = response.read()
data = json.loads(content.decode('utf8'))

print(type(data))
print(data['type'])
