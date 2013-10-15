from urllib.request import urlopen
import json

def printResults(data):
    theJSON = json.loads(data)
    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])

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
