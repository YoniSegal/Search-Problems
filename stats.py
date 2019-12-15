'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple
from ways import load_map_from_csv


def getBranchingFactor(roads):
    junctions_to_outgoing = {}
    for junction in roads.values():
        for link in junction[3]:
            if junction not in junctions_to_outgoing:
                junctions_to_outgoing[junction] = 0
            if link[0] == junction[0]:
                junctions_to_outgoing[junction] += 1
    start = next(iter(junctions_to_outgoing))
    min_outgoing = junctions_to_outgoing[start]
    max_outgoing = 0
    total = 0
    for pair in junctions_to_outgoing:
        total += pair[1]
        if pair[1] < min_outgoing:
            min_outgoing = pair[1]
        if pair[1] > max_outgoing:
            max_outgoing = pair[1]
    average_outgoing = total / len(junctions_to_outgoing.keys())
    return max_outgoing, min_outgoing, average_outgoing


def getLinkDistances(links):
    links = tuple(links)
    min_distance = links[0][2]
    max_distance = 0
    total = 0

    for link in links:
        total += link[2]
        if link[2] < min_distance:
            min_distance = link[2]
        if link[2] > max_distance:
            max_distance = link[2]
    average_distance = total / len(links)
    return max_distance, min_distance, average_distance


def getStats(roads):
    junctions = len(roads)
    links = set(link for junction in roads.values() for link in junction[3])
    branching_factor = getBranchingFactor(roads)
    link_distances = getLinkDistances(links)
    return junctions, len(links), branching_factor, link_distances


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    stats = getStats(roads)
    return {
        'Number of junctions': stats[0],
        'Number of links': stats[1],
        'Outgoing branching factor': Stat(max=stats[2][0], min=stats[2][1], avg=stats[2][2]),
        'Link distance': Stat(max=stats[3][0], min=stats[3][1], avg=stats[3][2]),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': collections.Counter(getattr(link, 'highway_type') for link in roads.iterlinks())
        # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
