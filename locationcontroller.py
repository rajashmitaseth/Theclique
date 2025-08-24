import geocoder
from geopy.geocoders import Nominatim


def getLocation():
    g = geocoder.ip('me')
    ll = g.latlng
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse(ll)
    address = location.raw['address']
    state = address.get('state').split()[0]
    district = address.get('state_district').split()[0]
    location = address.get('county').split()[0]
    return [state,district,location]