from gmaps import getCitiesInCounty
import requests
import json

# enter your api key here
api_key = 'AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk'
county = 'Alameda' # should come from user input 
# cities = ['Alameda', 'Oakland', 'Hayward', 'Pleasanton', 'Livermore', 'San Leandro', 'Berkeley', 'Dublin',
#           'Castro Valley', 'Union City', 'Newark', 'Emeryville', 'Albany', 'San Lorenzo', 'Piedmont', 'Sunol',
#           'Piedmont', 'Sunol', 'Cherryland', 'Fairview', 'Ashland']
cities = getCitiesInCounty(county)
state = 'CA' # should come from user input
county_station = []

def stationCalc():
    global county_station
    for city in cities:
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    
    
        # The text string on which to search
        query = 'Fire station in ' + city + ', ' + state
    
        # get method of requests module
        # return response object
        r = requests.get(url + 'query=' + query +
                         '&key=' + api_key)
    
        # json method of response object convert
        #  json format data into python format data
        x = r.json()
    
        # now x contains list of nested dictionaries
        # we know dictionary contain key value pair
        # store the value of result key in variable y
        y = x['results']
    
        # keep looping upto length of y
        for i in range(len(y)):
            # Append value corresponding to the
            # 'name' key at the ith index of y
            if county in y[i]['name'] or city in y[i]['name']:
                county_station.append((y[i]['name']))
    
    county_station = set(county_station)
    return len(county_station)


county_hospital = []
def hospitalCalc():
    global county_hospital
    for city in cities:
        # url variable store url
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

        # The text string on which to search
        query = 'Fire station in ' + city + ', ' + state

        # get method of requests module
        # return response object
        r = requests.get(url + 'query=' + query +
                         '&key=' + api_key)

        # json method of response object convert
        #  json format data into python format data
        x = r.json()

        # now x contains list of nested dictionaries
        # we know dictionary contain key value pair
        # store the value of result key in variable y
        y = x['results']

        # keep looping upto length of y
        for i in range(len(y)):
            # Append value corresponding to the
            # 'name' key at the ith index of y
            county_hospital.append((y[i]['name']))

    county_station = set(county_hospital)
    return len(county_station)
