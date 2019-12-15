import math
from math import radians, cos, pi, acos, sin

from ways import info


def getLink(source, target):
    for link in source[3]:
        if link[1] == target[0]:
            return link
    return None


def compute_cost(source, target):
    return cost(source, target)


def compute_distance(lat1, lon1, lat2, lon2):
    return distance(lat1, lon1, lat2, lon2) / 110


def cost(source, target):
    dist = compute_distance(source[1], source[2], target[1], target[2])
    # dist = dist / 1000 + dist % 1000
    link = getLink(source, target)
    if link is None:
        return math.inf
    speed = info.SPEED_RANGES[link[3]][1]
    return dist / speed


def distance(lat1, lon1, lat2, lon2):
    '''computes distance in KM'''
    '''
    This code was borrowed from 
    http://www.johndcook.com/python_longitude_latitude.html
    '''
    if (lat1, lon1) == (lat2, lon2):
        return 0.0
    if max(abs(lat1 - lat2), abs(lon1 - lon2)) < 0.00001:
        return 0.001

    phi1 = radians(90 - lat1)
    phi2 = radians(90 - lat2)

    meter_units_factor = 40000 / (2 * pi)
    arc = acos(sin(phi1) * sin(phi2) * cos(radians(lon1) - radians(lon2))
               + cos(phi1) * cos(phi2))
    return arc * meter_units_factor
