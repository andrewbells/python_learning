
import urllib.request
import json


def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON['metadata']:
        print (theJSON["metadata"]["title"])
    count = theJSON["metadata"]["count"];
    print (str(count) + " events recorded")
    
    for i in theJSON["features"]:
        print (i["properties"]["place"])
        
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
        
    print ("events that were felt: ")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None and feltReports > 0:
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) +" times")

def main():
    
    urlData = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    webUrl = urllib.request.urlopen(urlData)
    print (webUrl.getcode())
    if webUrl.getcode() == 200:
        data = webUrl.read().decode('utf-8')
        printResults(data)
    else:
        print ('received an error from server, cannot retrieve results, code ' + str(webUrl.getcode()))




if __name__ == '__main__':
    main()
    