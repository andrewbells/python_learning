from urllib.request import urlopen
import json

'''
output
200
USGS Magnitude 2.5+ Earthquakes, Past Day
63 events recorded
17km WSW of Nereju, Romania
44km NE of Luganville, Vanuatu
5km SSE of Panaytayon, Philippines
...
'''

def printResults(data):
    theJSON = json.loads(data)
    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])
    count = theJSON['metadata']['count']
    print(str(count) + ' events recorded')
    for i in theJSON['features']:
        print (i['properties']['place'])
        
def main():
    urlData = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    webUrl = urlopen(urlData)
    print(webUrl.getcode())
    if webUrl.getcode() == 200:
        data = webUrl.read().decode("utf-8")
        printResults(data)
    else:
        print ("it's got screwd up")
    


if __name__ == '__main__':
    main()
