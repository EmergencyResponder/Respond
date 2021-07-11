from gmaps import getCitiesInCounty, getCounty
from googlemaps import Client as GoogleMaps
import requests
import json

Geocoder = GoogleMaps.Client(key='AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk')
# enter your api key here
api_key = 'AIzaSyBx2lGCeaLjMTNblROj3I4iNL8DWi45jvk'
countyName = getCounty(94555)  # should come from user input
# cities = ['Alameda', 'Oakland', 'Hayward', 'Pleasanton', 'Livermore', 'San Leandro', 'Berkeley', 'Dublin',
#           'Castro Valley', 'Union City', 'Newark', 'Emeryville', 'Albany', 'San Lorenzo', 'Piedmont', 'Sunol',
#           'Piedmont', 'Sunol', 'Cherryland', 'Fairview', 'Ashland']
stateName = 'CA'  # should come from user input

nearbyStation = []
stationAddresses = []

def stationCalc(address):
    global nearbyStation

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    query = 'Fire station'

    location = Geocoder.geocode(address)
    latitude = location[0]['geometry']['location']['lat']
    longitude = location[0]['geometry']['location']['lng']

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query + '&location=' + latitude + ', ' + longitude +
                     '&type=fire_station' + '&rankby=distance' + '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y
    for i in range(min(len(y), 5)):
        nearbyStation.append((y[i]['name']))
        stationAddresses.append(y[i]['formatted_address'])
    stationNumber = len(stationAddresses)
    return stationNumber, stationAddresses, nearbyStation


nearbyHospital = []
hospitalAddresses = []

def hospitalCalc(address):
    global nearbyHospital
    global hospitalAddresses

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    query = 'Hospital'

    location = Geocoder.geocode(address)
    latitude = location[0]['geometry']['location']['lat']
    longitude = location[0]['geometry']['location']['lng']

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query + '&location=' + latitude + ', ' + longitude +
                     '&type=hospital' + '&rankby=distance' + '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y
    for i in range(min(len(y),5)):
        hospitalName = y[i]['name']
        nearbyHospital.append(hospitalName)
        hospitalAddresses.append(y[i]['formatted_address'])

    hospitalNumber = len(nearbyHospital)
    return hospitalNumber, hospitalAddresses, nearbyHospital

AlamedaStationNum, AlamedaStationAddresses, AlamedaStationNames = stationCalc('5121 Stagecoach Street')
AlamedaHospitalNum, AlamedaHospAddresses, AlamedaHospNames = hospitalCalc('5121 Stagecoach Street')
print(AlamedaStationNames)
print(AlamedaHospNames)
