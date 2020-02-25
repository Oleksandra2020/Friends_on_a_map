import json
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import ssl
import folium

geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=100)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
ssl._create_default_https_context = ssl._create_unverified_context


# def read_file(file):
#     """
#     () -> list
#     Reads the given json file
#     """
#     with open(file) as f:
#         return json.load(f)


def locs_names(file):
    """
    list -> dict
    Returns the dictionary of the name of a friend as a key and
    the location as a value
    """
    count = 0
    dct = {}
    for id in file['users']:
        loc = id['location']
        if loc:
            dct[id['screen_name']] = loc
            count += 1
    return dct


def show_map(dct):
    """
    dict -> ()
    Creates html map of user's friends
    """
    map = folium.Map()
    fg = folium.FeatureGroup(name="Friends_map")
    count = 0.1
    for key in dct:
        ag = "specify_your_app_name_here"
        geolocator = Nominatim(user_agent=ag, timeout=100)
        try:
            location = geolocator.geocode(dct[key], timeout=100)
            lat, lon = location.latitude, location.longitude
            fg.add_child(folium.CircleMarker(location=[lat+count, lon+count],
                                             radius=10,
                                             popup=key,
                                             fill_color='blue',
                                             color='green',
                                             fill_opacity=0.5))
            count += 0.2
        except AttributeError:
            continue
        except TypeError:
            continue
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    m = map.get_root().render()
    return m


def get_started(file):
    # file = read_file(file)
    dct = locs_names(file)
    p = show_map(dct)
    return p
