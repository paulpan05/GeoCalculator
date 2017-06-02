from googlemaps import *
from datetime import datetime
from pytz import *
from vincenty import vincenty

n1 = open(r'mapkey.txt', "r")
n2 = open(r'timekey.txt', "r")

key1 = n1.read()
key2 = n2.read()

n1.close()
n2.close()

key1 = key1.replace(' ', '')
key2 = key2.replace(' ', '')

map = Client(key=key1, client_id=None, client_secret=None, timeout=10, connect_timeout=None, read_timeout=None, retry_timeout=60, requests_kwargs=None, queries_per_second=10, channel=None)
mapTime = Client(key=key2, client_id=None, client_secret=None, timeout=10, connect_timeout=None, read_timeout=None, retry_timeout=60, requests_kwargs=None, queries_per_second=10, channel=None)


class GoogleMapsAPI(object):

    def __init__(self, location):
        self.geocode = map.geocode(location)
    def getFormatedAddress(self):
        self.address = self.geocode[0].get('formatted_address')
        return self.address
    def getLat(self):
        self.lat = self.geocode[0].get('geometry').get('location').get('lat')
        return self.lat
    def getLng(self):
        self.lng = self.geocode[0].get('geometry').get('location').get('lng')
        return self.lng
    def getElevation(self):
        self.eleData = map.elevation((self.getLat(),self.getLng()))
        self.elevation = self.eleData[0].get('elevation')
        return self.elevation
    def getElevationft(self):
        return self.getElevation() * 3.280839895
    def getFormatedElevation(self):
        return "Elevation: \n" + str("%.2f" % self.getElevation()) + " m\n" + str("%.2f" % self.getElevationft()) + " ft"
    def getCoordinate(self):
        self.coordinate = (self.getLat(), self.getLng())
        return self.coordinate
    def getFormatedCoordinate(self):
        if self.getLat() < 0:
            ns = "S"
            newLatitude = abs(self.getLat())
            newLatDeg = int(newLatitude) / 1.0
            newLatMin = (newLatitude - newLatDeg) * 60.0
            newLatSec = (newLatMin - (int(newLatMin) / 1.0)) * 60.0
        else:
            ns = "N"
            newLatDeg = int(self.getLat()) / 1.0
            newLatMin = (self.getLat() - newLatDeg) * 60.0
            newLatSec = (newLatMin - (int(newLatMin) / 1.0)) * 60.0
        if self.getLng() < 0:
            ew = "W"
            newLongitude = abs(self.getLng())
            newLongDeg = int(newLongitude) / 1.0
            newLongMin = (newLongitude - newLongDeg) * 60.0
            newLongSec = (newLongMin - (int(newLongMin) / 1.0)) * 60.0
        else:
            ew = "E"
            newLongDeg = int(self.getLng()) / 1.0
            newLongMin = (self.getLng() - newLongDeg) * 60.0
            newLongSec = (newLongMin - (int(newLongMin) / 1.0)) * 60.0
        return "Latitude:  " + str(int(newLatDeg)) + "° " + str(int(newLatMin)) + "' " + str("%.4f" % newLatSec) + '" ' + ns + "\nLongitude: " + str(int(newLongDeg)) + "° " + str(int(newLongMin)) + "' " + str("%.4f" % newLongSec) + '" ' + ew
    def getTime(self):
        self.timezone_str = mapTime.timezone(location = self.getCoordinate()).get('timeZoneId')
        self.tzone = timezone(self.timezone_str)
        self.tzTime = datetime.now(self.tzone)
        return self.tzTime
    def getFormatedTime(self):
        return self.getTime().strftime('Date: %Y-%m-%d\nTime: %H:%M:%S')

def getDistanceKM(location1, location2):
    newAPI_1 = GoogleMapsAPI(location1)
    newAPI_2 = GoogleMapsAPI(location2)
    coordinate_1 = newAPI_1.getCoordinate()
    coordinate_2 = newAPI_2.getCoordinate()
    return vincenty(coordinate_1, coordinate_2)

def getDistanceMI(location1, location2):
    newAPI_1 = GoogleMapsAPI(location1)
    newAPI_2 = GoogleMapsAPI(location2)
    coordinate_1 = newAPI_1.getCoordinate()
    coordinate_2 = newAPI_2.getCoordinate()
    return vincenty(coordinate_1, coordinate_2, miles=True)

def getFormatedDistance(location1, location2):
    return("Distance:\n" + str("%.2f" % getDistanceKM(location1, location2)) + " km\n" + str("%.2f" % getDistanceMI(location1, location2)) + " mi")

def getFlightTime(location1, location2):
    return ((getDistanceMI(location1,location2) / 562.0) + 0.8)

def getFormatedFlightTime(location1, location2):
    flightTimeHours = int(getFlightTime(location1, location2))
    flightTimeMinutes = int((getFlightTime(location1, location2) - (flightTimeHours/1.0)) * (60.0))
    return "Flight Time: " + str(flightTimeHours) + " hours " + str(flightTimeMinutes) + " minutes" + "\n\nNote: Flight time includes both takeoff and landing times."

def getFormatedTimeDifference(location1, location2):
    newAPI_1 = GoogleMapsAPI(location1)
    newAPI_2 = GoogleMapsAPI(location2)
    coordinate_1 = newAPI_1.getCoordinate()
    coordinate_2 = newAPI_2.getCoordinate()
    time_1 = mapTime.timezone(location = coordinate_1)
    time_2 = mapTime.timezone(location = coordinate_2)
    offset_1 = time_1.get('rawOffset')
    offset_2 = time_2.get('rawOffset')
    timeDifference = (abs(offset_1-offset_2)) / (60.0 * 60.0)
    return "Time Difference: " + str(int(timeDifference)) + " hours " + str(int((timeDifference - (int(timeDifference)/1.0))*60.0)) + " minutes"

def getFormatedPhysicalTimeDifference(location1, location2):
    newAPI_1 = GoogleMapsAPI(location1)
    newAPI_2 = GoogleMapsAPI(location2)
    coordinate_1 = newAPI_1.getCoordinate()
    coordinate_2 = newAPI_2.getCoordinate()
    time_1 = mapTime.timezone(location = coordinate_1)
    time_2 = mapTime.timezone(location = coordinate_2)
    offset_1 = time_1.get('rawOffset')
    offset_2 = time_2.get('rawOffset')
    timeDifference = (abs(offset_1-offset_2)) / (60.0 * 60.0)
    if timeDifference > 12.0:
        timeDifference = 24.0 - timeDifference
    return "Time Difference: " + str(int(timeDifference)) + " hours " + str(int((timeDifference - (int(timeDifference)/1.0))*60.0)) + " minutes"